from django.shortcuts import render, redirect
from django.urls import reverse 
from django.http import HttpResponse
from control_talleres_padres import models
from control_talleres_padres import forms

# Create your views here.
def prueba_html(request):
    contexto = {}
    http_response = render (
        request=request,
        template_name='index.html',
        context=contexto,
    )
    return http_response

def talleres(request):
    if request.method == "POST":
        formulario = forms.tallerFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre=data['nombre']
            generacion=data['generacion']
            talleres =  models.Talleres(nombre=nombre, generacion=generacion)
            talleres.save()
        url_exitosa = reverse('Inicio')
        return redirect(url_exitosa)
    else: #GET
        formulario = forms.tallerFormulario()
        http_response = render(
            request=request,
            template_name='talleres.html',
            context={'formulario': formulario}
            )
        return http_response 
def prospectos(request):
    if request.method == "POST":
        formulario2 = forms.prospectoFormulario(request.POST)
        if formulario2.is_valid():
            data2 = formulario2.cleaned_data
            apellido=data2['apellido']
            nombre=data2['nombre']
            email=data2['email']
            telefono=data2['telefono']
            prospectos =  models.Prospecto(apellido=apellido, nombre=nombre, email=email, telefono=telefono)
            prospectos.save()
        url_exitosa = reverse('Inicio')
        return redirect(url_exitosa)
    else: #GET
        formulario = forms.prospectoFormulario()
        http_response = render(
            request=request,
            template_name='prospectos.html',
            context={'formulario': formulario}
            )
        return http_response 
def Inscritos(request):
    if request.method == "POST":
        formulario = forms.clienteFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            apellido=data['apellido']
            nombre=data['nombre']
            email=data['email']
            objetivo=data['objetivo']
            inscritos =  models.Inscrito(apellido=apellido, nombre=nombre, email=email, objetivo=objetivo)
            inscritos.save()
        url_exitosa = reverse('Inicio')
        return redirect(url_exitosa)
    else: #GET
        formulario = forms.clienteFormulario()
        http_response = render(
            request=request,
            template_name='inscritos.html',
            context={'formulario': formulario}
            )
        return http_response 
def buscar_prospectos(request):
    return render(request, template_name='busqueda_prospectos.html')

def buscar(request):
    if request.method == "POST":
        data=request.POST
        busqueda = data["busqueda"]
        prospectos = models.Prospecto.objects.filter(nombre__contains=busqueda)
        contexto = {
            "prospectos": prospectos,
            }
        return render(request, template_name='resultadosBusqueda.html',context=contexto,)
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
    

