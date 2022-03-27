from django.db import models

class Person(models.Model):

    name = models.CharField(max_length=80)
    age = models.IntegerField(default=0)
    
    def __repr__(self) -> str:
        return f'{self.name}, {self.age} years old.'
        
    def serialize(self):
        return {'id': self.id, 'name': self.name, 'age': self.age}
    
    def happyBirthday(self):
        self.age += 1
        self.save()

    def changeName(self, new_name):
        self.name = new_name
        self.save()
    
    def update_from_request(self, request):
        if 'name' in request.POST.keys():
            self.name = request.POST.get('name')
        if 'age' in request.POST.keys():
            self.age = request.POST.get('age')
        
        self.save()


class Office(models.Model):

    name = models.CharField(max_length=80)
    people_working = models.ManyToManyField(Person)
    
    def __repr__(self) -> str:
        return f"{self.name} employes {''.join([person.name for person in self.people_working])}"

    def serialize(self):
        return {'id': self.id, 'name': self.name, 'people_working': [person.serialize() for person in self.people_working.all()]}
    
    def startWorkingFor(self, person: Person):
        self.people_working.add(person.id)
        self.save()

    def finishedWorkingFor(self, person: Person):
        self.people_working.remove(person.id)
        self.save()
    
    def update_from_request(self, request, people_working= None):
        if 'name' in request.POST.keys():
            self.name = request.POST.get('name')
        if people_working is not None:
            for person in people_working:
                self.people_working.add(person.id)
        
        self.save()