from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from pegawaiadmin.decorators import pegawaiadmin_area

# Create your views here.
@pegawaiadmin_area
def index(request):
    print(request.session['username'])
    data = {
        'sessionnya' : request.session['jenis_akun'],
        'namaakun' : request.session['namapegawai']
    }
    return render(request, 'admin/base.html', data)
