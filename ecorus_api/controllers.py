from django.views import View
from django.http import JsonResponse

from .models import Office, Person

class Controller:
    def wrap_for_repsonse(self, payload):

        payload = {'data': payload}
        return JsonResponse(payload)

class PersonController(View, Controller):

    def get(self, request):

        persons_data = [person.serialize() for person in Person.objects.all()]
        
        return self.wrap_for_repsonse(persons_data)

    def post(self, request):        

        person_fields = {
            'name': request.POST.get('name', ''),
            'age': request.POST.get('age', 0),
        }

        person = Person.objects.create(**person_fields)

        return self.wrap_for_repsonse(person.serialize())

class PersonUpdateController(View, Controller):

    def patch(self, request, person_id):
        person = Person.objects.get(id=person_id)
        person.update_from_request(request)
        person.save()

        return self.wrap_for_repsonse(person.serialize())
    
    def delete(self, request, person_id):
        person = Person.objects.get(id=person_id)
        person.delete()

        return self.wrap_for_repsonse(f'Person {person_id} has been deleted')

class OfficeController(View, Controller):
    
    def get(self, request):

        offices_data = [office.serialize() for office in Office.objects.all()]

        return self.wrap_for_repsonse(offices_data)
    
    def post(self, request):

        people_working = [Person.objects.get(id) for id in request.POST.get('people_working', [])]
        
        office_fields = {
            'name': request.POST.get('name', ''),
            'people_working': people_working,
        }
        office = Office.objects.create(**office_fields)

        return self.wrap_for_repsonse(office.serialize())

class OfficeUpdateController(View, Controller):    
    def patch(self, request, office_id):

        office = Office.objects.get(id= office_id)
        people_working = [Person.objects.get(id) for id in request.POST.get('people_working', [])]

        office.update_from_request(request, people_working)
        office.save()

        return self.wrap_for_repsonse()
    
    def delete(self, request, office_id):
        office = Office.objects.get(id=office_id)
        office.delete()

        return self.wrap_for_repsonse(f'Office {office_id} has been deleted')