#from django.conf.urls import url
from django.urls import path
from .views import readdata, createdata, updatedata, deletedata
from simplecrud import views

urlpatterns = [
    path('read', readdata, name="readdata"),
    path('createdata', createdata, name="createdata"),
    path('updatedata/<int:id>', updatedata, name="updatedata"),
    path('deletedata/<int:id>', deletedata, name="deletedata"),
]