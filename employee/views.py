from django.shortcuts import render,redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employees
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_emp(request):
    #validation
    if not request.user.has_perm('employee.add_emp'):
        redirect('view_Employee')

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_emp')
    else :
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html', {'form':form})

@login_required
def view_emp(request):
    search_query = request.GET.get('search', '')
    sort = request.GET.get('sort', '')

    employees = Employees.objects.all()
    # Searching
    if search_query and search_query.strip():
        employees = employees.filter(
            Q(name__icontains=search_query.strip()) | 
            Q(email__icontains=search_query.strip())
        )

    # Sorting
    if sort == 'name_asc':
        employees = employees.order_by(Lower('name').asc())
    elif sort == 'name_desc':
        employees = employees.order_by(Lower('name').desc())
    elif sort == 'salary_asc':
            employees = employees.order_by('salary')
    elif sort == 'salary_desc':
                employees = employees.order_by('-salary')

    # Pagination 
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee/view_employee.html', {'page_obj': page_obj,'employees': page_obj})


@login_required
def update_emp(request, id):
    #validation
    if not request.user.has_perm('employee.update_emp'):
        redirect('view_Employee')
            
    employee = Employees.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view_emp')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/update_employee.html', {'employee':employee , 'form':form})


@login_required
def delete_emp(request, id):
    #validation
    if not request.user.has_perm('employee.delete_emp'):
        redirect('view_Employee')
            
    employee = Employees.objects.get(id =id)
    employee.delete()
    return redirect('view_emp')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print("Authenticated User:", user)

        if user is not None:
            login(request, user)
            print("Login Successful, redirecting to view_emp...")
            request.session['username'] = username
            return redirect('view_emp')
        else:
            return render(request, 'employee/home.html', {'error': "Invalid Username or Password"})
            
    return render(request, 'employee/home.html')

def user_logout(request):
     logout(request)
     request.session.flush()
     return redirect("user_login")