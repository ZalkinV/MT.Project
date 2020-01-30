from pathlib import Path

FILES_PATH = Path(".")

def remove_wrong_lines(lines):
    correct_lines = []
    for line in lines:
        if line.strip() and not line.startswith("<"):
            correct_lines.append(line)
    return correct_lines


if __name__ == "__main__":
    filenames = FILES_PATH.glob("*.hea")

    print("Files was cleaned:")
    for filename in filenames:
        with open(filename, "r") as file:
            input_lines = file.readlines()
        
        output_lines = remove_wrong_lines(input_lines)
        
        with open(filename, "w") as file:
            file.writelines(output_lines)
        print("\t", filename, sep='')

