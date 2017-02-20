from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')
def turtle(request):
    context = {
        "imagesrc": "first_app/css/images/tmnt.png"
    }
    return render(request, 'first_app/ninjas.html', context)

def ninjas(request, ninja_color):
    context = {
        "ninja_color": ninja_color,
        "imagesrc": ninja_color

    }
    if ninja_color == "blue":
        context['imagesrc'] = "first_app/css/images/leonardo.jpg"
    if ninja_color == "orange":
        context['imagesrc'] = "first_app/css/images/michelangelo.jpg"
    if ninja_color == "red":
        context['imagesrc'] = "first_app/css/images/raphael.jpg"
    if ninja_color == "purple":
        context['imagesrc'] = "first_app/css/images/donatello.jpg"
    else:
        context['imagesrc'] = "first_app/css/images/notapril.jpg"
    return render(request, 'first_app/ninjas.html', context)
