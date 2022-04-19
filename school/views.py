from optparse import Values
from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
# Create your views here.

def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(city = 'Smash')
    # student_data = Student.objects.exclude(name='Stark')
    # student_data = Student.objects.order_by('marks')
    # student_data = Student.objects.order_by('?')
    # student_data = Student.objects.order_by('id')[1:5]
    # student_data = Student.objects.order_by('id').reverse()
    # student_data = Student.objects.order_by('id').reverse()[:5]
    # student_data = Student.objects.values()    It returns a list of dictionaries
    # student_data = Student.objects.values('name','city')
    # student_data = Student.objects.values_list()  
    # student_data = Student.objects.values_list('id','name')  
    # student_data = Student.objects.values_list('id','name',named=True)  
    # student_data = Student.objects.using('default')
    # student_data = Student.objects.dates('pass_date','month')
    # student_data = Student.objects.datetimes('pass_date','month','ASC',tzinfo=None)
    # student_data = Student.objects.values('name').distinct()


    # Second Table
    qs1 = Student.objects.values_list('name',named = True)
    qs2 = Teacher.objects.values_list('name',named = True)
    # student_data = qs2.union(qs1)
    # student_data = qs2.union(qs1,all=True) It keeps duplicate Values
    # student_data = qs1.intersection(qs2)
    # student_data = qs1.difference(qs2)


    # Operators

    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106)) # Q is special object and we need to import it
    # student_data = Student.objects.filter(id=6,roll=106)

    # student_data = Student.objects.filter(id=6) | Student.objects.filter(name='Hulk')
    student_data = Student.objects.filter(Q(id=6) | Q(name='Hulk')) 

    print("Return:",student_data) # This prints all the query on terminal
    print()
    # print("SQL Query",student_data.query) 
    return render(request,'school/home.html',{'students':student_data})