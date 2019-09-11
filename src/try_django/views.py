'''
Defining views for home, about, and contact pages
'''
# from django.http import HttpResponse
from django.shortcuts import render

from blog.models import BlogPost
from .forms import ContactForm


def home_page(request):
    '''Home page view'''
    my_title = 'Welcome to Django Blog'
    qs = BlogPost.objects.all()[:5]
    context = {'title': my_title, 'blog_list': qs}
    return render(request, 'home.html', context)


def about_page(request):
    '''About page view'''
    return render(request, 'about.html', {'title': 'About Us'})


def contact_page(request):
    '''Contact page view'''
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {'title': 'Contact Us', 'form': form}
    return render(request, 'form.html', context)
