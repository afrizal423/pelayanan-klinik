from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from dokter.decorators import dokter_area
from datetime import date
from dokter.models import RekamMedis

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
    hasil = RekamMedis.objects.all().select_related('idpendaftaran').filter(created_on__contains=date.today()).order_by('created_on')
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': hasil
    }
    # print(hasil.get().idpendaftaran.norm.norm)
    # print(hasil.get().idantrian.noantrian)
    return render(request, 'hal_admin/dokter/antrian.html', data)
