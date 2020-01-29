from django.urls import path

from . import views

urlpatterns = [
    path('', views.most_wanted_list, name='most_wanted_list'),
    path('wanted_person_details/<int:id>', views.wanted_person_details, name='wanted_person_details'),

]