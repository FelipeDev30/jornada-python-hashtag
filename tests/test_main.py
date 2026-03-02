import pytest
from src import main


def test_main_runs_without_errors(capsys):
    # just ensure main can be called and prints expected messages
    main.main()
    captured = capsys.readouterr()
    assert "script" in captured.out.lower()
