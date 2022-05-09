from django.contrib import admin
from . models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid', 'cname', 'cmail', 'cadd']

admin.site.register(Customer, CustomerAdmin)


# Register your models here.
