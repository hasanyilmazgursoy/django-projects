from django.http import HttpResponse  # HTML veya düz metin cevap döndürmek için

# /products/ veya /products/index çağrıldığında çalışan fonksiyon
def index(request):
    return HttpResponse("index")  # Basit bir yanıt döner: "index"

# /products/details çağrıldığında çalışan fonksiyon
def details(request):
    return HttpResponse("details")

# /products/list çağrıldığında çalışan fonksiyon
def list(request):
    return HttpResponse("list")

# /products/<category> çağrıldığında çalışan dinamik fonksiyon
def getproductByCategory(request, category):  # URL'den gelen kategori bilgisi alınır
    category_text = None  # Başlangıçta boş tanımlanır

    # Eğer kategori bilgisayar veya telefon ise özel mesaj döner
    if category == 'bilgisayar':
        category_text = "bilgisayar kategorindeki pcler"
    elif category == 'telefon':
        category_text = "telefon kategorindeki telefonlar"
    else:
        category_text = "bilinmeyen kategori"  # Tanımsız kategoriler için varsayılan mesaj

    return HttpResponse(category_text)  # Kategoriye göre uygun mesajı döndürür
