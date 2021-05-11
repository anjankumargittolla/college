from django.contrib import admin
from .models import StudentApplication,Student,Staff
# Register your models here.
admin.site.register(StudentApplication)
admin.site.register(Student)
admin.site.register(Staff)