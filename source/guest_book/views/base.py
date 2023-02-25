from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from guest_book.models import Book


def guests_view(request: WSGIRequest):
    guest_list = Book.objects.exclude(status='blocked').order_by('-created_date')
    return render(request, 'index.html', context={'guest_list': guest_list})
