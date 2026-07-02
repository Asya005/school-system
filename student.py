class Student:
    """Student class that stores student data and grades."""

    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name
        self.courses = []
        self.grades = []

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @classmethod
    def from_text(cls, text):
        sid, name = text.split(",")
        return cls(sid.strip(), name.strip())

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"])

    def add_course(self, course):
        self.courses.append(course)

    def add_grade(self, grade):
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be 0-100")
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def report(self):
        text = f"\nStudent: {self.__name}\nID: {self.__student_id}\n"
        for i, g in enumerate(self.grades, 1):
            text += f"Grade {i}: {g}\n"
        text += f"Average: {self.calculate_average()}\n"
        return text

    def __str__(self):
        return f"{self.__student_id} | {self.__name}"

    def __repr__(self):
        return self.__str__()
