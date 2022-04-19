
from datetime import datetime
from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    # student_data = Student.objects.get(id=1)
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()
    # student_data = Student.objects.last()
    # student_data = Student.objects.latest('city')
    # student_data = Student.objects.earliest('city')
    student_data = Student.objects.all()
    Student.objects.create(name='Ram',roll=150,city='thn',marks=99,passing_year=datetime(2022,12,5))
    print(student_data.exists())
    # print("Return :", student_data)
    print()
    
    return render(request,'school/home.html',{'students':student_data})