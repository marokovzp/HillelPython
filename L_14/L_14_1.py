class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)  # ✅ Use super()
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Group:

    def __init__(self, number, max_students=10):
        self.number = number
        self.group = set()
        self.max_students = max_students

    def add_student(self, student):
        if len(self.group) < self.max_students:
            self.group.add(student)
        else:
            raise ValueError("Too many students")

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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
# print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
# print(gr)  # Only one student

for i in range (9):
    new_st = Student("Male", 30, f"Student{i+1}", f"Jobs", f"AN{145+i}")
    gr.add_student(new_st)
print(gr)


try:
    gr.add_student(st2)
except ValueError as e:
    print(e)