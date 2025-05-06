from django.contrib import admin  # Admin paneli için gerekli import
from django.urls import path, include  # URL tanımlamaları ve başka url dosyalarını dahil etmek için

# Tarayıcıda http://127.0.0.1:8000/ adresine gidildiğinde hangi uygulama çalışacak onu belirler
urlpatterns = [
    path('products/', include('myapp.urls')),  # /products/ ile başlayan URL'leri myapp uygulamasına yönlendirir
    path('admin/', admin.site.urls),  # /admin/ adresi Django admin paneline gider
]
