def compare_files(file1_path, file2_path):
    # Open and read the two files
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    # Ensure both files have the same number of lines
    if len(file1_lines) != len(file2_lines):
        print(f"The files have different lengths: {len(file1_lines)} vs {len(file2_lines)} lines.")
        return

    # Initialize counters
    total_lines = len(file1_lines)
    matching_lines = 0
    different_lines = []

    # Compare line by line
    for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines), start=1):
        if line1.strip() == line2.strip():
            matching_lines += 1
        else:
            different_lines.append((i, line1.strip(), line2.strip()))

    # Calculate percentage of identical lines
    percentage_match = (matching_lines / total_lines) * 100

    # Output the results
    print(f"Percentage of matching lines: {percentage_match:.2f}%")

    if different_lines:
        print("\nLines that differ:")
        for diff in different_lines:
            print(f"Line {diff[0]}:\nFile 1: {diff[1]}\nFile 2: {diff[2]}\n")
    else:
        print("The files are identical.")


compare_files('final_genres.txt', 'predicted_genres.txt')
