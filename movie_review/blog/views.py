from unicodedata import name
from django.shortcuts import render
from .models import blog
from django.shortcuts import get_object_or_404


# Create your views here.
def index(response):
    content = blog.objects.all()
    return render(response, 'index.html', {"content": content})


def blogdetails(response, id):
    contents = get_object_or_404(blog, pk=id)
    return render(response, 'blog_details.html', {"content": contents})
