import os
import shutil
import uuid
import itertools

mkdir_path = '/Users/saumiko/Desktop/Z/dirprac'
num_of_dir = 10
dirname_length = 5
depth = 4


def init_dir():
    if os.path.exists(mkdir_path):
        dirs = os.listdir(mkdir_path)
        for dir in dirs:
            try:
                shutil.rmtree(os.path.join(mkdir_path, dir))
            except:
                continue
    else:
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
    for i in range(depth):
        num_of_fol = num_of_fol * num_of_dir
        for j in range(num_of_fol):
            depth_names.append(get_randname())
        name_list.append(depth_names.copy())
        depth_names.clear()
    return name_list


init_dir()
gen_dirs(gen_names())