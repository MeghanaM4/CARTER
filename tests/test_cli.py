import subprocess


def test_main():
    assert subprocess.check_output(["wonderwaller", "foo", "foobar"], text=True) == "foobar\n"
