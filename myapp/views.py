from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib import messages


def demopage(request):
    return HttpResponse("Hello! This is my first Website.")

def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def frompage(request):
    return render(request,'form.html')

def frompageprocess(request):
    a = int(request.POST["txt1"])
    b = int(request.POST["txt2"])
    c = a+b
    return render (request,"ans.html",{'mya': a , 'myb': b, 'myc' : c})

def subpage(request):
    return render(request,'marks.html')

def sumpage(request):
    s1 = int(request.POST["sub1"])
    s2 = int(request.POST["sub2"])
    s3 = int(request.POST["sub3"])
    s4 = int(request.POST["sub4"])
    s5 = int(request.POST["sub5"])
    sum = s1+s2+s3+s4+s5
    avg= sum/5
    
    if avg>80:
        msg = "Pass"
    else:
        
        msg="Fail"
        
    return render(request,"sum.html",{'mys1':s1 , 'mys2':s2, 'mys3':s3,'mys4':s4,'mys5':s5,'sum':sum,'avg':avg,'mymsg':msg})

def addStudent(request):
    if request.method == 'GET':
        context ={'form':StudentForm()}
        return render(request,'add.html',context)
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Added')
            return redirect(addStudent)
        else:
            messages.error(request,'Error in Record Add')
            return render(request,'add.html',{'form' : form})
    
def displayStudent(request):
    dbdata = Student.objects.all()
    context = {'mydata':dbdata}
    return render(request,'display.html',context)

def deleteStudent(request,id):
    mydata = get_object_or_404(Student, pk=id)
    mydata.delete()
    messages.success(request,'Record Delete')
    return redirect(displayStudent)

def editStudent(request,id):
    mydata = get_object_or_404(Student,pk=id)
    if request.method == 'GET':
        context = {'form': StudentForm(instance=mydata),'id':id}
        return render(request,'edit.html',context)
    elif request.method == 'POST':
        form = StudentForm(request.POST, instance=mydata)
        if form.is_valid():
            form.save()
            messages.success(request,'updated Successfully')
            return redirect(displayStudent)
        else:
            messages.error(request,'errors:')
            return render(request,'edit.html',{'form':form})