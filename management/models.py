from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('FINANCE', 'FINANCE'),
        ('RM FINANCE', 'RM FINANCE'),
        ('RM', 'RM'),
        ('ACADAMICS', 'ACADAMICS'),
        ('CC', 'CC'),
        ('ONLINE OPERATIONS', 'ONLINE OPERATIONS'),
        ('ADMIN', 'ADMIN'),
    ]

    BRANCH_CHOICES = [
        ('kannur', 'Kannur'),
        ('calicut', 'Calicut'),
        ('thrissur', 'Thrissur'),
        ('kochi', 'Kochi'),
        ('kottayam', 'Kottayam'),
        ('trivandrum', 'Trivandrum'),
    ]

    date_of_joining = models.DateField()
    employee_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    designation = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES)
    work_location = models.CharField(max_length=100)
    reporting_officer = models.CharField(max_length=100)
    personal_email_id = models.EmailField()
    exited = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Ensure the employee_id starts with 'LA-IND-'
        if not self.employee_id.startswith('LA-IND-'):
            self.employee_id = f'LA-IND-{self.employee_id}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"



class Laptop(models.Model):
    serial_number = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram_capacity = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    inch = models.DecimalField(max_digits=4, decimal_places=1)
    status = models.CharField(max_length=50)
    building_name = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_details = models.CharField(max_length=100)
    warranty_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='laptops')

    def __str__(self):
        return f"{self.brand} - {self.serial_number}"

class Desktop(models.Model):
    serial_number = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram_capacity = models.CharField(max_length=50)
    storage = models.CharField(max_length=100)
    inch = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    building_name = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='desktops')

    def __str__(self):
        return f"{self.brand} - {self.serial_number}"

class Printer(models.Model):
    serial_number = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    building_name = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='printers')

    def __str__(self):
        return f"{self.brand} - {self.model} ({self.serial_number})"

class iPad(models.Model):
    serial_number = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram_capacity = models.CharField(max_length=50)
    storage = models.CharField(max_length=100)
    inch = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    building_name = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='ipads')

    def __str__(self):
        return f"{self.brand} - {self.serial_number}"

class iPhone(models.Model):
    serial_number = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    imei_no1 = models.CharField(max_length=50)
    imei_no2 = models.CharField(max_length=50)
    mobile_status = models.CharField(max_length=50)
    charger = models.BooleanField(default=False)
    date_of_purchase = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='iphones')

    def __str__(self):
        return f"{self.mobile} - {self.serial_number}"

class Smartphone(models.Model):
    serial_number = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    imei_no1 = models.CharField(max_length=50)
    imei_no2 = models.CharField(max_length=50)
    mobile_status = models.CharField(max_length=50)
    charger = models.BooleanField(default=False)
    date_of_purchase = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='smartphones')

    def __str__(self):
        return f"{self.mobile} - {self.serial_number}"

class KeypadPhone(models.Model):
    serial_number = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    imei_no1 = models.CharField(max_length=50)
    imei_no2 = models.CharField(max_length=50)
    mobile_status = models.CharField(max_length=50)
    charger = models.BooleanField(default=False)
    date_of_purchase = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='keypad_phones')

    def __str__(self):
        return f"{self.mobile} - {self.serial_number}"

class Headset(models.Model):
    date_of_purchase = models.DateField()
    brand = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    headset_status = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='headsets')

    def __str__(self):
        return f"{self.brand} - {self.serial_number}"

class Keyboard(models.Model):
    date_of_purchase = models.DateField()
    brand = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    keyboard_status = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='keyboards')

    def __str__(self):
        return f"{self.brand} - {self.serial_number}"

class Mouse(models.Model):
    date_of_purchase = models.DateField()
    brand = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    mouse_status = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='mice')

    def __str__(self):
        return f"{self.brand} - {self.serial_number}"

class Pendrive(models.Model):
    date_of_purchase = models.DateField()
    brand = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    pendrive_status = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='pendrives')

    def __str__(self):
        return f"{self.brand} - {self.serial_number}"

class HardDisk(models.Model):
    date_of_purchase = models.DateField()
    brand = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    hard_disk_status = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='hard_disks')

    def __str__(self):
        return f"{self.brand} - {self.serial_number}"

class LanAdapter(models.Model):
    date_of_purchase = models.DateField()
    brand = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    lan_adapter_status = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    warranty_details = models.CharField(max_length=255)
    warranty_date = models.DateField()
    purchased_amount = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='lan_adapters')

    def __str__(self):
        return f"{self.brand} - {self.serial_number}"

class SIM(models.Model):
    sim_number = models.CharField(max_length=100)
    sim_connection = models.CharField(max_length=100)
    sim_status = models.CharField(max_length=50)
    availability = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='sims')

    def __str__(self):
        return f"{self.sim_number} - {self.sim_connection}"

class RentalAsset(models.Model):
    serial_number = models.CharField(max_length=100)
    rental_laptop_brand = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram_capacity = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    inch = models.CharField(max_length=10)
    laptop_status = models.CharField(max_length=50)
    building_name = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='rental_assets')

    def __str__(self):
        return f"{self.rental_laptop_brand} - {self.serial_number}"


#Finance Module

class Invoice(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cash', 'Cash'),
        # Add other payment methods as needed
    ]
    
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Overdue', 'Overdue'),
        # Add other statuses as needed
    ]

    PAYMENT_TYPE_CHOICES = [
        ('One Time Payment', 'One Time Payment'),
        ('Quarterly Payment', 'Quarterly Payment'),
        ('Half Yearly Payment', 'Half Yearly Payment'),
        ('Yearly Payment', 'Yearly Payment'),
    ]

    requested_date = models.DateField()
    purchase_date = models.DateField()
    vendor = models.CharField(max_length=100)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_TYPE_CHOICES, null=True, blank=True)  # Allow null and blank
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    reference_transaction_id = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=100, blank=True, null=True)  # Updated field
    next_payment_date = models.DateField()
    department = models.CharField(max_length=100)
    invoice_file = models.FileField(upload_to='invoices/', null=True, blank=True)

    def _str_(self):
        return f"Invoice {self.id} from {self.vendor}"
