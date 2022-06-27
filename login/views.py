from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

# Create your views here.


def home(request):
    return HttpResponse('hello world')


def All_Book(request):
    all_book = Book.objects.all()
    context={
        'all_book':all_book,
    }
    return render(request, 'login/all_book.html', context)
