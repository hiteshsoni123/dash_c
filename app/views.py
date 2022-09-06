from django.shortcuts import render
from django.shortcuts import redirect
from app.models import Employee,Emp_login,Holiday
from django.contrib import messages




# def register(request):
#     return render(request, "emp_register.html")

# def ssregister(request):
#     employee_name = request.POST.get('t1')
#     employee_id = request.POST.get('t2')
#     username = request.POST.get('t10')
#     date_of_birth = request.POST.get('t3')
#     employee_contact = request.POST.get('t4')
#     employee_email = request.POST.get('t5')
#     employee_designation = request.POST.get('t6')
#     date_of_joining = request.POST.get('t7')
#     employee_image = request.POST.get('t8')
#     password = request.POST.get('t9')
#     sm = Employee(employee_name=employee_name, employee_id=employee_id, username=username ,date_of_birth=date_of_birth, employee_contact=employee_contact, employee_email=employee_email, employee_designation=employee_designation, date_of_joining=date_of_joining, employee_image=employee_image )
#     sm.save()

#     Emp_login(username=username,password=password).save()
#     # return render(request,'login.html',{'message':"data is save"})
#     # messages.success(request, "Registration Successfully")
#     return redirect('login')

def login(request):
    return render(request,"login.html")
def empLogin(request):
    u = request.POST.get("username") 
    p = request.POST.get("password")
    try:
        Employee.objects.get(username=u,password=p)
        return render(request,"dashboard.html",{"name":u})
    except Employee.DoesNotExist:
        messages.error(request,"Invalid User")
        # return redirect('login')
        return render(request,'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def holiday_list(request):
    data = Holiday.objects.all()
    count = len(data)
    return render(request, 'holiday_list.html',{"data":data, "count":count})
