import os
import uuid
import itertools
import click

mkdir_path = None
num_of_dir = None
dig_depth = None
dirname_length = None


def init_dir():
    if not os.path.exists(mkdir_path):
        os.makedirs(mkdir_path)


def get_randname():
    return uuid.uuid4().hex[:dirname_length]


def gen_dirs(names):
    dir_list = []
    for i in reversed(range(len(names)-1)):
        names[i] = list(itertools.chain.from_iterable(itertools.repeat(x,
                                                                       int(len(names[i+1])/len(names[i])))
                                                                        for x in names[i]))
    for i in range(len(names[0])):
        dir_list.append([row[i] for row in names])
    for dir, i in zip(dir_list, range(len(dir_list))):
        path = os.path.join(mkdir_path, '')
        for f in dir:
            path = os.path.join(path, f)
        os.makedirs(path)


def gen_names():
    depth_names = []
    num_of_fol = 1
    name_list = []
    for i in range(dig_depth):
        num_of_fol = num_of_fol * num_of_dir
        for j in range(num_of_fol):
            depth_names.append(get_randname())
        name_list.append(list(depth_names))
        del depth_names[:]
    return name_list


@click.command()
@click.option('--path', '-p', default=os.getcwd(), help="Bulk Directory Creation Path")
@click.option('--num', '-n', default=1, help="Number of folders to create in each directory")
@click.option('--depth', '-d', default=1, help="Directory tree depth")
@click.option('--length', '-l', default=5, help="Directory name length")
def main(path, num, depth, length):
    global mkdir_path, num_of_dir, dig_depth, dirname_length
    mkdir_path = path
    num_of_dir = num
    dig_depth = depth
    dirname_length = length
    init_dir()
    gen_dirs(gen_names())
