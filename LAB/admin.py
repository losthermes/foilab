from django.contrib import admin
from LAB.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)#the second variable is the view for the admin page?



