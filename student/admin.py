from django.contrib import admin

from student.models import City, Course, Student

# Register your models here.
admin.site.register(City)
admin.site.register(Course)
admin.site.register(Student)