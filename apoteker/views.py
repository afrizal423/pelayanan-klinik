from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from apoteker.decorators import apoteker_area

# Create your views here.
@apoteker_area
def index(request):
    return HttpResponse("You are logged in ! Apoteker area")
