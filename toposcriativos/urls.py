from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('tipopapel/', include('tipopapel.urls')),
    path('materiaprima/', include('materiaprima.urls')),
    path('tipoproduto/', include('tipoproduto.urls')),
    path('produto/', include('produto.urls')),
    
]
