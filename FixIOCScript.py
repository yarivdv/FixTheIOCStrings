def remove_duplicate_rows(input_file, output_file):
    # Step 1: Read the contents of the input file with 'utf-8' encoding
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Step 2: Create a set to store unique lines
    unique_lines = set()

    # Step 3: Iterate through each line and add it to the set
    for line in lines:
        unique_lines.add(line)

    # Step 4: Write the unique lines back to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(unique_lines)


def remove_leading_spaces_and_sort(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:  # Specify the correct encoding
        lines = file.readlines()

    modified_lines = [line.lstrip() for line in lines]
    sorted_lines = sorted(modified_lines)

    with open(output_file, 'w', encoding='utf-8') as file:  # Specify the correct encoding
        file.writelines(sorted_lines)

if __name__ == "__main__":
    input_file = r'C:\Users\User\Desktop\IOCStrings.txt'
    output_file = r'C:\Users\User\Desktop\output.txt'

    remove_duplicate_rows(input_file, output_file)
    remove_leading_spaces_and_sort(output_file, output_file)
