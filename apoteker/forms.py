from django import forms  
from apoteker.models import Obat

class ObatForm(forms.ModelForm):  
    class Meta:  
        model = Obat  
        fields = "__all__"  