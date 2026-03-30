from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Isso diz para o Django: "qualquer outra rota, vá procurar na pasta app"
    path('', include('app.urls')), 
]