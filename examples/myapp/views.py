from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound  # HTTP cevabı vermek için gerekli sınıflar
from django.shortcuts import redirect, render  # Kullanıcıyı başka bir sayfaya yönlendirmek için kullanılır
from django.urls import reverse  # URL'leri name değerine göre dinamik şekilde oluşturmak için kullanılır

# Kategorilere karşılık gelen açıklamaları içeren sözlük
data = {
    "telefon": "telefon kategorisindeki ürünler",
    "bilgisayar": "bilgisayar kategorisindeki ürünler",
    "elektronik": "elektronik kategorisindeki ürünler",
}

# Bu liste örnek amaçlı yazılmış, kullanılmıyor ama yukarıdaki sözlükle aynı kategorileri içeriyor
["telefon", "bilgisayar", "elektronik"]

# /products/ veya /products/index adresine istek gelince çalışacak olan fonksiyon
def index(request):
    list_items = ""  # Liste elemanlarını HTML olarak tutacak değişken
    category_list = list(data.keys())  # ['telefon', 'bilgisayar', 'elektronik'] gibi liste haline getiriyoruz

    for category in category_list:
        # 'products_by_category' URL'sinin dinamik yolunu 'category' ile oluşturuyoruz
        redirect_path = reverse('products_by_category', args=[category])
        list_items += f"<li><a href=\"{redirect_path}\">{category}</a></li>"  # HTML link olarak her kategoriyi ekle

    html = f"<ul>{list_items}</ul>"  # Tüm liste elemanlarını bir <ul> içinde topla
    return render(request, 'myapp/index.html')  # Tarayıcıya HTML döndür

# /products/<int:category_id> şeklinde gelen istekte çalışır
# Sayısal ID'ye göre doğru kategoriye yönlendirir
def getproductByCategoryId(request, category_id):
    category_list = list(data.keys())  # ['telefon', 'bilgisayar', 'elektronik']

    # Eğer ID, geçerli kategoriler arasında değilse hata döndür
    if category_id > len(category_list) or category_id < 1:
        return HttpResponseNotFound("yanlış kategori seçimi yaptınız")  # Geçersiz ID girildiyse hata döner

    category_name = category_list[category_id - 1]  # ID ile doğru kategori ismi eşleştirilir (1-indexli gibi çalışıyor)
    # İlgili kategoriye ait URL'yi 'category_name' ile oluşturuyoruz
    redirect_path = reverse('products_by_category', args=[category_name])
    return redirect(redirect_path)  # Kullanıcıyı o URL'ye yönlendir

# /products/<str:category> şeklinde gelen istekte çalışır
# Kategori adına göre açıklamayı döndürür
def getproductByCategory(request, category):
    try:
        # Kategori adıyla açıklamayı sözlükten alıyoruz
        category_text = data[category]
        # Kategori ve açıklama ile HTML döndürüyoruz
        return render(request, "myapp/products.html", {"category": category, "category_text": category_text})

    except:
        # Eğer kategori bulunamazsa, 404 hata mesajı döndür
        return HttpResponseNotFound(f"<h1>yanlış kategori seçimi</h1>")
