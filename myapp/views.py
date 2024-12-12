from django.shortcuts import render
from django.http import HttpResponse

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
        print("pass")
    else:
        print("Fail")
        msg=""
        
    return render(request,"sum.html",{'mys1':s1 , 'mys2':s2, 'mys3':s3,'mys4':s4,'mys5':s5,'sum':sum,'avg':avg})
    
    