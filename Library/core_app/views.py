from django.shortcuts import render

# Create your views here.
def core_render(requests):
    return render(request=requests, template_name="core.html")