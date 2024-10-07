from django import forms
from django.contrib.auth.models import User
from .models import Employee, Laptop, Desktop, Printer, iPad, iPhone, Smartphone, KeypadPhone, Headset, Keyboard, Mouse, Pendrive, HardDisk, LanAdapter, SIM, RentalAsset, Invoice
from datetime import datetime
from django.core.exceptions import ValidationError

# Custom Date Input to handle different date formats
class CustomDateInput(forms.DateInput):
    def __init__(self, **kwargs):
        kwargs['format'] = '%d-%m-%Y'  # Default format for display
        super().__init__(**kwargs)

    def to_python(self, value):
        if not value:
            return None
        date_formats = ['%d-%m-%Y', '%d/%m/%Y', '%m/%d/%Y']
        for fmt in date_formats:
            try:
                return datetime.strptime(value, fmt).date()
            except ValueError:
                continue
        raise ValidationError('Enter a valid date in DD-MM-YYYY, DD/MM/YYYY, or MM/DD/YYYY')

# User Form with password widget
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'})
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

# Employee Form with widgets
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'date_of_joining', 'employee_id', 'name', 'department',
            'designation', 'branch', 'work_location', 'reporting_officer',
            'personal_email_id'
        ]
        widgets = {
            'date_of_joining': forms.DateInput(attrs={
                'class': 'form-control', 'placeholder': 'dd-mm-yyyy', 'type': 'date'
            }),
            'employee_id': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Employee ID', 'value': 'LA-IND-'
            }),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Designation'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'work_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Work Location'}),
            'reporting_officer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Reporting Officer'}),
            'personal_email_id': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['employee_id'].widget.attrs['readonly'] = True
        else:
            self.fields['employee_id'].initial = 'LA-IND-'

# Laptop Form with widgets
class LaptopForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = Laptop
        fields = [
            'serial_number', 'brand', 'processor', 'ram_capacity',
            'storage', 'inch', 'status', 'building_name',
            'date_of_purchase', 'purchased_amount', 'warranty_details',
            'warranty_date', 'remarks'
        ]
        widgets = {
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'processor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Processor'}),
            'ram_capacity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter RAM Capacity'}),
            'storage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Storage'}),
            'inch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Inch'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'building_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Building Name'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# Desktop Form with widgets
class DesktopForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = Desktop
        fields = [
            'serial_number', 'brand', 'processor', 'ram_capacity',
            'storage', 'inch', 'status', 'building_name',
            'date_of_purchase', 'purchased_amount', 'warranty_details',
            'warranty_date', 'remarks'
        ]
        widgets = {
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'processor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Processor'}),
            'ram_capacity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter RAM Capacity'}),
            'storage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Storage'}),
            'inch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Inch'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'building_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Building Name'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# Printer Form with widgets
class PrinterForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = Printer
        fields = [
            'serial_number', 'brand', 'model', 'status', 'building_name',
            'date_of_purchase', 'purchased_amount', 'warranty_details',
            'warranty_date', 'remarks'
        ]
        widgets = {
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Model'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'building_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Building Name'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# iPad Form with widgets
class iPadForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = iPad
        fields = [
            'serial_number', 'brand', 'processor', 'ram_capacity',
            'storage', 'inch', 'status', 'building_name',
            'date_of_purchase', 'purchased_amount', 'warranty_details',
            'warranty_date', 'remarks'
        ]
        widgets = {
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'processor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Processor'}),
            'ram_capacity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter RAM Capacity'}),
            'storage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Storage'}),
            'inch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Inch'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'building_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Building Name'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# iPhone Form with widgets
class iPhoneForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = iPhone
        fields = [
            'serial_number', 'mobile', 'imei_no1', 'imei_no2', 'mobile_status',
            'charger', 'date_of_purchase', 'purchased_amount', 'warranty_details',
            'warranty_date', 'remarks'
        ]
        widgets = {
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile'}),
            'imei_no1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter IMEI No1'}),
            'imei_no2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter IMEI No2'}),
            'mobile_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Status'}),
            'charger': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# Smartphone Form with widgets
class SmartphoneForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = Smartphone
        fields = [
            'serial_number', 'mobile', 'imei_no1', 'imei_no2', 'mobile_status',
            'charger', 'date_of_purchase', 'purchased_amount', 'warranty_details',
            'warranty_date', 'remarks'
        ]
        widgets = {
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile'}),
            'imei_no1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter IMEI No1'}),
            'imei_no2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter IMEI No2'}),
            'mobile_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Status'}),
            'charger': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# Keypad Phone Form with widgets
class KeypadPhoneForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = KeypadPhone
        fields = [
            'serial_number', 'mobile', 'imei_no1', 'imei_no2', 'mobile_status',
            'charger', 'date_of_purchase', 'purchased_amount', 'warranty_details',
            'warranty_date', 'remarks'
        ]
        widgets = {
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile'}),
            'imei_no1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter IMEI No1'}),
            'imei_no2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter IMEI No2'}),
            'mobile_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Status'}),
            'charger': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# Headset Form with widgets
class HeadsetForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = Headset
        fields = [
            'date_of_purchase', 'brand', 'serial_number', 'headset_status',
            'remarks', 'warranty_details', 'warranty_date', 'purchased_amount'
        ]
        widgets = {
            'date_of_purchase': CustomDateInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'headset_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# Keyboard Form with widgets
class KeyboardForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = Keyboard
        fields = [
            'date_of_purchase', 'brand', 'serial_number', 'keyboard_status',
            'remarks', 'warranty_details', 'warranty_date', 'purchased_amount'
        ]
        widgets = {
            'date_of_purchase': CustomDateInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'keyboard_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# Mouse Form with widgets
class MouseForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = Mouse
        fields = [
            'date_of_purchase', 'brand', 'serial_number', 'mouse_status',
            'remarks', 'warranty_details', 'warranty_date', 'purchased_amount'
        ]
        widgets = {
            'date_of_purchase': CustomDateInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'mouse_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# Pendrive Form with widgets
class PendriveForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = Pendrive
        fields = [
            'date_of_purchase', 'brand', 'serial_number', 'pendrive_status',
            'storage', 'remarks', 'warranty_details', 'warranty_date', 'purchased_amount'
        ]
        widgets = {
            'date_of_purchase': CustomDateInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'pendrive_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'storage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Storage'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# HardDisk Form with widgets
class HardDiskForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = HardDisk
        fields = [
            'date_of_purchase', 'brand', 'serial_number', 'hard_disk_status',
            'storage', 'remarks', 'warranty_details', 'warranty_date', 'purchased_amount'
        ]
        widgets = {
            'date_of_purchase': CustomDateInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'hard_disk_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'storage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Storage'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# LanAdapter Form with widgets
class LanAdapterForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())
    warranty_date = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = LanAdapter
        fields = [
            'date_of_purchase', 'brand', 'serial_number', 'lan_adapter_status',
            'remarks', 'warranty_details', 'warranty_date', 'purchased_amount'
        ]
        widgets = {
            'date_of_purchase': CustomDateInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'lan_adapter_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'purchased_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Purchased Amount'}),
            'warranty_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Warranty Details'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# SIM Form with widgets
class SIMForm(forms.ModelForm):
    class Meta:
        model = SIM
        fields = [
            'sim_number', 'sim_connection', 'sim_status',
            'availability', 'remarks'
        ]
        widgets = {
            'sim_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter SIM Number'}),
            'sim_connection': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter SIM Connection'}),
            'sim_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter SIM Status'}),
            'availability': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Availability'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# Rental Asset Form with widgets
class RentalAssetForm(forms.ModelForm):
    date_of_purchase = forms.DateField(widget=CustomDateInput())

    class Meta:
        model = RentalAsset
        fields = [
            'serial_number', 'rental_laptop_brand', 'processor',
            'ram_capacity', 'storage', 'inch', 'laptop_status',
            'building_name', 'date_of_purchase', 'remarks'
        ]
        widgets = {
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'rental_laptop_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Laptop Brand'}),
            'processor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Processor'}),
            'ram_capacity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter RAM Capacity'}),
            'storage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Storage'}),
            'inch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Inch'}),
            'laptop_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'building_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Building Name'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Remarks'}),
        }

# Invoice Form with widgets
class InvoiceForm(forms.ModelForm):
    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cash', 'Cash'),
    ]
    
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Overdue', 'Overdue'),
    ]
    
    PAYMENT_TYPE_CHOICES = [
        ('One Time Payment', 'One Time Payment'),
        ('Quarterly Payment', 'Quarterly Payment'),
        ('Half Yearly Payment', 'Half Yearly Payment'),
        ('Yearly Payment', 'Yearly Payment'),
    ]

    requested_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    purchase_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    payment_type = forms.ChoiceField(choices=PAYMENT_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    next_payment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    invoice_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Invoice Number'}))
    invoice_file = forms.FileField(required=False)

    class Meta:
        model = Invoice
        fields = [
            'requested_date', 'purchase_date', 'vendor', 'product','quantity', 'payment_method',
            'payment_type', 'amount', 'status', 'reference_transaction_id', 'invoice_number',
            'next_payment_date', 'department', 'invoice_file'
        ]
        widgets = {
            'vendor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Vendor'}),
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quantity'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'reference_transaction_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Transaction ID'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department'}),
        }

# Bulk Upload Form with widgets
class BulkUploadForm(forms.Form):
    csv_file = forms.FileField()

# Invoice Filter Form with widgets
class InvoiceFilterForm(forms.Form):
    purchase_date_from = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    purchase_date_to = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    invoice_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Invoice Number'}))
    vendor = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Vendor Name'}))
    department = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department Name'}))
