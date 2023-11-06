from django.shortcuts import render

# Create your views here.
def prueba_html(request):
    contexto = {}
    http_response = render (
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response