from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound  # HTTP cevapları için gerekli sınıflar
from django.shortcuts import redirect  # Kullanıcıyı başka bir URL'ye yönlendirmek için
from django.urls import reverse  # URL'leri name parametresine göre dinamik oluşturmak için

# Kategorilere ait verileri tutan sözlük (kategori ismi => açıklama)
data = {
    "telefon": "telefon kategorisindeki ürünler",
    "bilgisayar": "bilgisayar kategorisindeki ürünler",
    "elektronik": "elektronik kategorisindeki ürünler",
}

# Not: Alttaki liste şu an kullanılmıyor, sadece örnek amaçlı orada
["telefon", "bilgisayar", "elektronik"]

# /products/ veya /products/index adresine istek gelince çalışacak olan fonksiyon
def index(request):
    return HttpResponse("index")  # Tarayıcıya "index" yazısı gönderilir

# /products/details adresine istek gelince çalışır
def details(request):
    return HttpResponse("details")  # Tarayıcıya "details" yazısı gönderilir

# /products/<int:category_id> şeklinde gelen istekte çalışır
# Sayısal ID'ye göre doğru kategoriye yönlendirir
def getproductByCategoryId(request, category_id):
    category_list = list(data.keys())  # Kategori isimlerini listeye çeviriyoruz (örn: ['telefon', 'bilgisayar', 'elektronik'])

    if category_id > len(category_list) or category_id < 1:
        return HttpResponseNotFound("yanlış kategori seçimi yaptınız")  # Geçersiz ID girildiyse hata döner

    category_name = category_list[category_id - 1]  # ID ile doğru kategori ismi eşleştirilir (1-indexli gibi çalışıyor)

    redirect_path = reverse('products_by_category', args=[category_name])  # İlgili kategori için URL'yi dinamik oluştur

    return redirect(redirect_path)  # Kullanıcıyı o URL'ye yönlendir

# /products/<str:category> şeklinde gelen istekte çalışır
# Kategori adına göre açıklamayı döndürür
def getproductByCategory(request, category):
    try:
        category_text = data[category]  # Sözlükten kategori açıklaması alınır
        return HttpResponse(category_text)  # Tarayıcıya açıklama gönderilir
    except:
        return HttpResponseNotFound("yanlış kategori seçimi yaptınız")  # Kategori bulunamazsa 404 mesajı döner
