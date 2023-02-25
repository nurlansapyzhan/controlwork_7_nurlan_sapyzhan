from django.contrib import admin

from guest_book.models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'text', 'created_date', 'updated_date', 'status')
    list_filter = ('author', 'email', 'status')
    search_fields = ('author', 'email', 'status')
    fields = ('author', 'email', 'text', 'created_date', 'updated_date', 'status')
    readonly_fields = ('id', 'created_date', 'updated_date')


admin.site.register(Book, BookAdmin)
