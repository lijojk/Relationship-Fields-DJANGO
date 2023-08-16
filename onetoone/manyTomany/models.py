# many to many db relation
# track the enrollment of students in various courses.
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tag_picture = models.ImageField(upload_to='tag_img_stdnt/')
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    enrollment_date = models.DateField(auto_now_add=True)
    courses = models.ManyToManyField('Course', related_name='enrolled_students', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Current date and time when created
    updated_at = models.DateTimeField(auto_now=True)  # Current date and time when updated

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(Student, related_name='courses_enrolled', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Current date and time when created
    updated_at = models.DateTimeField(auto_now=True)  # Current date and time when updated

    def __str__(self):
        return self.title
