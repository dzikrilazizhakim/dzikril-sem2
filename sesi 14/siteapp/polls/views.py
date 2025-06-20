from django.http import request, HttpResponse

def  alamat_view(request):
    return HttpResponse( "Alamat: Jl. Pangsor Kebin Jeruk Palabuhanratu")
def  telepon_view(request):
    return HttpResponse("Telepon: +628-5880-4064-02")