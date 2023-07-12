from django.urls import path
from materiaprima import views

urlpatterns = [
    path('list/', views.list, name="materiaprima.list"),
    path('insert/', views.insert, name="materiaprima.insert"),
    path('update/<int:id>/', views.update, name="materiaprima.update"),
    path('delete/<int:id>/', views.delete, name="materiaprima.delete"),
]
