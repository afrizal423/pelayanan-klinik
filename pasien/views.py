from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from pegawaiadmin.decorators import pegawaiadmin_area
from random import *
from pasien.models import Pasien
from pasien.forms import PasienForm
import datetime
# Create your views here.
@pegawaiadmin_area
def index(request):
    print(request.session['username'])
    hasil = Pasien.objects.all().order_by('-created_on')
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'data': hasil
    }
    return render(request, 'hal_admin/pasien/index.html', data)

@pegawaiadmin_area
def tambah_pasien(request):
    form = PasienForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            # ps = Pasien()
            # ps.namapasien = request.POST['namapasien']
            # ps.save()
            # print(request.POST['namapasien'])
            form.save()
            # print("suksessssssssssssssssssssss")
            return redirect("/pegawaiadmin/dtpasien/")
        pass
    tgl = datetime.datetime.now().strftime('%Y%m%d%H%M')
    norm = str(randint(1,100)) + tgl 
    # print(norm)
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
        'norm': norm,
        'form':PasienForm(),
    }
    return render(request, 'hal_admin/pasien/tambahpasien.html', data)

@pegawaiadmin_area
def edit_pasien(request, id):
    obj = get_object_or_404(Pasien, id = id) 
  
    # pass the object as instance in form 
    form = PasienForm(request.POST or None, instance = obj)
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return redirect("/pegawaiadmin/dtpasien/")  
    data = {
        'data':obj,
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai'],
    }   
    return render(request, 'hal_admin/pasien/editpasien.html',data)

@pegawaiadmin_area
def hapus_pasien(request, id):
    dt = Pasien.objects.get(id=id)
    dt.delete()
    return redirect("/pegawaiadmin/dtpasien/")
