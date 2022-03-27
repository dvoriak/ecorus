from django.urls import path
from .views import happyBirthday, changeName, startWorkingFor, finishedWorkingFor
from .controllers import PersonController, PersonUpdateController, OfficeController, OfficeUpdateController

urlpatterns = [
    path('persons/', PersonController.as_view()),
    path('persons/<person_id>', PersonUpdateController.as_view()),
    path('persons/<person_id>/happybirthday', happyBirthday),
    path('persons/<person_id>/changename', changeName),

    path('offices/', OfficeController.as_view()),
    path('offices/<office_id>', OfficeUpdateController.as_view()),
    path('offices/<office_id>/startworkingfor', startWorkingFor),
    path('offices/<office_id>/finishedworkingfor', finishedWorkingFor),
]