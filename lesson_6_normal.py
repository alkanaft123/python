# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:


class School():
    students: dict
    _teachers: list
    classes: list

    def __init__(self, class_rooms):
        self.classes = []
        for class_room in class_rooms:
            if not class_room in self.classes:
                self.classes.append(class_room)
            else:
                print('This class is already exist in school')
        self.students = {}
        self._teachers = []

    # getters
    def get_students(self, class_room):
        return [key for key, value in self.students.items() if value == class_room]

    def get_teachers_by_classroom(self, clas) -> tuple:
        teacher_lst = []
        for teacher in self._teachers:
            for iter_cl in teacher.classes.keys():
                if iter_cl == clas:
                    teacher_lst.append(teacher)
        return tuple(set(teacher_lst))

    def get_subjects(self, student):
        lst = []
        class_room = self.students[student]
        for tchr in self.teachers:
            for key, value in tchr.classes.items():
                if key == class_room:
                    lst.append(value)
        return lst

    # setters
    # исхожу из логики, что учитель может преподавать предмет даже если его уже кто-то преподает в принципеб но в других классах
    # то есть не могут два учителя преподавать один и тот же предмет в одном классе
    def add_teacher(self, teacher):
        flag = True
        for key, value in teacher.classes.items():
            for tchr in self._teachers:
                for key_2, value_2 in tchr.classes.items():
                    if key == key_2 and value == value_2:
                        flag = False
        self._teachers.append(teacher) if flag else print('Invalid classrooms and subjects for ',teacher.get_name(),sep='')


class Person:
    name: str = ''
    surname: str = ''

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return f'{self.name} {self.surname}'


class Student(Person):
    father: Person = None
    mother: Person = None

    def __init__(self, name: str, surname: str, father: Person, mother: Person):
        Person.__init__(self, name, surname)
        self.name = name
        self.surname = surname

        if father is mother:
            print('Mother and father cant be the same person')
        else:
            self.father = father
            self.mother = mother


class Teacher(Person):
    classes: dict = {}

    def __init__(self, name, surname, classes: dict):
        Person.__init__(self, name, surname)
        self.classes = classes


if __name__ == '__main__':
    school_1 = School(['5A', '6B'])

    dict_1 = {'5A': 'math', '6B': 'geometry'}
    teacher_1 = Teacher('Jhon', 'Doe', dict_1)
    dict_2 = {'3A': 'georaphy', '6B': 'biology'}
    teacher_2 = Teacher('Arthur', 'Brown', dict_2)

    teacher_3 = Teacher('Mark', 'White', dict_2)

    school_1.add_teacher(teacher_1)
    school_1.add_teacher(teacher_2)
    school_1.add_teacher(teacher_3)

    parent_1 = Person('Peter', 'Parker')
    parent_2 = Person('Jesica', 'Parker')
    parent_3 = Person('Peter', 'Black')
    parent_4 = Person('Jesica', 'Black')

    student_1 = Student('Mark', 'Parker', parent_1, parent_2)
    student_2 = Student('Lora', 'Black', parent_3, parent_4)

    school_1.students.update({student_1: '5A'})
    school_1.students.update({student_2: '5A'})

    # 1. Получить полный список всех классов школы DONE
    print(school_1.classes)
    # 2. Получить список всех учеников в указанном классе DONE
    #  (каждый ученик отображается в формате "Фамилия И.О.")

    print('In class-room 5A stydying:')
    for std in school_1.get_students('5A'):
        print(std.get_name())

    # 3. Получить список всех предметов указанного ученика
    #  (Ученик --> Класс --> Учителя --> Предметы)

    print('', student_1.get_name(), ' stydying ', ','.join(school_1.get_teachers_by_classroom(student_1)),sep='')
    # 4. Узнать ФИО родителей указанного ученика

    print('Parents of ', student_1.get_name(), ' are: ', student_1.father.get_name(), ' ', student_1.mother.get_name())

    # 5. Получить список всех Учителей, преподающих в указанном классе

    print(list(x.get_name() for x in school_1.get_teachers_by_classroom('5A')))
