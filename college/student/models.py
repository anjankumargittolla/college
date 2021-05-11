import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class StudentApplication(models.Model):
    student_name = models.CharField(max_length=25)
    student_email = models.EmailField(unique=True)
    ssc_marks = models.IntegerField()
    inter_marks = models.IntegerField()
    is_approved = models.BooleanField(default=False)


class Student(models.Model):
    DEPARTMENT_CHOICES = (
        ('CE', 'Civil Engineering'),
        ('CSE', 'Computer Science Engineering'),
        ('ECE', 'Electronics Communtication Engineering'),
        ('EEE', 'Electronics Electrical Engineering'),
        ('ME', 'Mechanical Engineering')
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    student = models.OneToOneField(User, related_name="student_info", on_delete=models.CASCADE)
    student_app = models.OneToOneField(StudentApplication, on_delete=models.CASCADE)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES, default=None)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    mobile = models.IntegerField()
    profile_pic = models.ImageField('pictures/')
    father_name = models.CharField(max_length=25)


class Staff(models.Model):
    DEPARTMENT_CHOICES = (
        ('CE', 'Civil Engineering'),
        ('CSE', 'Computer Science Engineering'),
        ('ECE', 'Electronics Communtication Engineering'),
        ('EEE', 'Electronics Electrical Engineering'),
        ('ME', 'Mechanical Engineering')
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    staff = models.OneToOneField(User, related_name="staff_info", on_delete=models.CASCADE)
    staff_dept = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES, default=None)
    staff_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    staff_mob = models.IntegerField()
    qualification = models.TextField(max_length=10)
    experience = models.CharField(max_length=10)
    staff_pic = models.ImageField('pictures/')