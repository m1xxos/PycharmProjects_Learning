# the list "students" is already defined
students = [["Will", "B"], ["Kate", "B"], ["Max", "A"], ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]
print([students[stud][0] for stud in range(len(students)) if students[stud][1] == "A"])
