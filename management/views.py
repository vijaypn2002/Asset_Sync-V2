from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db import IntegrityError
from datetime import datetime
import csv
from collections import Counter
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collections import Counter



# Import the User model
from django.contrib.auth.models import User

from .models import (
    Employee, Laptop, Desktop, Printer, iPad, iPhone, Smartphone,
    KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter,
    SIM, RentalAsset
)
from .forms import (
    UserForm, EmployeeForm, LaptopForm, DesktopForm, PrinterForm, iPadForm,
    iPhoneForm, SmartphoneForm, KeypadPhoneForm, HeadsetForm, KeyboardForm,
    MouseForm, PendriveForm, HardDiskForm, LanAdapterForm, SIMForm,
    RentalAssetForm
)

# User Management Views
@login_required
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User added successfully!')
            return redirect('settings')
    else:
        form = UserForm()
    return render(request, 'management/add_user.html', {'form': form})


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('settings')
    else:
        form = UserForm(instance=user)
    return render(request, 'management/edit_user.html', {'form': form})


@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('settings')
    return render(request, 'management/delete_user.html', {'user': user})


@login_required
def settings(request):
    return render(request, 'management/settings.html')


@login_required
def homepage(request):
    return render(request, 'management/homepage.html')

#####################################################################################
#########################################################################################
######################################################################################
from collections import Counter
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, RentalAsset, Employee

@login_required
def dashboard(request):
    # Fetch data for the dashboard
    laptops = Laptop.objects.select_related('employee').all()
    desktops = Desktop.objects.select_related('employee').all()
    printers = Printer.objects.select_related('employee').all()
    ipads = iPad.objects.select_related('employee').all()
    iphones = iPhone.objects.select_related('employee').all()
    smartphones = Smartphone.objects.select_related('employee').all()
    keypadphones = KeypadPhone.objects.select_related('employee').all()
    headsets = Headset.objects.select_related('employee').all()
    keyboards = Keyboard.objects.select_related('employee').all()
    mice = Mouse.objects.select_related('employee').all()
    pendrives = Pendrive.objects.select_related('employee').all()
    harddisks = HardDisk.objects.select_related('employee').all()
    lanadapters = LanAdapter.objects.select_related('employee').all()
    sims = SIM.objects.select_related('employee').all()
    rental_assets = RentalAsset.objects.select_related('employee').all()

    all_assets = list(laptops) + list(desktops) + list(printers) + list(ipads) + \
                 list(iphones) + list(smartphones) + list(keypadphones) + \
                 list(headsets) + list(keyboards) + list(mice) + \
                 list(pendrives) + list(harddisks) + list(lanadapters) + \
                 list(sims) + list(rental_assets)

    # Filter assets that are assigned to employees
    assigned_assets = [asset for asset in all_assets if asset.employee]

    # Group by branch and department
    branch_counts = Counter(asset.employee.branch for asset in assigned_assets if asset.employee and asset.employee.branch)
    department_counts = Counter(asset.employee.department for asset in assigned_assets if asset.employee and asset.employee.department)

    # Prepare data for the charts
    branch_labels = list(branch_counts.keys())
    branch_values = list(branch_counts.values())
    department_labels = list(department_counts.keys())
    department_values = list(department_counts.values())

    # Fetch employee data
    employees = Employee.objects.all()
    branch_employee_counts = Counter(employees.values_list('branch', flat=True))
    department_employee_counts = Counter(employees.values_list('department', flat=True))

    branch_employee_labels = list(branch_employee_counts.keys())
    branch_employee_values = list(branch_employee_counts.values())
    department_employee_labels = list(department_employee_counts.keys())
    department_employee_values = list(department_employee_counts.values())

    # Assigned assets by department
    assigned_department_counts = Counter(asset.employee.department for asset in assigned_assets if asset.employee and asset.employee.department)
    assigned_department_labels = list(assigned_department_counts.keys())
    assigned_department_values = list(assigned_department_counts.values())

    # Fetch the total counts
    total_employees = Employee.objects.count()
    total_assets = len(all_assets)
    assigned_assets_count = len(assigned_assets)

    # Asset counts by type
    asset_types = ['Laptop', 'Desktop', 'Printer', 'iPad', 'iPhone', 'Smartphone', 'KeypadPhone', 'Headset', 'Keyboard', 'Mouse', 'Pendrive', 'HardDisk', 'LanAdapter', 'SIM', 'RentalAsset']
    asset_counts = [len(laptops), len(desktops), len(printers), len(ipads), len(iphones), len(smartphones), len(keypadphones), len(headsets), len(keyboards), len(mice), len(pendrives), len(harddisks), len(lanadapters), len(sims), len(rental_assets)]

    # Free assets by type
    free_assets_by_type = [
        laptops.filter(employee__isnull=True).count(),
        desktops.filter(employee__isnull=True).count(),
        printers.filter(employee__isnull=True).count(),
        ipads.filter(employee__isnull=True).count(),
        iphones.filter(employee__isnull=True).count(),
        smartphones.filter(employee__isnull=True).count(),
        keypadphones.filter(employee__isnull=True).count(),
        headsets.filter(employee__isnull=True).count(),
        keyboards.filter(employee__isnull=True).count(),
        mice.filter(employee__isnull=True).count(),
        pendrives.filter(employee__isnull=True).count(),
        harddisks.filter(employee__isnull=True).count(),
        lanadapters.filter(employee__isnull=True).count(),
        sims.filter(employee__isnull=True).count(),
        rental_assets.filter(employee__isnull=True).count(),
    ]

    context = {
        'branch_labels': branch_labels,
        'branch_values': branch_values,
        'department_labels': department_labels,
        'department_values': department_values,
        'branch_employee_labels': branch_employee_labels,
        'branch_employee_values': branch_employee_values,
        'department_employee_labels': department_employee_labels,
        'department_employee_values': department_employee_values,
        'assigned_department_labels': assigned_department_labels,
        'assigned_department_values': assigned_department_values,
        'total_employees': total_employees,
        'total_assets': total_assets,
        'assigned_assets_count': assigned_assets_count,
        'asset_types': asset_types,
        'asset_counts': asset_counts,
        'free_assets_by_type': free_assets_by_type,
    }
    return render(request, 'management/dashboard.html', context)

#####################################################################################
####################################################################################
##################################################################################

@login_required
def onboarding_exit_clearance(request):
    return render(request, 'management/onboarding_exit_clearance.html')


# Employee Management Views
@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            if Employee.objects.filter(employee_id=employee_id).exists():
                messages.error(request, "This employee ID already exists.")
            else:
                form.save()
                messages.success(request, "Employee added successfully.")
                return redirect('view_employee')
    else:
        form = EmployeeForm()
    return render(request, 'management/add_employee.html', {'form': form})

from django.db.models import Q  # For complex queries with search

@login_required
def view_employee(request):
    # Get all active employees
    employee_list = Employee.objects.filter(exited=False)

    # Get filter values from request
    department = request.GET.get('department')
    designation = request.GET.get('designation')
    branch = request.GET.get('branch')
    search_query = request.GET.get('search')

    # Apply filters if values are provided
    if department:
        employee_list = employee_list.filter(department=department)
    if designation:
        employee_list = employee_list.filter(designation=designation)
    if branch:
        employee_list = employee_list.filter(branch=branch)

    # Apply search if search_query is provided (search by name or employee ID)
    if search_query:
        employee_list = employee_list.filter(
            Q(name__icontains=search_query) | Q(employee_id__icontains=search_query)
        )

    # Add pagination
    paginator = Paginator(employee_list, 20)
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)

    # Get distinct values for filters (to populate filter options in the template)
    departments = Employee.objects.values_list('department', flat=True).distinct()
    designations = Employee.objects.values_list('designation', flat=True).distinct()
    branches = Employee.objects.values_list('branch', flat=True).distinct()

    # Render template with filters and search functionality
    context = {
        'employees': employees,
        'departments': departments,
        'designations': designations,
        'branches': branches,
    }
    return render(request, 'management/view_employee.html', context)



@login_required
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    if request.method == 'POST':
        try:
            date_of_joining = request.POST.get('date_of_joining')
            if date_of_joining:
                date_of_joining = datetime.strptime(date_of_joining, "%Y-%m-%d").date()
                employee.date_of_joining = date_of_joining

            employee.name = request.POST.get('name')
            employee.department = request.POST.get('department')
            employee.designation = request.POST.get('designation')
            employee.branch = request.POST.get('branch')
            employee.work_location = request.POST.get('work_location')
            employee.reporting_officer = request.POST.get('reporting_officer')
            employee.personal_email_id = request.POST.get('personal_email_id')

            employee.save()
            messages.success(request, "Employee details updated successfully.")
            return redirect('view_employee')
        except ValidationError as e:
            messages.error(request, f"Error updating employee: {e}")
    return render(request, 'management/edit_employee.html', {'employee': employee})


@login_required
def bulk_import_employees(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('employee_csv')
        if not csv_file:
            messages.error(request, "No CSV file uploaded.")
            return redirect('add_employee')

        decoded_file = csv_file.read().decode('utf-8-sig').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            row = {k.lower(): v for k, v in row.items()}
            employee_id = row.get('employee_id')
            date_of_joining = row.get('date_of_joining')
            name = row.get('name')
            work_location = row.get('work_location', 'Default Location')
            reporting_officer = row.get('reporting_officer', 'Unknown Officer')

            if not name or not date_of_joining or not employee_id:
                messages.error(request, "Required fields are missing. Skipping row.")
                continue

            try:
                date_of_joining = datetime.strptime(date_of_joining, "%d-%m-%Y").date()
            except ValueError:
                messages.error(request, f"Invalid date format for Employee ID {employee_id}. Skipping row.")
                continue

            if not Employee.objects.filter(employee_id=employee_id).exists():
                try:
                    Employee.objects.create(
                        date_of_joining=date_of_joining,
                        employee_id=employee_id,
                        name=name,
                        department=row.get('department'),
                        designation=row.get('designation'),
                        branch=row.get('branch'),
                        work_location=work_location,
                        reporting_officer=reporting_officer,
                        personal_email_id=row.get('personal_email_id')
                    )
                except IntegrityError as e:
                    messages.error(request, f"Error saving Employee ID {employee_id}: {str(e)}")
            else:
                messages.warning(request, f"Employee ID {employee_id} already exists. Skipping row.")

        messages.success(request, "Bulk import completed successfully.")
        return redirect('view_employee')

    return redirect('add_employee')


@login_required
def exit_employee(request):
    # Filter only non-exited employees
    employees_list = Employee.objects.filter(exited=False)

    # Get filter values from request
    department = request.GET.get('department')
    designation = request.GET.get('designation')
    branch = request.GET.get('branch')
    search_query = request.GET.get('search')

    # Apply filters if values are provided
    if department:
        employees_list = employees_list.filter(department=department)
    if designation:
        employees_list = employees_list.filter(designation=designation)
    if branch:
        employees_list = employees_list.filter(branch=branch)

    # Apply search if search_query is provided (search by name or employee ID)
    if search_query:
        employees_list = employees_list.filter(
            Q(name__icontains=search_query) | Q(employee_id__icontains=search_query)
        )

    # Add pagination
    paginator = Paginator(employees_list, 20)
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)

    # Get distinct values for filters
    departments = Employee.objects.values_list('department', flat=True).distinct()
    designations = Employee.objects.values_list('designation', flat=True).distinct()
    branches = Employee.objects.values_list('branch', flat=True).distinct()

    # Render template with filters and search functionality
    context = {
        'employees': employees,
        'departments': departments,
        'designations': designations,
        'branches': branches,
    }
    return render(request, 'management/exit_employee.html', context)




@login_required
def confirm_exit_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    if request.method == 'POST':
        # Mark the employee as exited
        employee.exited = True
        employee.save()
        messages.success(request, f"Employee {employee.employee_id} has been exited.")
        return redirect('exit_employee')  # Redirect to the Exit Employee page
    return render(request, 'management/confirm_exit_employee.html', {'employee': employee})



@login_required
def exit_tracker(request):
    # Show only employees who have exited
    exited_employees = Employee.objects.filter(exited=True)
    
    # Add pagination
    paginator = Paginator(exited_employees, 20)  # Show 20 employees per page
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)

    return render(request, 'management/exit_tracker.html', {'employees': employees})




@login_required
def restore_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    if request.method == 'POST':
        employee.exited = False
        employee.save()
        messages.success(request, f"Employee {employee.employee_id} has been restored.")
        return redirect('exit_tracker')
    return render(request, 'management/restore_employee.html', {'employee': employee})


# Asset Management Views
@login_required
def asset_management(request):
    return render(request, 'management/asset_management.html')


@login_required
def add_asset(request):
    return render(request, 'management/add_asset.html')


@login_required
def view_asset(request):
    return render(request, 'management/view_asset.html')


# Hardware Views
@login_required
def add_hardware(request):
    return render(request, 'management/add_hardware.html')


# Laptop Views
@login_required
def add_laptop(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_laptops')
    else:
        form = LaptopForm()
    return render(request, 'management/add_laptop.html', {'form': form})


from django.core.paginator import Paginator

@login_required
def view_laptops(request):
    laptops_list = Laptop.objects.all()
    paginator = Paginator(laptops_list, 10)  # Show 10 laptops per page
    
    page_number = request.GET.get('page')
    laptops = paginator.get_page(page_number)
    
    return render(request, 'management/view_laptops.html', {'laptops': laptops})


@login_required
def edit_laptop(request, laptop_id):
    laptop = get_object_or_404(Laptop, pk=laptop_id)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('view_laptops')
    else:
        if laptop.date_of_purchase:
            laptop.date_of_purchase = laptop.date_of_purchase.strftime('%d-%m-%Y')
        form = LaptopForm(instance=laptop)
    return render(request, 'management/edit_laptop.html', {'form': form})


@login_required
def delete_laptop(request, laptop_id):
    laptop = get_object_or_404(Laptop, pk=laptop_id)
    if request.method == 'POST':
        laptop.delete()
        return redirect('view_laptops')
    return render(request, 'management/delete_laptop.html', {'laptop': laptop})


# Desktop Views
from django.core.paginator import Paginator

@login_required
def view_desktops(request):
    desktops_list = Desktop.objects.all()
    paginator = Paginator(desktops_list, 10)  # Show 10 desktops per page
    
    page_number = request.GET.get('page')
    desktops = paginator.get_page(page_number)
    
    return render(request, 'management/view_desktops.html', {'desktops': desktops})



@login_required
def add_desktop(request):
    if request.method == 'POST':
        form = DesktopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_desktops')
    else:
        form = DesktopForm()
    return render(request, 'management/add_desktop.html', {'form': form})


@login_required
def edit_desktop(request, desktop_id):
    desktop = get_object_or_404(Desktop, pk=desktop_id)
    if request.method == 'POST':
        form = DesktopForm(request.POST, instance=desktop)
        if form.is_valid():
            form.save()
            return redirect('view_desktops')
    else:
        if desktop.date_of_purchase:
            desktop.date_of_purchase = desktop.date_of_purchase.strftime('%d-%m-%Y')
        if desktop.warranty_date:
            desktop.warranty_date = desktop.warranty_date.strftime('%d-%m-%Y')
        form = DesktopForm(instance=desktop)
    return render(request, 'management/edit_desktop.html', {'form': form})


@login_required
def delete_desktop(request, desktop_id):
    desktop = get_object_or_404(Desktop, pk=desktop_id)
    if request.method == 'POST':
        desktop.delete()
        return redirect('view_desktops')
    return render(request, 'management/delete_desktop.html', {'desktop': desktop})


# Printer Views
from django.core.paginator import Paginator

@login_required
def view_printers(request):
    printers_list = Printer.objects.all()
    paginator = Paginator(printers_list, 10)  # Show 10 printers per page

    page_number = request.GET.get('page')
    printers = paginator.get_page(page_number)

    return render(request, 'management/view_printers.html', {'printers': printers})


@login_required
def add_printer(request):
    if request.method == 'POST':
        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()  # Ensure data is actually saved to the database
            return redirect('view_printers')
        else:
            print(form.errors)  # This can help identify validation errors
    else:
        form = PrinterForm()
    return render(request, 'management/add_printer.html', {'form': form})


@login_required
def edit_printer(request, printer_id):
    printer = get_object_or_404(Printer, pk=printer_id)
    if request.method == 'POST':
        form = PrinterForm(request.POST, instance=printer)
        if form.is_valid():
            form.save()
            return redirect('view_printers')
    else:
        if printer.date_of_purchase:
            printer.date_of_purchase = printer.date_of_purchase.strftime('%d-%m-%Y')
        if printer.warranty_date:
            printer.warranty_date = printer.warranty_date.strftime('%d-%m-%Y')
        form = PrinterForm(instance=printer)
    return render(request, 'management/edit_printer.html', {'form': form})


@login_required
def delete_printer(request, printer_id):
    printer = get_object_or_404(Printer, pk=printer_id)
    if request.method == 'POST':
        printer.delete()
        return redirect('view_printers')
    return render(request, 'management/delete_printer.html', {'printer': printer})


# iPad Views
from django.core.paginator import Paginator

@login_required
def view_ipads(request):
    ipads_list = iPad.objects.all()
    paginator = Paginator(ipads_list, 10)  # Show 10 iPads per page

    page_number = request.GET.get('page')
    ipads = paginator.get_page(page_number)

    return render(request, 'management/view_ipads.html', {'ipads': ipads})



@login_required
def add_ipad(request):
    if request.method == 'POST':
        form = iPadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_ipads')
    else:
        form = iPadForm()
    return render(request, 'management/add_ipad.html', {'form': form})


@login_required
def edit_ipad(request, ipad_id):
    ipad = get_object_or_404(iPad, pk=ipad_id)
    if request.method == 'POST':
        form = iPadForm(request.POST, instance=ipad)
        if form.is_valid():
            form.save()
            return redirect('view_ipads')
    else:
        if ipad.date_of_purchase:
            ipad.date_of_purchase = ipad.date_of_purchase.strftime('%d-%m-%Y')
        if ipad.warranty_date:
            ipad.warranty_date = ipad.warranty_date.strftime('%d-%m-%Y')
        form = iPadForm(instance=ipad)
    return render(request, 'management/edit_ipad.html', {'form': form})


@login_required
def delete_ipad(request, ipad_id):
    ipad = get_object_or_404(iPad, pk=ipad_id)
    if request.method == 'POST':
        ipad.delete()
        return redirect('view_ipads')
    return render(request, 'management/delete_ipad.html', {'ipad': ipad})


# iPhone Views
from django.core.paginator import Paginator

@login_required
def view_iphones(request):
    iphones_list = iPhone.objects.all()
    paginator = Paginator(iphones_list, 10)  # Show 10 iPhones per page

    page_number = request.GET.get('page')
    iphones = paginator.get_page(page_number)

    return render(request, 'management/view_iphones.html', {'iphones': iphones})



from django.contrib import messages

@login_required
def add_iphone(request):
    if request.method == 'POST':
        form = iPhoneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'iPhone added successfully!')  # Success message
            return redirect('view_iphones')  # Redirect with correct syntax
    else:
        form = iPhoneForm()

    return render(request, 'management/add_iphone.html', {'form': form})




@login_required
def edit_iphone(request, iphone_id):
    iphone = get_object_or_404(iPhone, pk=iphone_id)
    if request.method == 'POST':
        form = iPhoneForm(request.POST, instance=iphone)
        if form.is_valid():
            form.save()
            return redirect('view_iphones')
    else:
        if iphone.date_of_purchase:
            iphone.date_of_purchase = iphone.date_of_purchase.strftime('%d-%m-%Y')
        if iphone.warranty_date:
            iphone.warranty_date = iphone.warranty_date.strftime('%d-%m-%Y')
        form = iPhoneForm(instance=iphone)
    return render(request, 'management/edit_iphone.html', {'form': form})


@login_required
def delete_iphone(request, iphone_id):
    iphone = get_object_or_404(iPhone, pk=iphone_id)
    if request.method == 'POST':
        iphone.delete()
        return redirect('view_iphones')
    return render(request, 'management/delete_iphone.html', {'iphone': iphone})


# Smartphone Views
from django.core.paginator import Paginator

@login_required
def view_smartphones(request):
    smartphones_list = Smartphone.objects.all()
    paginator = Paginator(smartphones_list, 10)  # Show 10 smartphones per page

    page_number = request.GET.get('page')
    smartphones = paginator.get_page(page_number)

    return render(request, 'management/view_smartphones.html', {'smartphones': smartphones})


@login_required
def add_smartphone(request):
    if request.method == 'POST':
        form = SmartphoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_smartphones')  # Redirect to view smartphones after successful form submission
    else:
        form = SmartphoneForm()

    return render(request, 'management/add_smartphone.html', {'form': form})


@login_required
def edit_smartphone(request, smartphone_id):
    smartphone = get_object_or_404(Smartphone, pk=smartphone_id)
    if request.method == 'POST':
        form = SmartphoneForm(request.POST, instance=smartphone)
        if form.is_valid():
            form.save()
            return redirect('view_smartphones')
    else:
        if smartphone.date_of_purchase:
            smartphone.date_of_purchase = smartphone.date_of_purchase.strftime('%d-%m-%Y')
        if smartphone.warranty_date:
            smartphone.warranty_date = smartphone.warranty_date.strftime('%d-%m-%Y')
        form = SmartphoneForm(instance=smartphone)
    return render(request, 'management/edit_smartphone.html', {'form': form})


@login_required
def delete_smartphone(request, smartphone_id):
    smartphone = get_object_or_404(Smartphone, pk=smartphone_id)
    if request.method == 'POST':
        smartphone.delete()
        return redirect('view_smartphones')
    return render(request, 'management/delete_smartphone.html', {'smartphone': smartphone})


# Keypad Phone Views
from django.core.paginator import Paginator

@login_required
def view_keypadphones(request):
    keypadphones_list = KeypadPhone.objects.all()
    paginator = Paginator(keypadphones_list, 10)  # Show 10 keypad phones per page

    page_number = request.GET.get('page')
    keypadphones = paginator.get_page(page_number)

    return render(request, 'management/view_keypadphones.html', {'keypadphones': keypadphones})



@login_required
def add_keypadphone(request):
    if request.method == 'POST':
        form = KeypadPhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_keypadphones')  # Redirect to view keypad phones after successful form submission
    else:
        form = KeypadPhoneForm()

    return render(request, 'management/add_keypadphone.html', {'form': form})



@login_required
def edit_keypadphone(request, keypadphone_id):
    keypadphone = get_object_or_404(KeypadPhone, pk=keypadphone_id)
    if request.method == 'POST':
        form = KeypadPhoneForm(request.POST, instance=keypadphone)
        if form.is_valid():
            form.save()
            return redirect('view_keypadphones')
    else:
        if keypadphone.date_of_purchase:
            keypadphone.date_of_purchase = keypadphone.date_of_purchase.strftime('%d-%m-%Y')
        if keypadphone.warranty_date:
            keypadphone.warranty_date = keypadphone.warranty_date.strftime('%d-%m-%Y')
        form = KeypadPhoneForm(instance=keypadphone)
    return render(request, 'management/edit_keypadphone.html', {'form': form})


@login_required
def delete_keypadphone(request, keypadphone_id):
    keypadphone = get_object_or_404(KeypadPhone, pk=keypadphone_id)
    if request.method == 'POST':
        keypadphone.delete()
        return redirect('view_keypadphones')
    return render(request, 'management/delete_keypadphone.html', {'keypadphone': keypadphone})


# Accessories Views
@login_required
def add_accessories(request):
    return render(request, 'management/add_accessories.html')


# Headset Views
from django.core.paginator import Paginator

@login_required
def view_headsets(request):
    headsets_list = Headset.objects.all()
    paginator = Paginator(headsets_list, 10)  # Show 10 headsets per page

    page_number = request.GET.get('page')
    headsets = paginator.get_page(page_number)

    return render(request, 'management/view_headsets.html', {'headsets': headsets})



@login_required
def add_headset(request):
    if request.method == 'POST':
        form = HeadsetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_headsets')
    else:
        form = HeadsetForm()
    return render(request, 'management/add_headset.html', {'form': form})


@login_required
def edit_headset(request, headset_id):
    headset = get_object_or_404(Headset, pk=headset_id)
    if request.method == 'POST':
        form = HeadsetForm(request.POST, instance=headset)
        if form.is_valid():
            form.save()
            return redirect('view_headsets')
    else:
        if headset.date_of_purchase:
            headset.date_of_purchase = headset.date_of_purchase.strftime('%d-%m-%Y')
        if headset.warranty_date:
            headset.warranty_date = headset.warranty_date.strftime('%d-%m-%Y')
        form = HeadsetForm(instance=headset)
    return render(request, 'management/edit_headset.html', {'form': form})


@login_required
def delete_headset(request, headset_id):
    headset = get_object_or_404(Headset, pk=headset_id)
    if request.method == 'POST':
        headset.delete()
        return redirect('view_headsets')
    return render(request, 'management/delete_headset.html', {'headset': headset})


# Keyboard Views
from django.core.paginator import Paginator

@login_required
def view_keyboards(request):
    keyboards_list = Keyboard.objects.all()
    paginator = Paginator(keyboards_list, 10)  # Show 10 keyboards per page

    page_number = request.GET.get('page')
    keyboards = paginator.get_page(page_number)

    return render(request, 'management/view_keyboards.html', {'keyboards': keyboards})



@login_required
def add_keyboard(request):
    if request.method == 'POST':
        form = KeyboardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_keyboards')
    else:
        form = KeyboardForm()
    return render(request, 'management/add_keyboard.html', {'form': form})


@login_required
def edit_keyboard(request, keyboard_id):
    keyboard = get_object_or_404(Keyboard, pk=keyboard_id)
    if request.method == 'POST':
        form = KeyboardForm(request.POST, instance=keyboard)
        if form.is_valid():
            form.save()
            return redirect('view_keyboards')
    else:
        if keyboard.date_of_purchase:
            keyboard.date_of_purchase = keyboard.date_of_purchase.strftime('%d-%m-%Y')
        if keyboard.warranty_date:
            keyboard.warranty_date = keyboard.warranty_date.strftime('%d-%m-%Y')
        form = KeyboardForm(instance=keyboard)
    return render(request, 'management/edit_keyboard.html', {'form': form})


@login_required
def delete_keyboard(request, keyboard_id):
    keyboard = get_object_or_404(Keyboard, pk=keyboard_id)
    if request.method == 'POST':
        keyboard.delete()
        return redirect('view_keyboards')
    return render(request, 'management/delete_keyboard.html', {'keyboard': keyboard})


# Mouse Views
from django.core.paginator import Paginator

@login_required
def view_mice(request):
    mice_list = Mouse.objects.all()
    paginator = Paginator(mice_list, 10)  # Show 10 mice per page

    page_number = request.GET.get('page')
    mice = paginator.get_page(page_number)

    return render(request, 'management/view_mice.html', {'mice': mice})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MouseForm

@login_required
def add_mouse(request):
    if request.method == 'POST':
        form = MouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_mice')
    else:
        form = MouseForm()

    return render(request, 'management/add_mouse.html', {'form': form})



@login_required
def edit_mouse(request, mouse_id):
    mouse = get_object_or_404(Mouse, pk=mouse_id)
    if request.method == 'POST':
        form = MouseForm(request.POST, instance=mouse)
        if form.is_valid():
            form.save()
            return redirect('view_mice')
    else:
        if mouse.date_of_purchase:
            mouse.date_of_purchase = mouse.date_of_purchase.strftime('%d-%m-%Y')
        if mouse.warranty_date:
            mouse.warranty_date = mouse.warranty_date.strftime('%d-%m-%Y')
        form = MouseForm(instance=mouse)
    return render(request, 'management/edit_mouse.html', {'form': form})


@login_required
def delete_mouse(request, mouse_id):
    mouse = get_object_or_404(Mouse, pk=mouse_id)
    if request.method == 'POST':
        mouse.delete()
        return redirect('view_mice')
    return render(request, 'management/delete_mouse.html', {'mouse': mouse})


# Pendrive Views
from django.core.paginator import Paginator

@login_required
def view_pendrives(request):
    pendrives_list = Pendrive.objects.all()
    paginator = Paginator(pendrives_list, 10)  # Show 10 pendrives per page

    page_number = request.GET.get('page')
    pendrives = paginator.get_page(page_number)

    return render(request, 'management/view_pendrives.html', {'pendrives': pendrives})



@login_required
def add_pendrive(request):
    if request.method == 'POST':
        form = PendriveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_pendrives')
    else:
        form = PendriveForm()
    return render(request, 'management/add_pendrive.html', {'form': form})



@login_required
def edit_pendrive(request, pendrive_id):
    pendrive = get_object_or_404(Pendrive, pk=pendrive_id)
    if request.method == 'POST':
        form = PendriveForm(request.POST, instance=pendrive)
        if form.is_valid():
            form.save()
            return redirect('view_pendrives')
    else:
        if pendrive.date_of_purchase:
            pendrive.date_of_purchase = pendrive.date_of_purchase.strftime('%d-%m-%Y')
        if pendrive.warranty_date:
            pendrive.warranty_date = pendrive.warranty_date.strftime('%d-%m-%Y')
        form = PendriveForm(instance=pendrive)
    return render(request, 'management/edit_pendrive.html', {'form': form})


@login_required
def delete_pendrive(request, pendrive_id):
    pendrive = get_object_or_404(Pendrive, pk=pendrive_id)
    if request.method == 'POST':
        pendrive.delete()
        return redirect('view_pendrives')
    return render(request, 'management/delete_pendrive.html', {'pendrive': pendrive})


# HardDisk Views
from django.core.paginator import Paginator

@login_required
def view_harddisks(request):
    harddisks_list = HardDisk.objects.all()
    paginator = Paginator(harddisks_list, 10)  # Show 10 hard disks per page

    page_number = request.GET.get('page')
    harddisks = paginator.get_page(page_number)

    return render(request, 'management/view_harddisks.html', {'harddisks': harddisks})



@login_required
def add_harddisk(request):
    if request.method == 'POST':
        form = HardDiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_harddisks')
    else:
        form = HardDiskForm()
    return render(request, 'management/add_harddisk.html', {'form': form})


@login_required
def edit_harddisk(request, harddisk_id):
    harddisk = get_object_or_404(HardDisk, pk=harddisk_id)
    if request.method == 'POST':
        form = HardDiskForm(request.POST, instance=harddisk)
        if form.is_valid():
            form.save()
            return redirect('view_harddisks')
    else:
        if harddisk.date_of_purchase:
            harddisk.date_of_purchase = harddisk.date_of_purchase.strftime('%d-%m-%Y')
        if harddisk.warranty_date:
            harddisk.warranty_date = harddisk.warranty_date.strftime('%d-%m-%Y')
        form = HardDiskForm(instance=harddisk)
    return render(request, 'management/edit_harddisk.html', {'form': form})


@login_required
def delete_harddisk(request, harddisk_id):
    harddisk = get_object_or_404(HardDisk, pk=harddisk_id)
    if request.method == 'POST':
        harddisk.delete()
        return redirect('view_harddisks')
    return render(request, 'management/delete_harddisk.html', {'harddisk': harddisk})


# LanAdapter Views
from django.core.paginator import Paginator

@login_required
def view_lanadapters(request):
    lanadapters_list = LanAdapter.objects.all()
    paginator = Paginator(lanadapters_list, 10)  # Show 10 LAN adapters per page

    page_number = request.GET.get('page')
    lanadapters = paginator.get_page(page_number)

    return render(request, 'management/view_lanadapters.html', {'lanadapters': lanadapters})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LanAdapterForm

@login_required
def add_lanadapter(request):
    if request.method == 'POST':
        form = LanAdapterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_lanadapters')  # Make sure this view exists and is correct
        else:
            print(form.errors)  # This will print validation errors to the console
    else:
        form = LanAdapterForm()
    return render(request, 'management/add_lanadapter.html', {'form': form})


@login_required
def edit_lanadapter(request, lanadapter_id):
    lanadapter = get_object_or_404(LanAdapter, pk=lanadapter_id)
    if request.method == 'POST':
        form = LanAdapterForm(request.POST, instance=lanadapter)
        if form.is_valid():
            form.save()
            return redirect('view_lanadapters')
    else:
        if lanadapter.date_of_purchase:
            lanadapter.date_of_purchase = lanadapter.date_of_purchase.strftime('%d-%m-%Y')
        if lanadapter.warranty_date:
            lanadapter.warranty_date = lanadapter.warranty_date.strftime('%d-%m-%Y')
        form = LanAdapterForm(instance=lanadapter)
    return render(request, 'management/edit_lanadapter.html', {'form': form})


@login_required
def delete_lanadapter(request, lanadapter_id):
    lanadapter = get_object_or_404(LanAdapter, pk=lanadapter_id)
    if request.method == 'POST':
        lanadapter.delete()
        return redirect('view_lanadapters')
    return render(request, 'management/delete_lanadapter.html', {'lanadapter': lanadapter})


# Communication Devices Views
@login_required
def add_communication_devices(request):
    return render(request, 'management/add_communication_devices.html')


# SIM Views
from django.core.paginator import Paginator

@login_required
def view_sims(request):
    sims_list = SIM.objects.all()
    paginator = Paginator(sims_list, 10)  # Show 10 SIMs per page

    page_number = request.GET.get('page')
    sims = paginator.get_page(page_number)

    return render(request, 'management/view_sims.html', {'sims': sims})



@login_required
def add_sim(request):
    if request.method == 'POST':
        form = SIMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_sims')
    else:
        form = SIMForm()
    return render(request, 'management/add_sim.html', {'form': form})



@login_required
def edit_sim(request, sim_id):
    sim = get_object_or_404(SIM, pk=sim_id)
    if request.method == 'POST':
        form = SIMForm(request.POST, instance=sim)
        if form.is_valid():
            form.save()
            return redirect('view_sims')
    else:
        form = SIMForm(instance=sim)
    return render(request, 'management/edit_sim.html', {'form': form})


@login_required
def delete_sim(request, sim_id):
    sim = get_object_or_404(SIM, pk=sim_id)
    if request.method == 'POST':
        sim.delete()
        return redirect('view_sims')
    return render(request, 'management/delete_sim.html', {'sim': sim})


from django.core.paginator import Paginator

@login_required
def view_rental_assets(request):
    rental_assets_list = RentalAsset.objects.all()
    paginator = Paginator(rental_assets_list, 10)  # Show 10 rental assets per page

    page_number = request.GET.get('page')
    rental_assets = paginator.get_page(page_number)

    return render(request, 'management/view_rental_assets.html', {'rental_assets': rental_assets})



@login_required
def add_rental_asset(request):
    if request.method == 'POST':
        form = RentalAssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_rental_assets')
    else:
        form = RentalAssetForm()
    return render(request, 'management/add_rental_asset.html', {'form': form})


@login_required
def edit_rental_asset(request, rental_asset_id):
    rental_asset = get_object_or_404(RentalAsset, pk=rental_asset_id)
    if request.method == 'POST':
        form = RentalAssetForm(request.POST, instance=rental_asset)
        if form.is_valid():
            form.save()
            return redirect('view_rental_assets')
    else:
        if rental_asset.date_of_purchase:
            rental_asset.date_of_purchase = rental_asset.date_of_purchase.strftime('%d-%m-%Y')
        form = RentalAssetForm(instance=rental_asset)
    return render(request, 'management/edit_rental_asset.html', {'form': form})


@login_required
def delete_rental_asset(request, rental_asset_id):
    rental_asset = get_object_or_404(RentalAsset, pk=rental_asset_id)
    if request.method == 'POST':
        rental_asset.delete()
        return redirect('view_rental_assets')
    return render(request, 'management/delete_rental_asset.html', {'rental_asset': rental_asset})


# Asset Assignment Views
#########################################################################################
##########################################################################################
###############################################################################################
#############################################################################################
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Laptop, Employee, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM

# Asset Assignment Views
@login_required
def assign_asset(request):
    return render(request, 'management/assign_asset.html')

from django.shortcuts import render
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM

# A dictionary to map asset types to their corresponding model
ASSET_MODELS = {
    'Laptop': Laptop,
    'Desktop': Desktop,
    'Printer': Printer,
    'iPad': iPad,
    'iPhone': iPhone,
    'Smartphone': Smartphone,
    'KeypadPhone': KeypadPhone,
    'Headset': Headset,
    'Keyboard': Keyboard,
    'Mouse': Mouse,
    'Pendrive': Pendrive,
    'HardDisk': HardDisk,
    'LanAdapter': LanAdapter,
    'SIM': SIM,
}

# View for Total Assets
from django.core.paginator import Paginator
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *

def total_assets(request):
    asset_type = request.GET.get('asset_type', 'Laptop')
    brand_filter = request.GET.get('brand', '')

    # Fetch the correct model based on asset type
    asset_model = {
        'Laptop': Laptop,
        'Desktop': Desktop,
        'Printer': Printer,
        'iPad': iPad,
        'iPhone': iPhone,
        'Smartphone': Smartphone,
        'KeypadPhone': KeypadPhone,
        'Headset': Headset,
        'Keyboard': Keyboard,
        'Mouse': Mouse,
        'Pendrive': Pendrive,
        'HardDisk': HardDisk,
        'LanAdapter': LanAdapter,
        'SIM': SIM,
    }.get(asset_type, Laptop)

    # Check if the model has a brand field
    has_brand_field = hasattr(asset_model, 'brand')

    # Filter assets by brand if applicable and selected
    if has_brand_field and brand_filter:
        assets = asset_model.objects.filter(brand=brand_filter)
    else:
        assets = asset_model.objects.all()

    # Collect all unique brands for the filter dropdown if the asset type has a brand field
    brands = asset_model.objects.values_list('brand', flat=True).distinct() if has_brand_field else []

    # Paginate the results
    paginator = Paginator(assets, 5)  # Show 5 assets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'asset_type': asset_type,
        'brands': brands if has_brand_field else None,  # Only pass brands if available
        'selected_brand': brand_filter,
        'page_obj': page_obj,
    }
    return render(request, 'management/total_assets.html', context)


from django.shortcuts import render
from .models import Laptop, Desktop, Printer, iPhone, Smartphone, KeypadPhone, SIM  # Add other asset models
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Helper function to get assets by type

from django.shortcuts import render
from .models import Laptop, Desktop, Printer, iPhone, Smartphone, KeypadPhone, SIM, Headset, Keyboard, Mouse, Pendrive, HardDisk
    
from django.shortcuts import render
from .models import Laptop, Desktop, Printer, iPhone, Smartphone, KeypadPhone, SIM
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Laptop, Desktop, Printer, iPhone, Smartphone, KeypadPhone, SIM, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, iPad  # Add other asset models
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def free_assets(request):
    asset_type = request.GET.get('asset_type', 'Laptop')  # Default to Laptop
    assets = None

    # Fetch free assets based on asset_type
    if asset_type == 'Laptop':
        assets = Laptop.objects.filter(employee__isnull=True)
    elif asset_type == 'Desktop':
        assets = Desktop.objects.filter(employee__isnull=True)
    elif asset_type == 'Printer':
        assets = Printer.objects.filter(employee__isnull=True)
    elif asset_type == 'iPhone':
        assets = iPhone.objects.filter(employee__isnull=True)
    elif asset_type == 'Smartphone':
        assets = Smartphone.objects.filter(employee__isnull=True)
    elif asset_type == 'KeypadPhone':
        assets = KeypadPhone.objects.filter(employee__isnull=True)
    elif asset_type == 'SIM':
        assets = SIM.objects.filter(employee__isnull=True)
    elif asset_type == 'Headset':
        assets = Headset.objects.filter(employee__isnull=True)
    elif asset_type == 'Keyboard':
        assets = Keyboard.objects.filter(employee__isnull=True)
    elif asset_type == 'Mouse':
        assets = Mouse.objects.filter(employee__isnull=True)
    elif asset_type == 'Pendrive':
        assets = Pendrive.objects.filter(employee__isnull=True)
    elif asset_type == 'HardDisk':
        assets = HardDisk.objects.filter(employee__isnull=True)
    elif asset_type == 'LanAdapter':
        assets = LanAdapter.objects.filter(employee__isnull=True)
    elif asset_type == 'iPad':
        assets = iPad.objects.filter(employee__isnull=True)
    else:
        assets = Laptop.objects.none()  # If no valid asset type, return an empty queryset

    # Pagination
    paginator = Paginator(assets, 5)  # Show 5 assets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'asset_type': asset_type,
        'page_obj': page_obj,
    }
    return render(request, 'management/free_assets.html', context)
from django.shortcuts import render
from django.db.models import Q
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, Employee


from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop, Desktop, Smartphone, iPhone  # Import other relevant models
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM  # Import all relevant models
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, Employee  # Ensure Employee model is imported
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, Employee  # Ensure Employee model is imported
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import (
    Laptop, Desktop, Printer, iPad, iPhone, Smartphone, 
    KeypadPhone, Headset, Keyboard, Mouse, Pendrive, 
    HardDisk, LanAdapter, SIM, Employee
)
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM

def assign_asset_to_employee(request, asset_id):
    asset_type = request.GET.get('asset_type')
    if not asset_type:
        raise Http404("Asset type is missing")

    # Asset type mapping
    asset_model_mapping = {
        'Laptop': Laptop,
        'Desktop': Desktop,
        'Printer': Printer,
        'iPad': iPad,
        'iPhone': iPhone,
        'Smartphone': Smartphone,
        'KeypadPhone': KeypadPhone,
        'Headset': Headset,
        'Keyboard': Keyboard,
        'Mouse': Mouse,
        'Pendrive': Pendrive,
        'HardDisk': HardDisk,
        'LanAdapter': LanAdapter,
        'SIM': SIM,
    }

    # Fetch the correct asset model based on asset_type
    asset_model = asset_model_mapping.get(asset_type)
    if not asset_model:
        raise Http404(f"Asset type '{asset_type}' is not recognized.")

    # Get the asset object by its id
    asset = get_object_or_404(asset_model, id=asset_id)

    # Fetch all employees who are not exited
    employees = Employee.objects.filter(exited=False)

    # Apply search filter
    search_name = request.GET.get('search_name', '')
    department_filter = request.GET.get('department_filter', '')
    location_filter = request.GET.get('location_filter', '')

    if search_name:
        employees = employees.filter(name__icontains=search_name)

    if department_filter:
        employees = employees.filter(department=department_filter)

    if location_filter:
        employees = employees.filter(work_location=location_filter)

    # Pagination
    paginator = Paginator(employees, 30)  # 30 employees per page
    page_number = request.GET.get('page')
    employees_page = paginator.get_page(page_number)

    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)
        asset.employee = employee
        asset.save()
        return redirect('assigned_assets')

    # Pass asset_type and other relevant data to the template
    return render(request, 'management/assign_asset_to_employee.html', {
        'asset': asset,
        'employees': employees_page,
        'asset_type': asset_type,
        'search_name': search_name,
        'department_filter': department_filter,
        'location_filter': location_filter,
    })


from django.db.models import Q
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, Employee
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import csv
from django.core.paginator import Paginator
from django.contrib import messages

from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import csv
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, Employee

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.core.paginator import Paginator
import csv
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, Employee
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.core.paginator import Paginator
import csv
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, Employee
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, Employee

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, Employee
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, Employee

def assigned_assets(request):
    # Gather all assigned assets from each asset model
    asset_lists = [
        (Laptop.objects.filter(employee__isnull=False), 'Laptop'),
        (Desktop.objects.filter(employee__isnull=False), 'Desktop'),
        (Printer.objects.filter(employee__isnull=False), 'Printer'),
        (iPad.objects.filter(employee__isnull=False), 'iPad'),
        (iPhone.objects.filter(employee__isnull=False), 'iPhone'),
        (Smartphone.objects.filter(employee__isnull=False), 'Smartphone'),
        (KeypadPhone.objects.filter(employee__isnull=False), 'KeypadPhone'),
        (Headset.objects.filter(employee__isnull=False), 'Headset'),
        (Keyboard.objects.filter(employee__isnull=False), 'Keyboard'),
        (Mouse.objects.filter(employee__isnull=False), 'Mouse'),
        (Pendrive.objects.filter(employee__isnull=False), 'Pendrive'),
        (HardDisk.objects.filter(employee__isnull=False), 'HardDisk'),
        (LanAdapter.objects.filter(employee__isnull=False), 'LanAdapter'),
        (SIM.objects.filter(employee__isnull=False), 'SIM'),
    ]

    # Combine all asset querysets into a single list with asset type included
    assets = []
    for asset_list, asset_type in asset_lists:
        for asset in asset_list:
            asset.asset_type = asset_type  # Add asset type dynamically
            assets.append(asset)

    # Pagination setup (show 10 assets per page)
    paginator = Paginator(assets, 10)  # Show 10 assets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'management/assigned_assets.html', {
        'assets': page_obj,
        'departments': Employee.objects.values_list('department', flat=True).distinct(),
        'asset_types': ['Laptop', 'Desktop', 'Printer', 'iPad', 'iPhone', 'Smartphone', 'KeypadPhone', 'Headset', 'Keyboard', 'Mouse', 'Pendrive', 'HardDisk', 'LanAdapter', 'SIM'],
    })


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Employee, Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM

# Search for employees by name or ID
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Employee, Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM

def search_employee(request):
    query = request.GET.get('query', '')
    if query:
        employees = Employee.objects.filter(name__icontains=query) | Employee.objects.filter(employee_id__icontains=query)
        results = [{'id': emp.id, 'name': emp.name, 'employee_id': emp.employee_id} for emp in employees]
        return JsonResponse({'results': results})
    return JsonResponse({'results': []})

from django.core.paginator import Paginator

def assigned_employee_assets(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    assets = []

    asset_models = [Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM]
    for model in asset_models:
        assigned_assets = model.objects.filter(employee=employee)
        for asset in assigned_assets:
            assets.append({
                'asset_type': model.__name__,
                'serial_number': asset.serial_number,
                'brand': asset.brand,
                'date_of_purchase': asset.date_of_purchase,
                'warranty_date': asset.warranty_date,
                'status': asset.status,
            })

    # Add pagination
    paginator = Paginator(assets, 5)  # Show 5 assets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'management/assigned_employee_assets.html', {
        'employee': employee,
        'page_obj': page_obj,
    })

def export_assigned_assets_csv(assets):
    # Prepare CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="assigned_assets.csv"'

    writer = csv.writer(response)
    writer.writerow(['Asset Type', 'Serial Number', 'Brand', 'Employee Name', 'Department'])

    for asset in assets:
        writer.writerow([asset.__class__.__name__, asset.serial_number, asset.brand, asset.employee.name, asset.employee.department])

    return response


def unassign_asset(request, asset_id, asset_type):
    # Based on asset type, get the correct model
    asset_model_map = {
        'Laptop': Laptop,
        'Desktop': Desktop,
        'Printer': Printer,
        'iPad': iPad,
        'iPhone': iPhone,
        'Smartphone': Smartphone,
        'KeypadPhone': KeypadPhone,
        'Headset': Headset,
        'Keyboard': Keyboard,
        'Mouse': Mouse,
        'Pendrive': Pendrive,
        'HardDisk': HardDisk,
        'LanAdapter': LanAdapter,
        'SIM': SIM,
    }

    model = asset_model_map.get(asset_type)

    if model:
        asset = get_object_or_404(model, id=asset_id)

        # Confirmation message for unassignment
        if request.method == "POST":
            asset.employee = None  # Unassign the asset
            asset.save()
            return redirect('assigned_assets')

        return render(request, 'management/confirm_unassign.html', {'asset': asset})
    else:
        raise Http404(f"Invalid asset type: {asset_type}")


def export_assigned_assets_csv(assets):
    # Prepare CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="assigned_assets.csv"'

    writer = csv.writer(response)
    writer.writerow(['Asset Type', 'Serial Number', 'Brand', 'Employee Name', 'Department'])

    for asset in assets:
        writer.writerow([asset.__class__.__name__, asset.serial_number, asset.brand, asset.employee.name, asset.employee.department])

    return response


def unassign_asset(request, asset_id, asset_type):
    # Based on asset type, get the correct model
    asset_model_map = {
        'Laptop': Laptop,
        'Desktop': Desktop,
        'Printer': Printer,
        'iPad': iPad,
        'iPhone': iPhone,
        'Smartphone': Smartphone,
        'KeypadPhone': KeypadPhone,
        'Headset': Headset,
        'Keyboard': Keyboard,
        'Mouse': Mouse,
        'Pendrive': Pendrive,
        'HardDisk': HardDisk,
        'LanAdapter': LanAdapter,
        'SIM': SIM,
    }

    model = asset_model_map.get(asset_type)

    if model:
        asset = get_object_or_404(model, id=asset_id)

        # Confirmation message for unassignment
        if request.method == "POST":
            asset.employee = None  # Unassign the asset
            asset.save()
            return redirect('assigned_assets')

        return render(request, 'management/confirm_unassign.html', {'asset': asset})
    else:
        raise Http404(f"Invalid asset type: {asset_type}")

# Helper function to get assets by type
def get_assets_by_type(asset_type):
    if asset_type == 'Laptop':
        return Laptop.objects.all()
    elif asset_type == 'Desktop':
        return Desktop.objects.all()
    elif asset_type == 'Printer':
        return Printer.objects.all()
    elif asset_type == 'iPad':
        return iPad.objects.all()
    elif asset_type == 'iPhone':
        return iPhone.objects.all()
    elif asset_type == 'Smartphone':
        return Smartphone.objects.all()
    elif asset_type == 'KeypadPhone':
        return KeypadPhone.objects.all()
    elif asset_type == 'Headset':
        return Headset.objects.all()
    elif asset_type == 'Keyboard':
        return Keyboard.objects.all()
    elif asset_type == 'Mouse':
        return Mouse.objects.all()
    elif asset_type == 'Pendrive':
        return Pendrive.objects.all()
    elif asset_type == 'HardDisk':
        return HardDisk.objects.all()
    elif asset_type == 'LanAdapter':
        return LanAdapter.objects.all()
    elif asset_type == 'SIM':
        return SIM.objects.all()
    else:
        return Laptop.objects.all()  # Default to Laptop


###################################################################################################################
#####################################################################################################################
########################################################################################################################
#######################################################################################################################



# Finance Management and Report Views
@login_required
def finance_management(request):
    return render(request, 'management/finance_management.html')


def report(request):
    employees = Employee.objects.all()

    DEVICE_MODELS = {
        'Laptop': Laptop,
        'Desktop': Desktop,
        'Printer': Printer,
        'iPad': iPad,
        'iPhone': iPhone,
        'Smartphone': Smartphone,
        'KeypadPhone': KeypadPhone,
        'Headset': Headset,
        'Keyboard': Keyboard,
        'Mouse': Mouse,
        'Pendrive': Pendrive,
        'HardDisk': HardDisk,
        'LanAdapter': LanAdapter,
        'SIM': SIM,
        'RentalAsset': RentalAsset,
    }

    # Data for employees: active and exited
    departments = employees.values_list('department', flat=True)
    department_counts = Counter(departments)

    active_employees = employees.filter(exited=False)
    exited_employees = employees.filter(exited=True)

    active_department_counts = Counter(active_employees.values_list('department', flat=True))
    exited_department_counts = Counter(exited_employees.values_list('department', flat=True))

    department_labels = list(department_counts.keys())
    active_values = [active_department_counts.get(dept, 0) for dept in department_labels]
    exited_values = [exited_department_counts.get(dept, 0) for dept in department_labels]

    # Exited employees count for donut chart
    total_exited = exited_employees.count()
    exited_per_department = [exited_department_counts.get(dept, 0) for dept in department_labels]

    # Fetch total assets data
    total_assets = {
        asset_type: model.objects.count() for asset_type, model in DEVICE_MODELS.items()
    }

    total_assets_labels = list(total_assets.keys())
    total_assets_values = list(total_assets.values())

    # Fetch free (unassigned) assets data
    free_assets = {
        asset_type: model.objects.filter(employee__isnull=True).count() for asset_type, model in DEVICE_MODELS.items()
    }

    free_assets_labels = list(free_assets.keys())
    free_assets_values = list(free_assets.values())

    # Fetch assigned assets data
    assigned_assets_counts = Counter()
    for asset_type, model in DEVICE_MODELS.items():
        assigned_assets_queryset = model.objects.filter(employee__isnull=False)
        assigned_assets_counts[asset_type] = assigned_assets_queryset.count()

    assigned_assets_labels = list(assigned_assets_counts.keys())
    assigned_assets_values = list(assigned_assets_counts.values())

    # Calculate the sums of the assets
    total_assets_sum = sum(total_assets_values)
    free_assets_sum = sum(free_assets_values)
    assigned_assets_sum = sum(assigned_assets_values)

    return render(request, 'management/report.html', {
        'employees': employees,
        'exited_employees': exited_employees,  # For exited employee table
        'department_labels': department_labels,
        'active_values': active_values,
        'exited_values': exited_values,
        'exited_per_department': exited_per_department,  # Data for donut chart
        'total_exited': total_exited,  # Total exited employees for display
        'total_assets': total_assets,  # Total assets data for display
        'total_assets_labels': total_assets_labels,  # Labels for total assets donut chart
        'total_assets_values': total_assets_values,  # Values for total assets donut chart
        'free_assets': free_assets,  # Free (unassigned) assets data
        'free_assets_labels': free_assets_labels,  # Labels for free assets donut chart
        'free_assets_values': free_assets_values,  # Values for free assets donut chart
        'assigned_assets_labels': assigned_assets_labels,  # Labels for assigned assets donut chart
        'assigned_assets_values': assigned_assets_values,  # Assigned asset counts for chart
        'total_assets_sum': total_assets_sum,  # Total assets count
        'free_assets_sum': free_assets_sum,  # Free assets count
        'assigned_assets_sum': assigned_assets_sum,  # Assigned assets count
    })

from .models import Invoice

import csv
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import Invoice
from .forms import InvoiceForm
from datetime import datetime
from django.conf import settings
from django.core.files.base import ContentFile, File
from django.core.paginator import Paginator

@login_required
def finance_module(request):
    total_amount = Invoice.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    total_paid_amount = Invoice.objects.filter(status='Paid').aggregate(total_paid_amount=Sum('amount'))['total_paid_amount'] or 0
    pending_amount = calculate_pending_amount()
    overdue_amount = calculate_overdue_amount()
    context = {
        'total_amount': total_amount,
        'total_paid_amount': total_paid_amount,
        'pending_amount': pending_amount,
        'overdue_amount': overdue_amount,
    }
    return render(request, 'management/finance_module.html', context)

def calculate_pending_amount():
    return Invoice.objects.filter(status='Pending').aggregate(total_amount=Sum('amount'))['total_amount'] or 0

def calculate_overdue_amount():
    return Invoice.objects.filter(status='Overdue').aggregate(total_amount=Sum('amount'))['total_amount'] or 0

def invoice_list(request):
    invoices = Invoice.objects.all().order_by('id')

    purchase_date_from = request.GET.get('purchase_date_from')
    purchase_date_to = request.GET.get('purchase_date_to')
    invoice_number = request.GET.get('invoice_number')
    vendor = request.GET.get('vendor')
    department = request.GET.get('department')
    status = request.GET.get('status')

    if purchase_date_from and purchase_date_from != 'None':
        invoices = invoices.filter(purchase_date__gte=purchase_date_from)
    if purchase_date_to and purchase_date_to != 'None':
        invoices = invoices.filter(purchase_date__lte=purchase_date_to)
    if invoice_number and invoice_number != 'None':
        invoices = invoices.filter(invoice_number__icontains=invoice_number)
    if vendor and vendor != 'None':
        invoices = invoices.filter(vendor__icontains=vendor)
    if department and department != 'None':
        invoices = invoices.filter(department__icontains=department)
    if status and status != 'None':
        invoices = invoices.filter(status__iexact=status)

    paginator = Paginator(invoices, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'purchase_date_from': purchase_date_from,
        'purchase_date_to': purchase_date_to,
        'invoice_number': invoice_number,
        'vendor': vendor,
        'department': department,
        'status': status,  # Make sure to add this line
    }
    return render(request, 'management/invoice_list.html', context)

def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            invoice = form.save()
            return JsonResponse({'success': True, 'amount': invoice.amount, 'status': invoice.status})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = InvoiceForm()
    return render(request, 'management/add_invoice.html', {'form': form})

def edit_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'management/edit_invoice.html', {'form': form})

def bulk_upload(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a CSV file.')
            return redirect('invoice_list')

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        date_formats = ['%Y-%m-%d', '%d-%m-%Y']

        for row in reader:
            try:
                for date_field in ['requested_date', 'purchase_date', 'next_payment_date']:
                    for fmt in date_formats:
                        try:
                            row[date_field] = datetime.strptime(row[date_field], fmt).date()
                            break
                        except ValueError:
                            continue
                    else:
                        messages.error(request, f'Invalid date format for {date_field} in row: {row}')
                        return redirect('invoice_list')

                invoice_file_path = row.get('invoice_file')
                invoice_file = None

                if invoice_file_path:
                    if os.path.exists(invoice_file_path):
                        with open(invoice_file_path, 'rb') as f:
                            file_content = ContentFile(f.read())
                            invoice_file_name = os.path.basename(invoice_file_path)
                            invoice_file = File(file_content, name=invoice_file_name)
                            invoice_file_path = os.path.join('invoices', invoice_file_name)
                            with open(os.path.join(settings.MEDIA_ROOT, invoice_file_path), 'wb') as destination:
                                for chunk in file_content.chunks():
                                    destination.write(chunk)
                    else:
                        messages.error(request, f'File {invoice_file_path} does not exist.')
                        return redirect('invoice_list')

                Invoice.objects.create(
                    requested_date=row['requested_date'],
                    purchase_date=row['purchase_date'],
                    vendor=row['vendor'],
                    product=row['product'],
                    quantity=int(row['quantity']),
                    payment_method=row['payment_method'],
                    payment_type=row['payment_type'] if row['payment_type'] else None,
                    amount=float(row['amount']),
                    status=row['status'],
                    reference_transaction_id=row['reference_transaction_id'],
                    invoice_number=row['invoice_number'],
                    next_payment_date=row['next_payment_date'],
                    department=row['department'],
                    invoice_file=invoice_file_path
                )
            except Exception as e:
                messages.error(request, f'Error in row {row}: {e}')
                return redirect('invoice_list')

        messages.success(request, 'Invoices uploaded successfully.')
        return redirect('invoice_list')

    return render(request, 'bulk_upload.html')

def export_invoices(request):
    if request.method == 'POST':
        selected_invoice_ids = request.POST.get('selected_invoice_ids', '')
        invoice_ids = selected_invoice_ids.split(',') if selected_invoice_ids else []

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="invoices.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Requested Date', 'Purchase Date', 'Vendor', 'Product', 'Quantity', 'Payment Method',
            'Payment Type', 'Amount', 'Status', 'Reference/Transaction ID', 'Invoice Number',
            'Next Payment Date', 'Department', 'Invoice File'
        ])

        invoices = Invoice.objects.filter(id__in=invoice_ids)

        for invoice in invoices.values_list(
            'requested_date', 'purchase_date', 'vendor', 'product', 'quantity', 'payment_method',
            'payment_type', 'amount', 'status', 'reference_transaction_id', 'invoice_number',
            'next_payment_date', 'department', 'invoice_file'
        ):
            writer.writerow(invoice)

        return response

def delete_invoices(request):
    if request.method == 'POST':
        invoice_ids = request.POST.get('invoice_ids')
        invoice_ids = invoice_ids.split(',')
        invoices = Invoice.objects.filter(pk__in=invoice_ids)
        invoices.delete()
        messages.success(request, 'Selected invoices deleted successfully.')
        return redirect('invoice_list')

def settings(request):
    return render(request, 'management/settings.html')







    DEVICE_MODELS = {
        'Laptop': Laptop,
        'Desktop': Desktop,
        'Printer': Printer,
        'iPad': iPad,
        'iPhone': iPhone,
        'Smartphone': Smartphone,
        'KeypadPhone': KeypadPhone,
        'Headset': Headset,
        'Keyboard': Keyboard,
        'Mouse': Mouse,
        'Pendrive': Pendrive,
        'HardDisk': HardDisk,
        'LanAdapter': LanAdapter,
        'SIM': SIM,
        'RentalAsset': RentalAsset,
    }

    # Data for employees: active and exited
    departments = employees.values_list('department', flat=True)
    department_counts = Counter(departments)

    active_employees = employees.filter(exited=False)
    exited_employees = employees.filter(exited=True)

    active_department_counts = Counter(active_employees.values_list('department', flat=True))
    exited_department_counts = Counter(exited_employees.values_list('department', flat=True))

    department_labels = list(department_counts.keys())
    active_values = [active_department_counts.get(dept, 0) for dept in department_labels]
    exited_values = [exited_department_counts.get(dept, 0) for dept in department_labels]

    # Exited employees count for donut chart
    total_exited = exited_employees.count()
    exited_per_department = [exited_department_counts.get(dept, 0) for dept in department_labels]

    # Fetch total assets data
    total_assets = {
        asset_type: model.objects.count() for asset_type, model in DEVICE_MODELS.items()
    }

    total_assets_labels = list(total_assets.keys())
    total_assets_values = list(total_assets.values())

    # Fetch free (unassigned) assets data
    free_assets = {
        asset_type: model.objects.filter(employee__isnull=True).count() for asset_type, model in DEVICE_MODELS.items()
    }

    free_assets_labels = list(free_assets.keys())
    free_assets_values = list(free_assets.values())

    # Fetch assigned assets data
    assigned_assets_counts = Counter()
    for asset_type, model in DEVICE_MODELS.items():
        assigned_assets_queryset = model.objects.filter(employee__isnull=False)
        assigned_assets_counts[asset_type] = assigned_assets_queryset.count()

    assigned_assets_labels = list(assigned_assets_counts.keys())
    assigned_assets_values = list(assigned_assets_counts.values())

    # Calculate the sums of the assets
    total_assets_sum = sum(total_assets_values)
    free_assets_sum = sum(free_assets_values)
    assigned_assets_sum = sum(assigned_assets_values)

    return render(request, 'management/report.html', {
        'employees': employees,
        'exited_employees': exited_employees,  # For exited employee table
        'department_labels': department_labels,
        'active_values': active_values,
        'exited_values': exited_values,
        'exited_per_department': exited_per_department,  # Data for donut chart
        'total_exited': total_exited,  # Total exited employees for display
        'total_assets': total_assets,  # Total assets data for display
        'total_assets_labels': total_assets_labels,  # Labels for total assets donut chart
        'total_assets_values': total_assets_values,  # Values for total assets donut chart
        'free_assets': free_assets,  # Free (unassigned) assets data
        'free_assets_labels': free_assets_labels,  # Labels for free assets donut chart
        'free_assets_values': free_assets_values,  # Values for free assets donut chart
        'assigned_assets_labels': assigned_assets_labels,  # Labels for assigned assets donut chart
        'assigned_assets_values': assigned_assets_values,  # Assigned asset counts for chart
        'total_assets_sum': total_assets_sum,  # Total assets count
        'free_assets_sum': free_assets_sum,  # Free assets count
        'assigned_assets_sum': assigned_assets_sum,  # Assigned assets count
    })


import csv
from django.http import HttpResponse
from collections import Counter
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Employee, Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, RentalAsset

# Helper function to export data to CSV
def export_to_csv(data, filename, fieldnames):
    """Helper function to export any data to CSV."""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

    writer = csv.DictWriter(response, fieldnames=fieldnames)
    writer.writeheader()

    # For each item in data, write a row in the CSV
    for row in data:
        writer.writerow(row)

    return response

# Main report view
def report(request):
    employees = Employee.objects.all()
    exited_employees = employees.filter(exited=True)

    DEVICE_MODELS = {
        'Laptop': Laptop,
        'Desktop': Desktop,
        'Printer': Printer,
        'iPad': iPad,
        'iPhone': iPhone,
        'Smartphone': Smartphone,
        'KeypadPhone': KeypadPhone,
        'Headset': Headset,
        'Keyboard': Keyboard,
        'Mouse': Mouse,
        'Pendrive': Pendrive,
        'HardDisk': HardDisk,
        'LanAdapter': LanAdapter,
        'SIM': SIM,
        'RentalAsset': RentalAsset,
    }

    # Handle export requests
    export_type = request.GET.get('export')
    
    # Export Employees
    if export_type == 'employees':
        fieldnames = ['employee_id', 'name', 'department', 'designation', 'branch', 'work_location', 'reporting_officer', 'personal_email_id', 'date_of_joining']
        return export_to_csv(employees.values(*fieldnames), 'employees', fieldnames)
    
    # Export Exited Employees
    elif export_type == 'exited_employees':
        fieldnames = ['employee_id', 'name', 'department', 'designation', 'branch', 'work_location', 'reporting_officer', 'personal_email_id']
        # Check if 'exit_date' or 'date_of_exit' exists and append accordingly
        if hasattr(Employee, 'exit_date'):
            fieldnames.append('exit_date')
        elif hasattr(Employee, 'date_of_exit'):
            fieldnames.append('date_of_exit')
        return export_to_csv(exited_employees.values(*fieldnames), 'exited_employees', fieldnames)

    # Export Total Assets
    elif export_type == 'total_assets':
        total_assets = {asset_type: model.objects.count() for asset_type, model in DEVICE_MODELS.items()}
        fieldnames = ['asset_type', 'total_count']
        asset_rows = [{'asset_type': asset_type, 'total_count': count} for asset_type, count in total_assets.items()]
        return export_to_csv(asset_rows, 'total_assets', fieldnames)

    # Export Free Assets
    elif export_type == 'free_assets':
        free_assets = {asset_type: model.objects.filter(employee__isnull=True).count() for asset_type, model in DEVICE_MODELS.items()}
        fieldnames = ['asset_type', 'free_count']
        asset_rows = [{'asset_type': asset_type, 'free_count': count} for asset_type, count in free_assets.items()]
        return export_to_csv(asset_rows, 'free_assets', fieldnames)

    # Export Assigned Assets
    elif export_type == 'assigned_assets':
        assigned_assets = {asset_type: model.objects.filter(employee__isnull=False).count() for asset_type, model in DEVICE_MODELS.items()}
        fieldnames = ['asset_type', 'assigned_count']
        asset_rows = [{'asset_type': asset_type, 'assigned_count': count} for asset_type, count in assigned_assets.items()]
        return export_to_csv(asset_rows, 'assigned_assets', fieldnames)

    # Pagination setup for employees and exited employees
    employee_paginator = Paginator(employees, 50)  # Show 50 employees per page
    exited_employee_paginator = Paginator(exited_employees, 50)  # Show 50 exited employees per page

    page_number = request.GET.get('page', 1)
    employees_page_obj = employee_paginator.get_page(page_number)
    exited_employees_page_obj = exited_employee_paginator.get_page(page_number)

    # Data for employees: active and exited
    departments = employees.values_list('department', flat=True)
    department_counts = Counter(departments)

    active_employees = employees.filter(exited=False)
    active_department_counts = Counter(active_employees.values_list('department', flat=True))
    exited_department_counts = Counter(exited_employees.values_list('department', flat=True))

    department_labels = list(department_counts.keys())
    active_values = [active_department_counts.get(dept, 0) for dept in department_labels]
    exited_values = [exited_department_counts.get(dept, 0) for dept in department_labels]

    # Exited employees count for donut chart
    total_exited = exited_employees.count()
    exited_per_department = [exited_department_counts.get(dept, 0) for dept in department_labels]

    # Fetch total assets data
    total_assets = {
        asset_type: model.objects.count() for asset_type, model in DEVICE_MODELS.items()
    }

    total_assets_labels = list(total_assets.keys())
    total_assets_values = list(total_assets.values())

    # Fetch free (unassigned) assets data
    free_assets = {
        asset_type: model.objects.filter(employee__isnull=True).count() for asset_type, model in DEVICE_MODELS.items()
    }

    free_assets_labels = list(free_assets.keys())
    free_assets_values = list(free_assets.values())

    # Fetch assigned assets data
    assigned_assets_counts = Counter()
    for asset_type, model in DEVICE_MODELS.items():
        assigned_assets_queryset = model.objects.filter(employee__isnull=False)
        assigned_assets_counts[asset_type] = assigned_assets_queryset.count()

    assigned_assets_labels = list(assigned_assets_counts.keys())
    assigned_assets_values = list(assigned_assets_counts.values())

    # Calculate the sums of the assets
    total_assets_sum = sum(total_assets_values)
    free_assets_sum = sum(free_assets_values)
    assigned_assets_sum = sum(assigned_assets_values)

    return render(request, 'management/report.html', {
        'employees_page_obj': employees_page_obj,  # For paginated employee list
        'exited_employees_page_obj': exited_employees_page_obj,  # For paginated exited employees
        'department_labels': department_labels,
        'active_values': active_values,
        'exited_values': exited_values,
        'exited_per_department': exited_per_department,  # Data for donut chart
        'total_exited': total_exited,  # Total exited employees for display
        'total_assets': total_assets,  # Total assets data for display
        'total_assets_labels': total_assets_labels,  # Labels for total assets donut chart
        'total_assets_values': total_assets_values,  # Values for total assets donut chart
        'free_assets': free_assets,  # Free (unassigned) assets data
        'free_assets_labels': free_assets_labels,  # Labels for free assets donut chart
        'free_assets_values': free_assets_values,  # Values for free assets donut chart
        'assigned_assets_labels': assigned_assets_labels,  # Labels for assigned assets donut chart
        'assigned_assets_values': assigned_assets_values,  # Assigned asset counts for chart
        'total_assets_sum': total_assets_sum,  # Total assets count
        'free_assets_sum': free_assets_sum,  # Free assets count
        'assigned_assets_sum': assigned_assets_sum,  # Assigned assets count
    })
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))  # Redirect to the login page after logout
