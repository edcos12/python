class student:
    def __init__(self, age, name, class_num, score1, score2, score3):
        self.age = age
        self.name = name
        self.class_num = class_num
        self.score1 = score1 
        self.score2 = score2
        self.score3 = score3 

    def set_age(self):
        self.age = input("age: ")

    def set_name(self):
        self.name = input("name: ")

    def set_class_num(self):
        self.class_num = input("class number: ")

    def set_grades(self):
        self.score1 = int(input("grade 1: "))
        self.score2 = int(input("grade 2: "))
        self.score3 = int(input("grade 3: "))

    def create_student(self):
        self.set_name(self)
        self.set_age(self)
        self.set_class_num(self)
        self.set_grades(self)

    def get_average_score(self):
        self.avg = round((self.score1 + self.score2 + self.score3) / 3, 2)
        return "Average grade: " + str(self.avg) 

    def get_age(self):
        return "Age: " + str(self.age)
    
    def get_name(self):
        return "Name: " + self.name
    
    def get_class_num(self):
        return "Class: " + self.class_num
    
student1 = student("19", "Edward", "4B", 6, 5, 8 )
#student.create_student(student1)
print(f"Student1: \n {student.get_name(student1)} \n {student.get_age(student1)} \n {student.get_class_num(student1)} \n {student.get_average_score(student1)} ")
