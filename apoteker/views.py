from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from apoteker.decorators import apoteker_area
from .models import Obat, PemesananObat
from apoteker.forms import ObatForm
from dokter.models import RekamMedis
from datetime import date
from pegawaiadmin.models import Antrian


# Create your views here.
@apoteker_area
def index(request):
    print(request.session['username'])
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai']
    }
    return render(request, 'hal_admin/apoteker/home.html', data)

@apoteker_area
def index_obat(request):
    hasil = Obat.objects.all()
    # print(hasil) ## untuk lihat hasilnya silahkan liat diterminal
    data = {
        'data':hasil,
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
    }   
    return render(request, 'hal_admin/apoteker/index.html',data)
    # return HttpResponse("You are logged in ! Apoteker area")

@apoteker_area
def tambah_obat(request):
    form = ObatForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # print("suksessssssssssssssssssssss")
            return redirect("/apoteker/dtobat")
        pass
    data = {
        'form':ObatForm(),
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
    }   
    return render(request, 'hal_admin/apoteker/tambahobat.html',data)

@apoteker_area
def edit_obat(request, id):
    obj = get_object_or_404(Obat, id = id) 
  
    # pass the object as instance in form 
    form = ObatForm(request.POST or None, instance = obj)
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return redirect("/apoteker/dtobat/")  
    data = {
        'data':obj,
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
    }   
    return render(request, 'hal_admin/apoteker/editobat.html',data)

@apoteker_area
def hapus_obat(request, id):
    dt = Obat.objects.get(id=id)
    dt.delete()
    return redirect("/apoteker/dtobat/")

@apoteker_area
def antrian(request):
    hasil = RekamMedis.objects.all().select_related('idpendaftaran').filter(created_on__contains=date.today(), idantrian__statusdokter="selesai", idantrian__statusapoteker="belum").order_by('created_on')
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': hasil
    }
    # print(hasil.get().idpendaftaran.norm.norm)
    # print(hasil.get().idantrian.noantrian)
    return render(request, 'hal_admin/apoteker/antrian.html', data)

@apoteker_area
def history(request):
    hasil = RekamMedis.objects.all().select_related('idpendaftaran').filter(idantrian__statusdokter="selesai", idantrian__statusapoteker="selesai").order_by('created_on')
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': hasil
    }
    # print(hasil.get().idpendaftaran.norm.norm)
    # print(hasil.get().idantrian.noantrian)
    return render(request, 'hal_admin/apoteker/history.html', data)

@apoteker_area
def pesanan_obat(request, id):
    obj = get_object_or_404(RekamMedis, id = id)
    pesanobat = PemesananObat.objects.all().filter(created_on__contains=date.today(), idrm=id) 
    ant = get_object_or_404(Antrian, idpendaftaran = id) 
    if request.method == 'POST':
        obj.diagnosa = request.POST['diagnosa']
        obj.save()
        ant.statusapoteker = request.POST['statusapoteker']
        ant.save()
        print(request.POST['statusapoteker'])
        return redirect('/apoteker/antrianobat/')
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': obj,
        'pesanan': pesanobat
    }
    return render(request, 'hal_admin/apoteker/pesanan.html', data)

