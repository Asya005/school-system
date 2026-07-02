from student import Student

class School:
    """School system that manages students and grades."""

    total_students = 0
    average = 0

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.student_id in self.students:
            print("Student already exists")
            return

        self.students[student.student_id] = student
        School.total_students += 1
        self.update_average()

    def set_grade(self, student_id, grade):
        if student_id not in self.students:
            print("Student not found")
            return

        self.students[student_id].add_grade(grade)
        self.update_average()

    def update_average(self):
        if not self.students:
            School.average = 0
            return

        total = sum(s.calculate_average() for s in self.students.values())
        School.average = total / len(self.students)

    def top_3(self):
        return sorted(self.students.values(),key=lambda s: s.calculate_average(),reverse=True)[:3]

    def search(self, text):
        return [s for s in self.students.values() if text.lower() in s.name.lower()]

    def export(self):
        with open("report.txt", "w", encoding="utf-8") as f:
            for s in self.students.values():
                f.write(s.report() + "\n")
