with open("ninja.txt", "r") as ninja_file:
    lines_list = ninja_file.read().splitlines()

with open("ninja.txt", "w") as ninja_file:
    next_line = "this is the last line"
    lines_list.append(next_line)
    print(lines_list)
    lines_list_string = "\n".join(lines_list)
    ninja_file.write(lines_list_string)
