from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from dokter.decorators import dokter_area

# Create your views here.
@dokter_area
def index(request):
    return HttpResponse("You are logged in ! Dokter area")
