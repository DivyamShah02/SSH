from django.contrib import admin
from .models import PropertyInquiry
# Register your models here.

class AdminPropertyInquiry(admin.ModelAdmin):
    list_display = ('name','number','whatsapp','email','profession')
admin.site.register(PropertyInquiry, AdminPropertyInquiry)
