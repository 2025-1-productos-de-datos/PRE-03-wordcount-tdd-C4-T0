import os


def read_all_lines(input_folder):
    lines = []
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        with open(file_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines