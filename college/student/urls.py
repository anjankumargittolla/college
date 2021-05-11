from django.urls import path
from . import views
app_name = 'student'
urlpatterns = [
    path('home/',views.home , name = 'home'),
    path('application/',views.student_application, name = 'student_application'),
    path('apply/',views.student_apply, name = 'student_apply'),
    path('registration/',views.student_registration, name = 'student_registration'),
    path('register/',views.student_reg, name = 'student_reg'),
    path('student_login/',views.student_login, name = 'student_login'),
    path('check/', views.check, name = 'check'),
    path('student_logout/',views.student_logout, name = 'student_logout'),
    path('staff_registration/',views.staff_registration, name = 'staff_registration'),
    path('staff_register/', views.staff_register, name = 'staff_register'),
    path('staff_login/',views.staff_login, name = 'staff_login'),
    path('staff_check/', views.staff_check, name = 'staff_check'),
    path('students_list/', views.student_list, name = 'student_list'),
    path('staff_logout/',views.staff_logout, name = 'staff_logout'),
    path('staff_list/', views.staff_list, name = 'staff_list'),
    path('stu_dept/', views.stu_dept, name='stu_dep'),
    path('ce_stu_list/', views.ce_stu_list, name='ce_stu_list'),
 ]