# write your code here
with open("salary.txt", "r") as file1:
    with open("salary_year.txt", "w") as file2:
        for line in file1:
            print(str(int(line) * 12), file=file2)
