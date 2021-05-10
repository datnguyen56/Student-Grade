student_num = input("How many students do you have? ")
for i in range(2):
    name = input("Students name: ")
    grade = input("Students grade: ")
    course = input("Select a course: 1 - Math, 2 - Science, 3 - History: ")
    print("Name: {}, Grade: {}, Course: {}".format(name, grade, course))