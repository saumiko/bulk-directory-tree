from click.testing import CliRunner
from bulk_directory_tree import main
import os


def test_cli_creates_directories(tmp_path):
    runner = CliRunner()
    root = tmp_path / "root"
    result = runner.invoke(main, ["-p", str(root), "-n", "2", "-d", "2", "-l", "4"])
    assert result.exit_code == 0
    first_level = [p for p in root.iterdir() if p.is_dir()]
    assert len(first_level) == 2
    for d in first_level:
        second_level = [p for p in d.iterdir() if p.is_dir()]
        assert len(second_level) == 2

