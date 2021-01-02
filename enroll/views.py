from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .forms import StudentRegistrationUpdate
from .models import student

# Create your views here.


# Adding Function
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
            return HttpResponseRedirect('/')


            # myform.save(commit=True)
    else:
        myform = StudentRegistration()
    studata = student.objects.all()
    diction = {'form':myform, 'studentdata':studata, 'title':"Home"}
    return render(request, 'enroll/addshow.html', context=diction )


#Update Data

def update(request, id):
    if request.method=='POST':
        u_id = student.objects.get(pk=id)
        myform = StudentRegistrationUpdate(request.POST, instance=u_id)
        if myform.is_valid():
            myform.save(commit=True)
            return HttpResponseRedirect('/')
        
    else:
        u_id = student.objects.get(pk=id)
        myform = StudentRegistrationUpdate(instance=u_id)

    singledata = student.objects.get(pk=id)
    diction = {'form':myform, 'title':"Update | Student", 'studentdata':singledata}
    return render(request, 'enroll/updatestudent.html', context=diction)





    # Deleting Functions

def delete(request,id):
    if request.method == 'POST':
        del_id = student.objects.get(pk=id)
        del_id.delete()
        return HttpResponseRedirect('/')