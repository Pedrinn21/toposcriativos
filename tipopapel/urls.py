from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name="tipopapel.list"),
    path('insert/', views.insert, name="tipopapel.insert"),
    path('update', views.update, name="tipopapel.update"),
    path('delete', views.delete, name="tipopapel.delete"),
]
