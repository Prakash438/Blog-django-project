from django.contrib import admin
from testapp.models import student,Proxystudent
class studentAdmin(admin.ModelAdmin):
    list_display =['name','age','mobile_no','Email','roll_no',]

class ProxystudentAdmin(admin.ModelAdmin):
    list_display =['name','age','mobile_no','Email','roll_no',]


# Register your models here.
admin.site.register(student,studentAdmin)
admin.site.register(Proxystudent,ProxystudentAdmin)