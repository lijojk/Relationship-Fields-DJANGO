import base64

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import UserProfile


# Register the UserProfile model to the admin interface
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'contact_number', 'pro_image')
    list_filter = ('user', 'contact_number')
    search_fields = ('user', 'contact_number')
    list_per_page = 10

    def pro_image(self, obj):
        if obj.profile_picture:
            # Assuming `image_field` is an instance of ImageFieldFile
            image_field = obj.profile_picture
            # Read the image file content and encode it as bytes
            image_bytes = base64.b64encode(image_field.read()).decode('utf-8')
            return mark_safe(f'<img src="data:image/jpeg;base64,{image_bytes}" width="100" />')
        return "No Image"

    pro_image.short_description = 'Profile Photo'  # Column header text

    def is_available(self, obj):
        return obj.available

    is_available.boolean = True
    is_available.short_description = 'Available'
