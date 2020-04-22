from django import forms  
from pasien.models import Pasien

class PasienForm(forms.ModelForm):  
    class Meta:  
        model = Pasien  
        fields = "__all__"  