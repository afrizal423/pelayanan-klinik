from django import forms  
from pegawaiadmin.models import Antrian, Pendaftaran

class AntrianForm(forms.ModelForm):  
    class Meta:  
        model = Antrian  
        fields = "__all__"  

class PendaftaranForm(forms.ModelForm):  
    class Meta:  
        model = Pendaftaran  
        fields = "__all__"  