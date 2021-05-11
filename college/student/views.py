from django.contrib.auth.models import User
from django.shortcuts import render
from .models import StudentApplication, Student, Staff
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'student/home.html')


def student_application(request):
    return render(request, 'student/application.html')


def student_apply(request):
    if request.method == 'POST':
        StudentApplication.objects.create(student_name = request.POST['student_name'],
                                          student_email = request.POST['student_email'],
                                          ssc_marks = request.POST['ssc_marks'],
                                          inter_marks = request.POST['inter_marks'])
    return HttpResponseRedirect('/student/home/')


def student_registration(request):
    return render(request,'student/register.html')


def student_reg(request):
    st = StudentApplication.objects.get(student_email=request.POST["email"])
    if request.method == 'POST' and st.is_approved == True:
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST["email"],
            password=request.POST['password'],
            is_staff = 'False'
        )
        user.set_password('password')
        Student.objects.create(student=user,
                               student_app = st,
                               mobile=request.POST['mobile'],
                               profile_pic=request.FILES['profile_pic'],
                               department=request.POST['department'],
                               gender=request.POST['gender'],
                               father_name=request.POST['father_name']
        )
        return HttpResponseRedirect('/student/home/')
    else:
        return HttpResponse("Aproval is not given")


def student_login(request):
    return render(request,'student/login.html')


def profile(request):
    student = Student.objects.get(student=request.user)
    data = {
        'Name': student.student.username,
        "Email": student.student.email,
        "Department": student.department,
        "Data": student.profile_pic,
        "sscmarks": student.student_app.ssc_marks,
        "intermarks": student.student_app.inter_marks
    }
    return render(request,'student/stlist.html',{'primary' : data})


def check(request):
    # import pdb
    # pdb.set_trace()
    UserModel = get_user_model()
    if not request.user.is_anonymous:
        return profile(request)
    elif request.method == "POST":
        try:
            user = UserModel.objects.get(email=request.POST['email'])
        except UserModel.DoesNotExist:
            return HttpResponse('Student credentials are not correct')
        else:
            if user.check_password(request.POST['password']):
                login(request, user)
                return profile(request)
    else:
        return render(request,'student/student_login.html',{})


@login_required(login_url='/student/student_login/')
def student_list(request):
    user = User.objects.filter(is_staff='False')
    #print(user)
    # st_list = Student.objects.all()
    # data = {
    #     'user' : user,
    #     'st_list' : st_list
    # }
    # print(user)
    return render(request, 'student/students_list.html',{"list" : user})


def student_logout(request):
    logout(request)
    return HttpResponseRedirect('/student/student_login/')


def staff_registration(request):
    return render(request,'student/staff_reg.html')


def staff_register(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST["email"],
            password=request.POST['password'],
            is_staff='True'
        )
        user.set_password('password')
        Staff.objects.create(staff=user,
                             staff_mob=request.POST['staff_mob'],
                             staff_dept=request.POST['staff_dept'],
                             staff_pic=request.FILES['staff_pic'],
                             qualification=request.POST['qualification'],
                             experience=request.POST['experience'],
                             staff_gender=request.POST['staff_gender']
        )

    return HttpResponseRedirect('/student/home/')


def staff_login(request):
    return render(request,'student/staff_login.html')


def staff_profile(request):
    staff = Staff.objects.get(staff=request.user)
    staff_data = {
        "name": staff.staff.username,
        "email": staff.staff.email,
        "department": staff.staff_dept,
        "qualification": staff.qualification,
        "experience": staff.experience,
        "mobile": staff.staff_mob,
        "staff_pic": staff.staff_pic
    }
    return render(request, "student/staff_details.html", {"staff": staff_data})


def staff_check(request):
    UserModel = get_user_model()
    if not request.user.is_anonymous:
        return staff_profile(request)
    elif request.method == "POST":
        try:
            user = UserModel.objects.get(email=request.POST['email'])
        except UserModel.DoesNotExist:
            return HttpResponse('Staff credentials are not correct')
        else:
            if user.check_password(request.POST['password']):
                login(request, user)
                return staff_profile(request)
    else:
        return render(request,'student/staff_login.html',{})
    return HttpResponse('Staff credentials are not correct')


def staff_logout(request):
    logout(request)
    return HttpResponseRedirect('/student/staff_login/')


@login_required(login_url='/student/staff_login/')
def staff_list(request):
    user = User.objects.filter(is_staff="True")
    staff_list = Staff.objects.all()
    #print(staff_list)
    return render(request, 'student/staff_list.html', {'staff' : user})


@login_required
def stu_dept(request):
    return render(request,'student/stu_dept.html')


@login_required
def ce_stu_list(reruest):
    ce_list = Student.objects.filter(department=reruest.POST['department'])
    return render(reruest,'student/ce_list.html',{'ce' : ce_list})