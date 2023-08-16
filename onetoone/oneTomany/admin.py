import base64
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Author, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'genre', 'book_cover_image')
    list_filter = ('author', 'genre', 'publication_date')
    search_fields = ('title', 'author', 'publication_date')

    def book_cover_image(self, obj):
        if obj.cover_image:
            # Assuming `image_field` is an instance of ImageFieldFile
            image_field = obj.cover_image
            # Read the image file content and encode it as bytes
            image_bytes = base64.b64encode(image_field.read()).decode('utf-8')
            return mark_safe(f'<img src="data:image/jpeg;base64,{image_bytes}" width="100" />')
        return "No Image"

    book_cover_image.short_description = 'Cover Image'  # Column header text


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'contact_number', 'author_image')
    list_filter = ('name', 'contact_number')
    search_fields = ('name', 'contact_number')

    def author_image(self, obj):
        if obj.profile_picture:
            # Assuming `image_field` is an instance of ImageFieldFile
            image_field = obj.profile_picture
            # Read the image file content and encode it as bytes
            image_bytes = base64.b64encode(image_field.read()).decode('utf-8')
            return mark_safe(f'<img src="data:image/jpeg;base64,{image_bytes}" width="100" />')
        return "No Image"

    author_image.short_description = 'Profile Image'  # Column header text


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
