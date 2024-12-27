import subprocess
import sys

def test_day1():
    print("Running day1 tests...")

    with open("input.txt", "w") as f:
        f.write("1721\n979\n366\n299\n675\n1456")
    
    result = subprocess.run([sys.executable, "day1.py", "input.txt"], capture_output=True, text=True)
    
    # Print the captured output
    # print("Captured stdout:")
    # print(result.stdout)
    # print("Captured stderr:")
    # print(result.stderr)
    
    assert "241861950" in result.stdout, f"Expected output to contain 241861950, but got {result.stdout}"

if __name__ == "__main__":
    test_day1()

