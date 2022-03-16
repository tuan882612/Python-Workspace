class student:
    def __init__(self):
        self.name = []
        self.grade = []
        
    def totalObtained(self):
        return sum(self.grade)

    def percentage(self):
        print(self.name,"\n",self.grade)
        return self.totalObtained()/len(self.grade)
    
if __name__ == "__main__":
    tom = student()
    grades = {"physic":93,"chemistry":90,"programming":96,"calculus":89}
    for classes, grade in grades.items():
        tom.name.append(classes)
        tom.grade.append(grade)
    print(tom.__dict__)
    print(tom.totalObtained())
    print(tom.percentage())