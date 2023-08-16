# many to many db relation
import base64
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Course, Student


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'instructor', 'start_date', 'end_date', 'formatted_students',)
    list_filter = ('title', 'instructor', 'start_date', 'end_date')
    search_fields = ('title', 'instructor')

    def formatted_students(self, obj):
        return ", ".join([student.first_name for student in obj.students.all()])

    formatted_students.short_description = 'Enrolled Students'


class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_tag_pic', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address',
                    'enrollment_date', 'formatted_courses')
    list_filter = ('first_name', 'phone_number')
    search_fields = ('first_name', 'phone_number')

    def formatted_courses(self, obj):
        return ", ".join([course.title for course in obj.courses.all()])

    formatted_courses.short_description = 'Enrolled Courses'

    def stu_tag_pic(self, obj):
        if obj.tag_picture:
            # Assuming `image_field` is an instance of ImageFieldFile
            image_field = obj.tag_picture
            # Read the image file content and encode it as bytes
            image_bytes = base64.b64encode(image_field.read()).decode('utf-8')
            return mark_safe(f'<img src="data:image/jpeg;base64,{image_bytes}" width="100" />')
        return "No Image"

    stu_tag_pic.short_description = 'Profile Image'  # Column header text


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
