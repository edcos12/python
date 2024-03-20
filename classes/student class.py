class student:
    def __init__(self, age, name, class_num):
        self.age = age
        self.name = name
        self.class_num = class_num

    def set_age(self):
        self.age = input("age: ")

    def set_name(self):
        self.name = input("name: ")

    def set_class_num(self):
        self.class_num = input("class number: ")

    def set_grades(self):
        score1 = int(input("grade 1: "))
        score2 = int(input("grade 2: "))
        score3 = int(input("grade 3: "))

        self.avg = round(score1 + score2 + score3 / 3, 2)

    def get_average_score(self):
        return "average grade: " + str(self.avg) 

    def get_age(self):
        return "age: " + str(self.age)
    
    def get_name(self):
        return "name: " + self.name
    
    def get_class_num(self):
        return "class: " + self.class_num
    
student1 = student
student.set_name(student1)
student.set_age(student1)
student.set_class_num(student1)
student.set_grades(student1)
print("student1: ")
print(student.get_name(student1))
print(student.get_age(student1))
print(student.get_class_num(student1))
print(student.get_average_score(student1))
