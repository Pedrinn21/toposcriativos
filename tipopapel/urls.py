from django.urls import path
from tipopapel import views

urlpatterns = [
    path('list/', views.list, name="tipopapel.list"),
    path('insert/', views.insert, name="tipopapel.insert"),
    path('update/<int:id>/', views.update, name="tipopapel.update"),
    path('delete/<int:id>/', views.delete, name="tipopapel.delete"),
]
