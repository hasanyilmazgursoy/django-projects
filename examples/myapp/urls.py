from django.urls import path  # URL tanımlamak için gerekli
from . import views  # Aynı dizindeki views.py dosyasını import ediyoruz

# Bu uygulamaya ait URL eşlemeleri burada tanımlanır.
urlpatterns = [
    path('', views.index, name='index'),  # /products/ adresi index fonksiyonuna gider (ana sayfa gibi)
    path('index', views.index, name='index'),  # /products/index adresi de aynı şekilde index fonksiyonuna gider

    # /products/5 gibi bir URL'de category_id parametresi integer olarak alınır
    # Bu URL örneğin: ürün kategorisini ID'ye göre filtrelemek için kullanılabilir
    path('<int:category_id>', views.getproductByCategoryId),

    # /products/electronics gibi bir URL'de category parametresi string olarak alınır
    # Bu da kategori adına göre ürünleri filtrelemek için kullanılır
    path('<str:category>', views.getproductByCategory, name='products_by_category'),
]
