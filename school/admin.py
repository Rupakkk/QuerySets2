from django.contrib import admin
from .models import Student, Teacher 
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city','pass_date']



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','emp_roll','city','salary','join_date']