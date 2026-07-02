class Course:
    """Course class that stores course information."""

    def __init__(self, course_code, name, credits):
        self.course_code = course_code
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"{self.course_code} | {self.name} | {self.credits}"

    def __repr__(self):
        return self.__str__()
