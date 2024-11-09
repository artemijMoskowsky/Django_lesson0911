from django.shortcuts import render

# Create your views here.
def show_ukr_au(request):
    return render(request=request, template_name='autor_app/ukr_au.html') 


def show_world_au(request):
    return render(request=request, template_name='autor_app/world_au.html')

