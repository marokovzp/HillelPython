from exceptions import GroupException

class Group:

    def __init__(self, number, max_students=10):
        self.number = number
        self.group = set()
        self.max_students = max_students

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise GroupException("Too many students")
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        else:
            return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students} '