from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from guest_book.forms import BookForm
from guest_book.models import Book


def add_guest_view(request: WSGIRequest):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'add_guest.html', context={'form': form})
    form = BookForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'add_guest.html', context={'form': form})
    else:
        Book.objects.create(**form.cleaned_data)
        return redirect('index')


def delete_guest(request: WSGIRequest, pk):
    guest = get_object_or_404(Book, pk=pk)
    return render(request, 'guest_delete_confirm.html', context={'guest': guest})


def confirm_delete(request: WSGIRequest, pk):
    guest = get_object_or_404(Book, pk=pk)
    guest.delete()
    return redirect('index')