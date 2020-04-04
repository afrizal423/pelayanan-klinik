from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from pegawaiadmin.decorators import pegawaiadmin_area

# Create your views here.
@pegawaiadmin_area
def index(request):
    return HttpResponse("You are logged in ! Pegawai ADmin Area!!")
