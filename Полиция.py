import os

input_files = ['1.txt', '2.txt']
file_info = []

for file in input_files:
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
            file_info.append((file, len(lines), lines))

file_info.sort(key=lambda x: x[1])

for file_name, line_count, lines in file_info:
    print(f"{file_name}\n{line_count}")
    print(''.join(lines), end='')
