import working_sim
import logging

LOGGER = logging.getLogger(__name__)

class TestClass:
    def test_office_creation(self):
        office = working_sim.Office(name= 'Ecorus')
        LOGGER.info(F'Created office {office}')

        assert office.name == 'Ecorus'
        assert isinstance(office.people_working, list)

    def test_persons_creation(self):
        eduardo = working_sim.Person(name='Eduardo')
        boris = working_sim.Person(name='Boris')
        LOGGER.info(f'Created persons {eduardo}, {boris}')

        assert eduardo.name == 'Eduardo'
        assert eduardo.age == 0

        assert boris.name == 'Boris'
        assert boris.age == 0
    
    def test_office_startworking(self):
        eduardo = working_sim.Person(name='Eduardo')
        boris = working_sim.Person(name='Boris')
        LOGGER.info(f'Created persons {eduardo}, {boris}')
        
        office = working_sim.Office(name= 'Ecorus')
        LOGGER.info(f'Created office {office}')

        office.startWorkingFor(eduardo)
        office.startWorkingFor(boris)
        LOGGER.info(f'Office gained employees {office}')

        assert eduardo in office.people_working
        assert boris in office.people_working
    
    def test_office_stopworking(self):
        boris = working_sim.Person(name='Boris')
        eduardo = working_sim.Person(name='Eduardo')
        LOGGER.info(f'Created person {eduardo}')
        office = working_sim.Office(name= 'Ecorus')
        LOGGER.info(f'Created office {office}')

        office.startWorkingFor(boris)
        office.startWorkingFor(eduardo)
        LOGGER.info(f'Office gains employees. {office}')
        office.finishedWorkingFor(eduardo)
        LOGGER.info(f'Office looses an employee. {office}')

        assert eduardo not in office.people_working


