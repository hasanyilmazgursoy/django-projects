from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

# Kategorilere karşılık gelen açıklamaları içeren sözlük
data = {
    "telefon": ["samsung s20", "iphone 12", "xiaomi mi 11"],
    "bilgisayar": ["dell xps 13", "macbook pro", "lenovo thinkpad"],
    "elektronik": [ "radyo", "buzdolabı"],
}

# /products/ veya /products/index adresine istek gelince çalışacak olan fonksiyon
def index(request):
    category_list = list(data.keys())  # ['telefon', 'bilgisayar', 'elektronik']

    return render(request, 'index.html', {"category_list": category_list})

# /products/<int:category_id> şeklinde gelen istekte çalışır
def getproductByCategoryId(request, category_id):
    category_list = list(data.keys())

    # Eğer ID, geçerli kategoriler arasında değilse hata döndür
    if category_id > len(category_list) or category_id < 1:
        return HttpResponseNotFound("Yanlış kategori seçimi yaptınız")

    category_name = category_list[category_id - 1]  # 1-indexli gibi çalışıyor
    # İlgili kategoriye ait URL'yi 'category_name' ile oluşturuyoruz
    redirect_path = reverse('products_by_category', args=[category_name])
    return redirect(redirect_path)  # Kullanıcıyı o URL'ye yönlendir

# /products/<str:category> şeklinde gelen istekte çalışır
def getproductByCategory(request, category):
    # Kategori adını kontrol et
    category = category.lower()  # Küçük harfe çevir, büyük/küçük harf farkını yok saymak için

    # Veriyi bulmaya çalış
    if category in data:
        products = data[category]
        return render(request, "products.html", {"category": category, "products": products})
    else:
        # Eğer kategori bulunamazsa, 404 hata mesajı döndür
        return HttpResponseNotFound(f"<h1>Yanlış kategori seçimi</h1>")

