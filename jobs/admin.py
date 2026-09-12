from django.contrib import admin
from .models import job, application

class Jobadmin  (admin.ModelAdmin):
    list_display = ('title', 'Company_name','posted_by'  ,'date_posted' )
    search_fields = ('title', 'Company_name',)
    list_filter = ('posted_by',)
    
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'date_applied')
    
admin.site.register(job, Jobadmin)
admin.site.register(application, ApplicationAdmin)