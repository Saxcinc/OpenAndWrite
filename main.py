def merge_file(*file):
    file_content = {}
    count = 0

    for page in file:
        with open(page) as f:
            for _ in f:
                count += 1
            file_content[count] = page
            count = 0
    ab = dict(sorted(file_content.items()))

    for item in ab.items():
        with open(item[1]) as file1, open("output.txt", "a") as file2:
            file2.write(item[1])
            file2.write("\n")
            file2.write(str(item[0]))
            file2.write("\n")
            for it in file1:
                file2.write(it)
            file2.write("\n")


merge_file("1.txt", "2.txt", "3.txt")
