from django.shortcuts import render
from .forms import StudentRegistration
from .models import student

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        myform = StudentRegistration(request.POST)
        if myform.is_valid():
            myform.save(commit=True)
    else:
        myform = StudentRegistration()
    diction = {'form':myform}
    return render(request, 'enroll/addshow.html', context=diction )