"""
Dummy docstring
"""
# from django.http import HttpResponse
from django.shortcuts import render

from blog.models import BlogPost
from .forms import ContactForm


def home_page(request):
    """Dummy docstring"""
    my_title = "Welcome to Django Blog"
    qs = BlogPost.objects.all()[:5]
    context = {"title": my_title, "blog_list": qs}
    return render(request, "home.html", context)


def about_page(request):
    """Dummy docstring"""
    return render(request, "about.html", {"title": "About Us"})


def contact_page(request):
    """Dummy docstring"""
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": "Contact Us", "form": form}
    return render(request, "form.html", context)
