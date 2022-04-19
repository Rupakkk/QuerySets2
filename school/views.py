from optparse import Values
from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    # student_data = Student.objects.get(id=1)
    # student_data = Student.objects.first()
    student_data = Student.objects.order_by('name').first()
    print("Return :", student_data)
    print()
    
    return render(request,'school/home.html',{'students':student_data})