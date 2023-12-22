from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   
    path("", views.index, name='login'),
    path("hm", views.hm, name='hm'),
    path("taskm", views.taskm, name='taskmanager'),
    path("filem", views.filem, name='filem'),
    path("fileup", views.fileupload, name='fileupload')
]
