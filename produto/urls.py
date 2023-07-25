from django.urls import path
from produto import views

urlpatterns = [
    path('list/', views.list, name="produto.list"),
    path('insert/', views.insert, name="produto.insert"),
    path('update/<int:id>/', views.update, name="produto.update"),
    path('delete/<int:id>/', views.delete, name="produto.delete"),
]
