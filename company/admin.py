from django.contrib import admin
from .models import Company,CompanyJobs,Jobs,Comment

# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyJobs)
admin.site.register(Jobs)

admin.site.register(Comment)
