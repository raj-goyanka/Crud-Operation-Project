# Import some important classes and functions.
from django.shortcuts import render,HttpResponseRedirect
from .forms import UserForm
from .models import User

# This function will add new students data and also show these data.
def add_show(request):
    if request.method == 'POST':
        fm=UserForm(request.POST)
        if fm.is_valid():
           fm.save() 
           return HttpResponseRedirect('/')
    else:
        fm=UserForm()
    students=User.objects.all()    
    return render(request,'enroll/addandshow.html',{'form':fm ,'stu':students})

# This function will delete perticular data.
def delete(request,id):
    student=User.objects.get(pk=id)
    student.delete() 
    return HttpResponseRedirect('/')

# This function will update perticular data.
def update(request,id):
    if request.method == 'POST':
       pi=User.objects.get(pk=id)
       fm=UserForm(request.POST,instance=pi)
       if fm.is_valid():
           fm.save()
    else:
       pi=User.objects.get(pk=id)
       fm=UserForm(instance=pi)
    return render(request,"enroll/update.html",{'form':fm,'id':id})   