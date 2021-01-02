from django.shortcuts import render
from .forms import StudentRegistration
from .models import student

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        myform = StudentRegistration(request.POST)
        if myform.is_valid():
            nm = myform.cleaned_data['name']
            em = myform.cleaned_data['email']
            pw = myform.cleaned_data['password']
            reg = student(name=nm, email=em, password=pw)
            reg.save()
            myform = StudentRegistration()

            # myform.save(commit=True)
    else:
        myform = StudentRegistration()
        studata = student.objects.all()
    diction = {'form':myform, 'studentdata':studata}
    return render(request, 'enroll/addshow.html', context=diction )