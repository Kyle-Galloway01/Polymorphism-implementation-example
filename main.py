class Person:
    def __init__(self, personid, firstname, lastname):
        self.personid, self.firstname, self.lastname = personid, firstname, lastname
    def display(self):
        return f"{self.firstname} {self.lastname} (ID: {self.personid})"

class Student(Person):
    def __init__(self, personid, firstname, lastname):
        super().__init__(personid, firstname, lastname)
        self.courses = []
    def addCourse(self, course):
        pass
    def dropCourse(self, course):
        pass

class Faculty(Person):
    def __init__(self, personid, firstname, lastname):
        super().__init__(personid, firstname, lastname)
        self.courses = []
    def teachCourse(self, course):
        pass
    def dropCourse(self, course):
        pass

class Staff(Person):
    def __init__(self, personid, firstname, lastname, dept):
        super().__init__(personid, firstname, lastname)
        self.dept = dept
    def assist(self):
        pass

persons = [Student(1, "Terry", "Aki"), Student(2, "Bud", "Derfinger"), Faculty(3, "Colby", "Jack"), 
           Faculty(4, "Halla", "Penyo"), Staff(5, "Mac", "Donald", "Human Resources")]

for person in persons:
    print(person.display())