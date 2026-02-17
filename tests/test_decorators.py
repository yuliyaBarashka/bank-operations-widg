import pytest

from src.decorators import log


def test_log_success_console(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert "add ok" in captured.out


def test_log_error_console(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_success_file(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    multiply(2, 3)

    content = log_file.read_text(encoding="utf-8")
    assert "multiply ok" in content


def test_log_error_file(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def fail():
        raise ValueError("boom")

    with pytest.raises(ValueError):
        fail()

    content = log_file.read_text(encoding="utf-8")
    assert "fail error" in content
    assert "boom" in content
