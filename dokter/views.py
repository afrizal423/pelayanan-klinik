from django.shortcuts import render, redirect ,get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from dokter.decorators import dokter_area
from datetime import date
from dokter.models import RekamMedis, Temp_Obat
from apoteker.models import Obat, PemesananObat
from pegawaiadmin.models import Antrian
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
    if request.session['jenis_akun'] == "dokter":
        hasil = RekamMedis.objects.all().select_related('idpendaftaran').filter(created_on__contains=date.today(), idantrian__is_dokterumum=True, idantrian__statusdokter="belum").order_by('created_on')
    elif request.session['jenis_akun'] == "dokter_gigi":
        hasil = RekamMedis.objects.all().select_related('idpendaftaran').filter(created_on__contains=date.today(), idantrian__is_doktergigi=True, idantrian__statusdokter="belum").order_by('created_on')
    
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': hasil
    }
    # print(hasil.get().idpendaftaran.norm.norm)
    # print(hasil.get().idantrian.noantrian)
    return render(request, 'hal_admin/dokter/antrian.html', data)

@dokter_area
def history(request):
    if request.session['jenis_akun'] == "dokter":
        hasil = RekamMedis.objects.all().select_related('idpendaftaran').filter(idantrian__is_dokterumum=True, idantrian__statusdokter="selesai").order_by('created_on')
    elif request.session['jenis_akun'] == "dokter_gigi":
        hasil = RekamMedis.objects.all().select_related('idpendaftaran').filter(idantrian__is_doktergigi=True, idantrian__statusdokter="selesai").order_by('created_on')
    
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': hasil
    }
    # print(hasil.get().idpendaftaran.norm.norm)
    # print(hasil.get().idantrian.noantrian)
    return render(request, 'hal_admin/dokter/history.html', data)


@dokter_area
def periksa(request , id):
    obj = get_object_or_404(RekamMedis, id = id) 
    print(obj.idpendaftaran.norm.norm)
    idpasien = "periksapasien/"+ str(id)
    pesanobat = Temp_Obat.objects.all().filter(created_on__contains=date.today(), url__contains=idpasien)
    if request.method == 'POST':
        tempobt = Temp_Obat.objects.all().filter(created_on__contains=date.today(),url__contains=request.META.get('HTTP_REFERER')) 
        ant = get_object_or_404(Antrian, id = id)
          
        for obt in tempobt:
            psnobat = PemesananObat()
            psnobat.idobat = Obat.objects.get(id = obt.id_obat)
            psnobat.jumlah_obat = obt.jumlah_obat
            psnobat.subtotal_obat = obt.jumlah_obat * obt.harga_obat
            psnobat.idrm = RekamMedis.objects.get(id = id)
            psnobat.save()
            obat = get_object_or_404(Obat, id = obt.id_obat)
            obat.stok_obat = obat.stok_obat - obt.jumlah_obat
            obat.save()
            
        tempobt.delete()
        ant.statusdokter = "selesai"
           
        ant.save()

        obj.diagnosa = request.POST['diagnosa']
        obj.save()
        return redirect('/dokter/antrianpasien/')
        # print(request.META.get('HTTP_REFERER'))

    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': obj,
        'pesanan': pesanobat
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

def tambahobat(request, id):
    results = Obat.objects.filter(id=id)
    print(results.get().nama_obat)
    print(request.META.get('HTTP_REFERER'))
    temp = Temp_Obat()
    temp.id_obat = id
    temp.nama_obat = results.get().nama_obat
    temp.jumlah_obat = 1
    temp.harga_obat = results.get().harga_obat
    temp.url = request.META.get('HTTP_REFERER')
    temp.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # item_id = str(1)
    # cart_items = request.session


    # # Create an empty cart object if it does not exist yet 
    # if not cart_items.has_key("cart_obat"):
    #     cart_items["cart_obat"] = {}

    # # print(request.META.get('HTTP_REFERER'))

    # product_data = {
    # 	'quantity': 2,
    # }

    # cart_items["cart_obat"][1] = product_data
    # cart_items.modified = True
    # print(cart_items.items())

def hapusobat(request, id):
    dt = Temp_Obat.objects.get(id=id)
    dt.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

