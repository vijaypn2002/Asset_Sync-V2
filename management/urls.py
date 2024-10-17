from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView

urlpatterns = [
    # Redirect the root URL to the login page
    path('', lambda request: redirect('login'), name='root'),
    path('search-employee/', views.search_employee, name='search_employee'),
    path('assigned-employee-assets/<int:employee_id>/', views.assigned_employee_assets, name='assigned_employee_assets'),

    # Authentication-related paths
    path('login/', LoginView.as_view(template_name='management/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),  # Modified for redirection after logout
    path('password-reset/', PasswordResetView.as_view(template_name='management/password_reset.html'), name='password_reset'),

    # Dashboard and general views
    path('dashboard/', views.dashboard, name='dashboard'),
    path('onboarding-exit-clearance/', views.onboarding_exit_clearance, name='onboarding_exit_clearance'),
    path('homepage/', views.homepage, name='homepage'),  # Added for redirecting to homepage after login

    # Employee-related views
    path('add-employee/', views.add_employee, name='add_employee'),
    path('view-employee/', views.view_employee, name='view_employee'),
    path('edit-employee/<str:employee_id>/', views.edit_employee, name='edit_employee'),
    path('bulk-import-employees/', views.bulk_import_employees, name='bulk_import_employees'),
    path('exit-employee/', views.exit_employee, name='exit_employee'),
    path('confirm-exit-employee/<str:employee_id>/', views.confirm_exit_employee, name='confirm_exit_employee'),
    path('exit-tracker/', views.exit_tracker, name='exit_tracker'),
    path('restore-employee/<str:employee_id>/', views.restore_employee, name='restore_employee'),

    # Asset Management
    path('asset-management/', views.asset_management, name='asset_management'),
    path('add-asset/', views.add_asset, name='add_asset'),
    path('view-asset/', views.view_asset, name='view_asset'),
    path('add-asset/hardware/', views.add_hardware, name='add_hardware'),

    # Specific asset types under Hardware
    path('add-asset/hardware/laptop/', views.add_laptop, name='add_laptop'),
    path('view-asset/laptops/', views.view_laptops, name='view_laptops'),
    path('edit-laptop/<int:laptop_id>/', views.edit_laptop, name='edit_laptop'),
    path('delete-laptop/<int:laptop_id>/', views.delete_laptop, name='delete_laptop'),
    path('view-asset/desktops/', views.view_desktops, name='view_desktops'),
    path('add-desktop/', views.add_desktop, name='add_desktop'),
    path('edit-desktop/<int:desktop_id>/', views.edit_desktop, name='edit_desktop'),
    path('delete-desktop/<int:desktop_id>/', views.delete_desktop, name='delete_desktop'),
    path('view-asset/printers/', views.view_printers, name='view_printers'),
    path('add-printer/', views.add_printer, name='add_printer'),
    path('edit-printer/<int:printer_id>/', views.edit_printer, name='edit_printer'),
    path('delete-printer/<int:printer_id>/', views.delete_printer, name='delete_printer'),
    path('view-asset/ipads/', views.view_ipads, name='view_ipads'),
    path('add-ipad/', views.add_ipad, name='add_ipad'),
    path('edit-ipad/<int:ipad_id>/', views.edit_ipad, name='edit_ipad'),
    path('delete-ipad/<int:ipad_id>/', views.delete_ipad, name='delete_ipad'),
    path('view-asset/iphones/', views.view_iphones, name='view_iphones'),
    path('add-iphone/', views.add_iphone, name='add_iphone'),
    path('edit-iphone/<int:iphone_id>/', views.edit_iphone, name='edit_iphone'),
    path('delete-iphone/<int:iphone_id>/', views.delete_iphone, name='delete_iphone'),
    path('view-asset/smartphones/', views.view_smartphones, name='view_smartphones'),
    path('add-smartphone/', views.add_smartphone, name='add_smartphone'),
    path('edit-smartphone/<int:smartphone_id>/', views.edit_smartphone, name='edit_smartphone'),
    path('delete-smartphone/<int:smartphone_id>/', views.delete_smartphone, name='delete_smartphone'),
    path('view-asset/keypad-phones/', views.view_keypadphones, name='view_keypadphones'),
    path('add-keypadphone/', views.add_keypadphone, name='add_keypadphone'),
    path('edit-keypadphone/<int:keypadphone_id>/', views.edit_keypadphone, name='edit_keypadphone'),
    path('delete-keypadphone/<int:keypadphone_id>/', views.delete_keypadphone, name='delete_keypadphone'),

    # Specific asset types under Accessories
    path('add-asset/accessories/', views.add_accessories, name='add_accessories'),
    path('view-asset/headsets/', views.view_headsets, name='view_headsets'),
    path('add-headset/', views.add_headset, name='add_headset'),
    path('edit-headset/<int:headset_id>/', views.edit_headset, name='edit_headset'),
    path('delete-headset/<int:headset_id>/', views.delete_headset, name='delete_headset'),
    path('view-asset/keyboards/', views.view_keyboards, name='view_keyboards'),
    path('add-keyboard/', views.add_keyboard, name='add_keyboard'),
    path('edit-keyboard/<int:keyboard_id>/', views.edit_keyboard, name='edit_keyboard'),
    path('delete-keyboard/<int:keyboard_id>/', views.delete_keyboard, name='delete_keyboard'),
    path('view-asset/mice/', views.view_mice, name='view_mice'),
    path('add-mouse/', views.add_mouse, name='add_mouse'),
    path('edit-mouse/<int:mouse_id>/', views.edit_mouse, name='edit_mouse'),
    path('delete-mouse/<int:mouse_id>/', views.delete_mouse, name='delete_mouse'),
    path('view-asset/pendrives/', views.view_pendrives, name='view_pendrives'),
    path('add-pendrive/', views.add_pendrive, name='add_pendrive'),
    path('edit-pendrive/<int:pendrive_id>/', views.edit_pendrive, name='edit_pendrive'),
    path('delete-pendrive/<int:pendrive_id>/', views.delete_pendrive, name='delete_pendrive'),
    path('view-asset/harddisks/', views.view_harddisks, name='view_harddisks'),
    path('add-harddisk/', views.add_harddisk, name='add_harddisk'),
    path('edit-harddisk/<int:harddisk_id>/', views.edit_harddisk, name='edit_harddisk'),
    path('delete-harddisk/<int:harddisk_id>/', views.delete_harddisk, name='delete_harddisk'),
    path('view-asset/lanadapters/', views.view_lanadapters, name='view_lanadapters'),
    path('add-lanadapter/', views.add_lanadapter, name='add_lanadapter'),
    path('edit-lanadapter/<int:lanadapter_id>/', views.edit_lanadapter, name='edit_lanadapter'),
    path('delete-lanadapter/<int:lanadapter_id>/', views.delete_lanadapter, name='delete_lanadapter'),

    # Specific asset types under Communication Devices
    path('add-asset/communication-devices/', views.add_communication_devices, name='add_communication_devices'),
    path('view-asset/sims/', views.view_sims, name='view_sims'),
    path('add-sim/', views.add_sim, name='add_sim'),
    path('edit-sim/<int:sim_id>/', views.edit_sim, name='edit_sim'),
    path('delete-sim/<int:sim_id>/', views.delete_sim, name='delete_sim'),

    # Rental Asset
    path('view-asset/rental-assets/', views.view_rental_assets, name='view_rental_assets'),
    path('add-rental-asset/', views.add_rental_asset, name='add_rental_asset'),
    path('edit-rental-asset/<int:rental_asset_id>/', views.edit_rental_asset, name='edit_rental_asset'),
    path('delete-rental-asset/<int:rental_asset_id>/', views.delete_rental_asset, name='delete_rental_asset'),




    # Asset Assignment
    path('assign-asset/', views.assign_asset, name='assign_asset'),
    path('assign-asset/total/', views.total_assets, name='total_assets'),
    path('assign-asset/free/', views.free_assets, name='free_assets'),
    path('assign-asset/assigned/', views.assigned_assets, name='assigned_assets'),
    path('assign-asset/unassign/<int:asset_id>/<str:asset_type>/', views.unassign_asset, name='unassign_asset'),
    path('assign-asset/export-csv/', views.export_assigned_assets_csv, name='export_assigned_assets_csv'),
    path('assign-asset/assign/<int:asset_id>/', views.assign_asset_to_employee, name='assign_asset_to_employee'),

    # Finance Management and Reports
    path('finance-management/', views.finance_management, name='finance_management'),
    path('report/', views.report, name='report'),

    # Settings and User Management URLs
    path('settings/', views.settings, name='settings'),
    path('add-user/', views.add_user, name='add_user'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),

    # Finance Module
    path('finance-module/', views.finance_module, name='finance_module'),
    path('invoice-list/', views.invoice_list, name='invoice_list'),
    path('invoices/add/', views.add_invoice, name='add_invoice'),
    path('edit-invoice/<int:pk>/', views.edit_invoice, name='edit_invoice'),
    path('export-invoices/', views.export_invoices, name='export_invoices'),
    path('delete-invoices/', views.delete_invoices, name='delete_invoices'),
    path('bulk-upload/', views.bulk_upload, name='bulk_upload'),
]
