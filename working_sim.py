class Person:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        return f'{self.name}, {self.age} years old.'
        
    def happyBirthday(self):
        self.age += 1

    def changeName(self, new_name):
        self.name = new_name


class Office:
    def __init__(self, name= '', people_working= None):
        if people_working is None:
            self.people_working = []
        self.name = name
    
    def __repr__(self) -> str:
        return f"{self.name} employes {', '.join([person.name for person in self.people_working])}"

    def startWorkingFor(self, person: Person):
        self.people_working.append(person)

    def finishedWorkingFor(self, person: Person):
        self.people_working.remove(person)