from django.urls import path

from guest_book.views.base import guests_view

urlpatterns = [
    path('', guests_view, name='index'),
]