from django.shortcuts import render

# Create your views here.
def world_books(request):
    return render(request, "book_app/world_lit.html")

def ukr_books(request):
    return render(request, "book_app/ukr_lit.html")