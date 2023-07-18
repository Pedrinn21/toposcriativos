from django.urls import path
from tipoproduto import views

urlpatterns = [
    path('list/', views.list, name="tipoproduto.list"),
    path('insert/', views.insert, name="tipoproduto.insert"),
    path('update/<int:id>/', views.update, name="tipoproduto.update"),
    path('delete/<int:id>/', views.delete, name="tipoproduto.delete"),
]
