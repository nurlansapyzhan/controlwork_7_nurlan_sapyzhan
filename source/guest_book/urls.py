from django.urls import path

from guest_book.views.base import guests_view
from guest_book.views.guests import add_guest_view, delete_guest, confirm_delete, edit_guest

urlpatterns = [
    path('', guests_view, name='index'),
    path('guest/add', add_guest_view, name='add_guest'),
    path('guest/<int:pk>/delete', delete_guest, name='guest_delete'),
    path('guest/<int:pk>/confirm_delete', confirm_delete, name='confirm_delete'),
    path('guest/<int:pk>/edit', edit_guest, name='guest_edit'),
]
