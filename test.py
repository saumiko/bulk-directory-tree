import pytest
from bulk_directory_tree import main


def test_main():
    with pytest.raises(TypeError):
        main(9,'f','u','c')