
import subprocess
import sys

def test_day1():
    with open("input.txt", "w") as f:
        f.write("1721\n979\n366\n299\n675\n1456")
    result = subprocess.run([sys.executable, "day1.py", "input.txt"], capture_output=True, text=True)
    assert "514579" in result.stdout

