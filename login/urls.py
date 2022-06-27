from unicodedata import name
from django.urls import path
from .views import home, All_Book

app_name = 'login'

urlpatterns = [
    path('', home, name='home'),
    path('all_book/', All_Book, name='all_book')
]