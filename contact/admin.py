from django.contrib import admin
from .models import Contact
# Register your models here.

admin.site.site_header="Contact Admin"
admin.site.site_title="Contact Admin Area"
admin.site.index_title="Welcome to Contact Admin Area"
admin.site.register(Contact)
