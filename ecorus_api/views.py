from django.views import View
from django.http import JsonResponse

from .models import Office, Person


def happyBirthday(request, person_id):

    person = Person.objects.get(id=person_id)
    person.happyBirthday()

    return JsonResponse({'data': person.serialize()})

def changeName(request, person_id):

    person = Person.objects.get(id=person_id)
    person.changeName(request.POST.get('name'))

    return JsonResponse({'data': person.serialize()})


def prepare_objects_from_ids(request, office_id):
        office = Office.objects.get(id=office_id)
        people_ids = request.POST.get('people_ids', '').split(',')
        persons = [Person.objects.get(id=person_id) for person_id in people_ids]

        return office, persons

def startWorkingFor(request, office_id):
    office, persons = prepare_objects_from_ids(request, office_id)

    for person in persons:
        office.startWorkingFor(person)
    
    return JsonResponse({'data': office.serialize()})

def finishedWorkingFor(request, office_id):
    office, persons = prepare_objects_from_ids(request, office_id)

    for person in persons:
        office.finishedWorkingFor(person)
    
    return JsonResponse({'data': office.serialize()})