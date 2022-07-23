from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Movie
from django.shortcuts import get_object_or_404



# Create your views here.
def home(request):
    searchKey = request.GET.get('search')
    if searchKey:
        movies = Movie.objects.filter(title__icontains = searchKey)

    else:

        movies = Movie.objects.all()
    return render(request, 'home.html', {'name': searchKey, "movies":movies})
    #return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return render(request, 'about.html')
   # return HttpResponse('<h2>About Us</h2>')


def signup(request):
    email = request.GET.get('mail')
    return render(request, 'signup.html', {'email':email})

def details(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'details.html', {'movie':movie})