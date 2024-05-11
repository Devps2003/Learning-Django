from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    if request.method == 'POST':
        check = request.POST['check']
        print(check)
    date = datetime.datetime.now()
    isActive= True
    name = "Dev Pratap Singh"
    list_of_items=['item1','item2','item3','item4']
    student={
        "student_name":"Rahul",
        "student_college":"ZZU",
        "student_city":"Lucknow"
    }
    data = {
        'date': date,
        'isActive': isActive,
        'name': name,
        'list_of_items': list_of_items,
        'student_data': student
    }
    return render(request, "home.html",data)

def about(request):
    return render(request, "about.html",{})

def services(request):
    return render(request, "services.html",{})