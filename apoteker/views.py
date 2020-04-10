from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from apoteker.decorators import apoteker_area
from .models import Obat
from apoteker.forms import ObatForm

# Create your views here.
@apoteker_area
def index(request):
    hasil = Obat.objects.all()
    # print(hasil) ## untuk lihat hasilnya silahkan liat diterminal
    data = {
        'data':hasil,
    }   
    return render(request, 'apoteker/index.html',data)
    # return HttpResponse("You are logged in ! Apoteker area")

@apoteker_area
def tambah_obat(request):
    form = ObatForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # print("suksessssssssssssssssssssss")
            return redirect("/apoteker/index")
        pass
    data = {
        'form':ObatForm(),
    }   
    return render(request, 'apoteker/tambahobat.html',data)

@apoteker_area
def edit_obat(request, id):
    obj = get_object_or_404(Obat, id = id) 
  
    # pass the object as instance in form 
    form = ObatForm(request.POST or None, instance = obj)
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return redirect("/apoteker/index/")  
    data = {
        'form':form,
    }   
    return render(request, 'apoteker/editobat.html',data)

@apoteker_area
def hapus_obat(request, id):
    dt = Obat.objects.get(id=id)
    dt.delete()
    return redirect("/apoteker/index/")
