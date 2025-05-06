from django.urls import path  # URL tanımlamak için gerekli
from . import views  # Aynı dizindeki views.py dosyasını import ediyoruz

# Bu uygulama içindeki URL eşlemeleri:
urlpatterns = [
    path('', views.index, name='index'),  # /products/ adresi index fonksiyonuna gider
    path('index', views.index, name='index'),  # /products/index adresi de aynı şekilde index fonksiyonuna gider
    path('details', views.details, name='details'),  # /products/details adresi details fonksiyonunu çağırır
    path('list', views.list, name='list'),  # /products/list adresi list fonksiyonunu çağırır
    path('<category>', views.getproductByCategory),  # /products/<category> şeklinde dinamik kategori URL'si
]
