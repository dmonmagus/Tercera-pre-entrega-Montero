from django import forms

class tallerFormulario(forms.Form):
    nombre = forms.CharField (required=True, max_length=64)
    generacion = forms.IntegerField (required=True, max_value=100)
class prospectoFormulario(forms.Form):
    apellido = forms.CharField(max_length=256)
    nombre = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256)
    telefono = forms.CharField(max_length=20)

class clienteFormulario(forms.Form):
    apellido = forms.CharField(max_length=256)
    nombre = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256)
    objetivo = forms.CharField(max_length=256)
