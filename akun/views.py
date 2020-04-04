from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import Akun, DataPegawai
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    akun = Akun.objects.get(akun=user.id)
                    login(request, user)

                    request.session['pegawai_id'] = akun.pegawai.id
                    request.session['jenis_akun'] = akun.jenis_akun
                    request.session['username'] = request.POST['username']
                except:
                    messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data karyawan, silahkan hubungi administrator')
                
                if request.session['jenis_akun'] == "dokter":
                    return redirect('/dokter/index') # sudah login ini
                elif request.session['jenis_akun'] == "pegawai_admin": 
                    return redirect('/pegawaiadmin/index') # sudah login ini
                elif request.session['jenis_akun'] == "pegawai_apotek": 
                    return redirect('/apoteker/index') # sudah login ini

                # return redirect('/akun') # sudah login ini
            else:   
                messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

    return render(request, 'login.html')
# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return HttpResponse("Berhasil logout !")