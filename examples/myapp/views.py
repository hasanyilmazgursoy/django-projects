from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound  # HTML veya düz metin cevap döndürmek için
from django.shortcuts import redirect  # Kullanıcıyı başka bir sayfaya yönlendirmek için

# Kategorilere ait verilerin tanımlandığı sözlük
data = {
    "telefon": "telefon kategorisindeki ürünler",  # Telefon kategorisindeki ürün açıklaması
    "bilgisayar": "bilgisayar kategorisindeki ürünler",  # Bilgisayar kategorisindeki ürün açıklaması
    "elektronik": "elektronik kategorisindeki ürünler",  # Elektronik kategorisindeki ürün açıklaması
}

# Kategoriler listesi (şu anda kullanılmıyor, veriler `data` sözlüğünden alınıyor)
["telefon", "bilgisayar", "elektronik"]  # Kategoriler listesi

# /products/ veya /products/index çağrıldığında çalışan fonksiyon
def index(request):
    return HttpResponse("index")  # Basit bir yanıt döner: "index"

# /products/details çağrıldığında çalışan fonksiyon
def details(request):
    return HttpResponse("details")  # Basit bir yanıt döner: "details"

# Kategori ID'sine göre yönlendirme yapan fonksiyon
def getproductByCategoryId(request, category_id):
    category_list = list(data.keys())  # data sözlüğündeki anahtarları (kategori isimlerini) bir listeye dönüştür
    if category_id > len(category_list):  # Eğer kategori numarası geçerli değilse
        return HttpResponseNotFound("yanlış kategori seçimi yaptınız")  # 404 hata mesajı döndür
    redirect_text = category_list[category_id-1]  # Kategori sırasına göre doğru kategori ismini al
    return redirect("/products/" + redirect_text)  # Kullanıcıyı doğru kategoriye yönlendir

# /products/<category> şeklinde dinamik kategori URL'siyle çağrıldığında çalışan fonksiyon
def getproductByCategory(request, category):  # URL'den gelen kategori bilgisi alınır
    try:
        category_text = data[category]  # Kategori ismini data sözlüğünden al
        return HttpResponse(category_text)  # Kategoriye göre uygun açıklama mesajını döndür
    except:  # Eğer kategori bulunamazsa
        return HttpResponseNotFound("yanlış kategori seçimi yaptınız")  # 404 hata mesajı döndür
