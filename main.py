

class Student:
    def __init__(self, name, surname, gender):
        self.average = "Оценка не выставлена"
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        i = 0
        summ = 0
        for values in self.grades.values():
            for value in values:
                i += 1
                summ += value
        if i != 0:
            self.average = summ / i

    def __lt__(self, other):
        self.average_grade()
        other.average_grade()
        if not isinstance(other, Student):
            print("Cравнение невозможно")
            return
        return self.average < other.average

    def __str__(self):
            self.average_grade()
            res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses) if len(self.finished_courses) != 0 else " Пока нет завершённых курсов"}'
            return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average = 0

    def average_grade(self):
        Student.average_grade(self)

    def __str__(self):
        self.average_grade()
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {round(self.average, 2)}'
        return res

    def __lt__(self, other):
        self.average_grade()
        other.average_grade()
        if not isinstance(other, Lecturer):
            print('Сравнение невозможно')
            return
        return self.average < other.average

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
            res = f'Имя: {self.name} \nФамилия: {self.surname}'
            return res

first_student = Student('Ruoy', 'Eman', 'male')
first_student.courses_in_progress = ['Math', 'English']

second_student = Student('Veronika', 'Love', 'female')
second_student.courses_in_progress = ['Math', 'English']


first_reviewer = Reviewer('Marusya', 'Klimova')
first_reviewer.courses_attached = ['Math', 'English']

second_reviewer = Reviewer('Anna', 'Shifman')
second_reviewer.courses_attached = ['Math', 'English']

first_lecturer = Lecturer('Nikolas', 'Cage')
first_lecturer.courses_attached = ['Math']

second_lecturer = Lecturer('Pavlik', 'Morozov')
second_lecturer.courses_attached = ['Math']


first_student.rate_hw(first_lecturer, 'Math', 6)
first_student.rate_hw(second_lecturer, 'Math', 8)
second_student.rate_hw(first_lecturer, 'Math', 4)
second_student.rate_hw(second_lecturer, 'Math', 2)

first_reviewer.rate_hw(first_student, 'Math', 4)
first_reviewer.rate_hw(second_student, 'Math', 7)
second_reviewer.rate_hw(first_student, 'English', 6)
second_reviewer.rate_hw(second_student, 'English', 8)

first_reviewer.rate_hw(first_student, 'English', 7)
first_reviewer.rate_hw(second_student, 'English', 9)
second_reviewer.rate_hw(first_student, 'Math', 3)
second_reviewer.rate_hw(second_student, 'Math', 5)

print(f'{first_student} \n{second_student} \n{first_lecturer} \n{second_lecturer} \n{first_reviewer} \n{second_reviewer}')

print(first_student < second_student)
print(first_lecturer < second_lecturer)

students = [first_student.grades, second_student.grades]
lecturers = [first_lecturer.grades, second_lecturer.grades]

def students_average(student_list, course_name):
    res = 0
    count = 0
    for student in student_list:
        for i, value in student.items():
            if i == course_name:
                count += len(value)
                res += sum(value)
    average = res/count

    print(f'Средняя оценка студентов по курсу {course_name}: {round(average, 2)}')
students_average(students, "Math")
students_average(students, "English")

def average_lecturers(lecturers_list, course_name):
    res = 0
    count = 0
    for lecture in lecturers_list:
        for key, value in lecture.items():
            if key == course_name:
                count += len(value)
                res += sum(value)
    average = res / count
    print(f'Средняя оценка лекторов по курсу {course_name}: {round(average, 2)}')

average_lecturers(lecturers, "Math")

