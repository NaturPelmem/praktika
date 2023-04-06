from django.contrib import admin
from .models import *


@admin.register(Client)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'address', 'INN', 'r_score', 'BIC', 'name_manager', 'contact_person', 'tel_contact_person', 'mail', 'password', 'client_code']
    list_editable = ['company_name', 'address', 'INN', 'r_score', 'BIC', 'name_manager', 'contact_person', 'tel_contact_person', 'mail', 'password', 'client_code']
    ordering = ['id']
    search_fields = ['company_name', 'INN', 'name_manager']
    save_as = True


@admin.register(ClientFL)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'FIO', 'client_code', 'passport_data', 'Date_of_birth', 'address', 'mail', 'password']
    list_editable = ['FIO', 'client_code', 'passport_data', 'Date_of_birth', 'address', 'mail', 'password']
    ordering = ['id']
    search_fields = ['FIO', 'client_code', 'passport_data']
    save_as = True


@admin.register(Employee)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'cod_employee', 'post', 'FIO', 'login', 'password', 'orders']
    list_editable = ['cod_employee', 'post', 'FIO', 'login', 'password', 'orders']
    ordering = ['id']
    search_fields = ['cod_employee', 'FIO', 'orders']
    save_as = True


@admin.register(Product)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['index', 'product', 'art', 'price']
    list_editable = ['product', 'art', 'price']
    ordering = ['id']
    search_fields = ['product', 'art', 'price']
    save_as = True


@admin.register(Order)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['index', 'order_number', 'date_creation', 'client_code', 'article', 'status', 'closing_date', 'employee_code']
    list_editable = ['order_number', 'date_creation', 'client_code', 'article', 'status', 'closing_date', 'employee_code']
    ordering = ['id']
    search_fields = ['order_number', 'client_code']
    save_as = True
