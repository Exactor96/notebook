from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'note'

urlpatterns = [
    path('add/', views.add_note, name='add_note'),
    path('detail/<int:id>', views.detail_note, name='detail_note'),
    path('', views.notes_list_index, name='note_list'),

]
