import bulk_directory_tree as bdt


def test_get_randname_length():
    bdt.dirname_length = 8
    name = bdt.get_randname()
    assert len(name) == 8


def test_gen_names_structure():
    bdt.num_of_dir = 2
    bdt.dig_depth = 3
    bdt.dirname_length = 4
    names = bdt.gen_names()
    assert len(names) == 3
    for i, level in enumerate(names, start=1):
        assert len(level) == 2 ** i

