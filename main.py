from school import School
from student import Student
from course import Course

school = School()

while True:
    print("""
1 Add student (text)
2 Add student (dict)
3 Add course
4 Add grade
5 Show report
6 Top 3
7 Search
8 Export
0 Exit
""")

    try:
        choice = input("Choose: ")

        if choice == "1":
            student = Student.from_text(input("id,name: "))
            school.add_student(student)

        elif choice == "2":
            sid = input("ID: ")
            name = input("Name: ")
            student = Student.from_dict({"id": sid, "name": name})
            school.add_student(student)

        elif choice == "3":
            sid = input("Student ID: ")
            course = Course(
                input("Code: "),
                input("Name: "),
                int(input("Credits: "))
            )
            school.students[sid].add_course(course)

        elif choice == "4":
            school.set_grade(input("ID: "), int(input("Grade: ")))

        elif choice == "5":
            print(school.students[input("ID: ")].report())

        elif choice == "6":
            for s in school.top_3():
                print(s, s.calculate_average())

        elif choice == "7":
            print(school.search(input("Search: ")))

        elif choice == "8":
            school.export()
            print("Exported")

        elif choice == "0":
            break

    except Exception as e:
        print("Error:", e)
