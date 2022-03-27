from django.test import TestCase
from .models import Person, Office

class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name='Boris')
        Person.objects.create(name='Eduardo', age=27)

    def test_person_can_have_bday(self):
        """Birthday method can be called and age increases"""
        boris =     Person.objects.get(name='Boris')
        eduardo =   Person.objects.get(name='Eduardo')
        
        boris.happyBirthday()
        eduardo.happyBirthday()

        self.assertEqual(boris.age, 1)
        self.assertEqual(eduardo.age, 28)
    
    def test_person_bday_persists(self):
        """Birthday age change persists in db"""
        boris = Person.objects.get(name='Boris')
        
        boris.happyBirthday()
        boris = Person.objects.get(name='Boris')

        self.assertEqual(boris.age, 1)
        
    def test_person_can_change_name(self):
        """Name change method can be called and name changes"""
        boris =     Person.objects.get(name='Boris')

        boris.changeName('The Blade')

        self.assertEqual(boris.name, 'The Blade')
    
    def test_person_change_name_persists(self):
        """Name change persists in db"""
        boris = Person.objects.get(name='Boris')

        boris.changeName('The Blade')
        boris = Person.objects.get(name='The Blade')

        self.assertEqual(boris.name, 'The Blade')
    

    
class OfficeTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name='Boris')
        Person.objects.create(name='Eduardo', age=27)

        Office.objects.create(name='Ecorus')

    def test_can_start_working(self):
        """A Person can start working in the office"""
        boris = Person.objects.get(name='Boris')
        eduardo = Person.objects.get(name='Eduardo')
        ecorus = Office.objects.get(name='Ecorus')

        ecorus.startWorkingFor(boris)
        ecorus.startWorkingFor(eduardo)

        self.assertListEqual(list(ecorus.people_working.all()), [boris, eduardo])
        self.assertListEqual(list(boris.office_set.all()), [ecorus])
        self.assertListEqual(list(eduardo.office_set.all()), [ecorus])
    
    def test_start_working_persists(self):
        """Person - Office mtm relationsihp persists"""
        boris = Person.objects.get(name='Boris')
        eduardo = Person.objects.get(name='Eduardo')
        ecorus = Office.objects.get(name='Ecorus')

        ecorus.startWorkingFor(boris)
        ecorus.startWorkingFor(eduardo)

        boris = Person.objects.get(name='Boris')
        eduardo = Person.objects.get(name='Eduardo')
        ecorus = Office.objects.get(name='Ecorus')

        self.assertListEqual(list(ecorus.people_working.all()), [boris, eduardo])
        self.assertListEqual(list(boris.office_set.all()), [ecorus])
        self.assertListEqual(list(eduardo.office_set.all()), [ecorus])
    
    def test_can_stop_working(self):
        """A Person can stop working in the office"""
        boris = Person.objects.get(name='Boris')
        eduardo = Person.objects.get(name='Eduardo')
        ecorus = Office.objects.get(name='Ecorus')

        ecorus.startWorkingFor(boris)
        ecorus.startWorkingFor(eduardo)
        ecorus.finishedWorkingFor(eduardo)

        self.assertListEqual(list(ecorus.people_working.all()), [boris])
        self.assertListEqual(list(boris.office_set.all()), [ecorus])
        self.assertListEqual(list(eduardo.office_set.all()), [])
    
    def test_stop_working_persists(self):
        """Person - Office relationship is removed from db"""
        boris = Person.objects.get(name='Boris')
        eduardo = Person.objects.get(name='Eduardo')
        ecorus = Office.objects.get(name='Ecorus')

        ecorus.startWorkingFor(boris)
        ecorus.startWorkingFor(eduardo)
        ecorus.finishedWorkingFor(eduardo)

        boris = Person.objects.get(name='Boris')
        eduardo = Person.objects.get(name='Eduardo')
        ecorus = Office.objects.get(name='Ecorus')

        self.assertListEqual(list(ecorus.people_working.all()), [boris])
        self.assertListEqual(list(boris.office_set.all()), [ecorus])
        self.assertListEqual(list(eduardo.office_set.all()), [])