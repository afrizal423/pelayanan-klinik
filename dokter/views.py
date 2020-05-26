from django.shortcuts import render, redirect ,get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from dokter.decorators import dokter_area
from datetime import date
from dokter.models import RekamMedis
from apoteker.models import Obat
from django.db.models import Q

# Create your views here.
@dokter_area
def index(request):
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai']
    }
    return render(request, 'hal_admin/dokter/home.html', data)

@dokter_area
def antrian(request):
    hasil = RekamMedis.objects.all().select_related('idpendaftaran').filter(created_on__contains=date.today(), idantrian__is_dokterumum=True, idantrian__statusdokter="belum").order_by('created_on')
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': hasil
    }
    # print(hasil.get().idpendaftaran.norm.norm)
    # print(hasil.get().idantrian.noantrian)
    return render(request, 'hal_admin/dokter/antrian.html', data)

@dokter_area
def periksa(request , id):
    obj = get_object_or_404(RekamMedis, id = id) 
    print(obj.idpendaftaran.norm.norm)

    item_id = str(1)
    cart_items = request.session


    # Create an empty cart object if it does not exist yet 
    if not cart_items.has_key("cart"):
        cart_items["cart"] = {}

    print(cart_items["cart"])

    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': obj
    }
    return render(request, 'hal_admin/dokter/periksa.html', data)

def cariobat(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:            
            results = Obat.objects.filter(  
            	Q( nama_obat__contains = q ) )          
            # print(results)
            return render(request,'hal_admin/dokter/cariobat.html', {'results': results})

