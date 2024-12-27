
def main():
    """Finds three numbers in a list that sum to 2020 and prints their product."""
    import sys
    input_file = sys.argv[1]
    file1 = open(input_file, "r")
    lines = file1.readlines()
    lines = [int(l) for l in lines]

    two_sum_indices = {}
    for i, a in enumerate(lines):
        for j, b in enumerate(lines):
            if i == j:
                continue
            two_sum_indices[a + b] = (i, j)

    for i, val in enumerate(lines):
        diff = 2020 - val
        if diff in two_sum_indices:
            if i == two_sum_indices[diff][0] or i == two_sum_indices[diff][1]:
                continue
            print(val * lines[two_sum_indices[diff][0]] * lines[two_sum_indices[diff][1]])
            break


if __name__ == "__main__":
    main()
