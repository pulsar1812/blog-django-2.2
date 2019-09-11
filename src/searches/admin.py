'''
Registering admin for Search
'''
from django.contrib import admin

from .models import SearchQuery

admin.site.register(SearchQuery)
