from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from pegawaiadmin.decorators import pegawaiadmin_area
from pegawaiadmin.models import Pendaftaran, Antrian, BiayaPemeriksaan
from dokter.models import RekamMedis
from datetime import date
from pasien.models import Pasien
from pegawaiadmin.forms import AntrianForm, PendaftaranForm
from django.utils import timezone
import datetime
from apoteker.models import PemesananObat

# Create your views here.
@pegawaiadmin_area
def index(request):
    print(request.session['username'])
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai']
    }
    return render(request, 'hal_admin/pegawaiadmin/home.html', data)

@pegawaiadmin_area
def antrian(request):
    hasil = Pendaftaran.objects.all().select_related('norm','antrian').filter(tglantrian__contains=date.today()).order_by('created_on')
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': hasil
    }
    print(hasil.query)
    return render(request, 'hal_admin/pegawaiadmin/antrian.html', data)

@pegawaiadmin_area
def tbantrian(request):
    hasil = Pasien.objects.all().order_by('-created_on')
    formdaftar = PendaftaranForm(request.POST or None, request.FILES or None)
    df = Pendaftaran.objects.all().select_related('norm','antrian').filter(tglantrian__contains=date.today()).order_by('-created_on')

    # print(isgigi.query)
    if request.method == 'POST':
        # if formdaftar.is_valid():
            # formdaftar.save()
        daftar = Pendaftaran()
        # daftar.norm=request.POST['norm rekammedik']
        daftar.norm=Pasien.objects.get(id=request.POST['norm rekammedik'])
        daftar.tujuanpoli=request.POST['tujuanpoli']
        daftar.gejalaawal=request.POST['gejalaawal']
        daftar.tglantrian = datetime.datetime.now()
        # ant = Antrian()
        if df.count() == 0 :
            print("Kosong")
            counter = 1
            daftar.save()
            ant = Antrian(idpendaftaran=daftar, noantrian=counter)

            # ant.idpendaftaran=daftar
            # ant.noantrian=counter
            if  daftar.tujuanpoli == "Poli Umum":
                ant.is_dokterumum=True
                ant.statusdokter="belum"
                ant.statusapoteker="belum"
            elif daftar.tujuanpoli == "Poli Gigi":
                ant.is_doktergigi=True
                ant.statusdokter="belum"
                ant.statusapoteker="belum"
            ant.save()
            rm = RekamMedis(idpendaftaran=daftar, idantrian=ant)
            rm.save()
        else:
            daftar.save()
            # nolama = Antrian.objects.all().filter(created_on__contains=date.today()).order_by('-created_on')
            if  daftar.tujuanpoli == "Poli Umum":
                nolama = Antrian.objects.all().filter(created_on__contains=date.today(),is_dokterumum=True).order_by('-created_on')
            elif daftar.tujuanpoli == "Poli Gigi":
                nolama = Antrian.objects.all().filter(created_on__contains=date.today(),is_doktergigi=True).order_by('-created_on')
            print(nolama.first())
            ant = Antrian(idpendaftaran=daftar)
            if  daftar.tujuanpoli == "Poli Umum" :
                if nolama.count() == 0:
                    counter=1
                elif nolama.count() > 0:
                    counter = nolama.first().noantrian + 1
                ant.noantrian=counter
                ant.is_dokterumum=True
                ant.statusdokter="belum"
                ant.statusapoteker="belum"
            elif daftar.tujuanpoli == "Poli Gigi" :
                if nolama.count() == 0:
                    counter=1
                elif nolama.count() > 0:
                    counter = nolama.first().noantrian + 1
                ant.noantrian=counter
                ant.is_doktergigi=True
                ant.statusdokter="belum"
                ant.statusapoteker="belum"
            ant.save()
            rm = RekamMedis(idpendaftaran=daftar, idantrian=ant)
            rm.save()
        # print(daftar.tujuanpoli)
        return redirect("/pegawaiadmin/antrian/")

    # print("gagal formnya")
        
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data' : hasil
    }
    return render(request, 'hal_admin/pegawaiadmin/tambahantrian.html', data)

@pegawaiadmin_area
def pembayaran(request):
    hasil = RekamMedis.objects.all().select_related('idpendaftaran', 'idantrian').filter(created_on__contains=date.today(),idantrian__statusdokter="selesai").order_by('created_on')
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': hasil
    }
    # print(hasil.get().idpendaftaran.norm.norm)
    # print(hasil.get().idantrian.noantrian)
    return render(request, 'hal_admin/pegawaiadmin/listpembayaran.html', data)

@pegawaiadmin_area
def detailbayar(request , id):
    obj = get_object_or_404(RekamMedis, id = id)
    pesanobat = PemesananObat.objects.all().filter(created_on__contains=date.today(), idrm=id)
    biayadokter = BiayaPemeriksaan.objects.all()[:1].get()
    totalobat=0
    for i in pesanobat:
        totalobat += i.subtotal_obat 
        # print(i.subtotal_obat) 
    print(totalobat)
    harusbayar = biayadokter.biaya_pemeriksaan+totalobat
   

    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': obj,
        'pesanan': pesanobat,
        'totalobat': totalobat,
        'biayadokter': biayadokter.biaya_pemeriksaan,
        'total' : harusbayar
    }
    return render(request, 'hal_admin/pegawaiadmin/pesanan.html', data)