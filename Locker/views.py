from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Data1.models import user1
from Data2.models import user2
from django.core.files.storage import FileSystemStorage
#from Data2.models import profile


def Signup(request):
    try:
        if request.method == "POST":
            mobile_no = request.POST['phone']
            usern = request.POST['user_name']
            email_id = request.POST['email_id']
            pin_no = request.POST['pin']
            fDB = user1(mobile_no=mobile_no , user_name=usern , email_id=email_id , pin_no=pin_no)
            fDB.save()
            # my_user = User.objects.create_user(mobile_no,usern,email_id,pin_no)
            # my_user.save()
            #return HttpResponse("The User has been created succesfully!!")
            
            return HttpResponseRedirect('/header/')
    except:
        pass
    return render(request, "Signup.html")

def Login(request):
    try:
        if request.method == "POST":
            usern = request.POST.get('user_name')
            pin_no = int(request.POST.get('pin'))
            print(usern,pin_no)
            u_n = user1.objects.values_list('user_name',flat=True).count()
            #print(u_n)
            for i in range(0,u_n):
                if usern==user1.objects.all()[i].user_name and pin_no==user1.objects.all()[i].pin_no:
                   # print(usern==user1.objects.all()[i].user_name)
                    #print(pin_no==user1.objects.all()[i].pin_no)
                    return redirect('/header/')
            else:
                return HttpResponse("Your PIN or User_name Invalid")
            
    except:
        pass
    return render(request, "login.html")


def header(request):
    return render(request,"header.html")
def contact(request):
    return render(request,"contact.html")
def blog(request):
    return render(request,"blog.html")
def AboutUs(request):
    return render(request,"AboutUs.html")
def service(request):
    all_uploads=user2.objects.all()
    return render(request,'service.html',{'uploads':all_uploads})
    
       # if request.method == "POST":
            
         ##   usern = request.POST['user_name']
            #file=request.POST['file']
          #  upload = upload( user_name=usern ,upload=file)
           # upload.save()
def normalupload(request):
    if request.method == 'POST' and request.FILES["file"]:
        file=request.FILES['file']
        fs=FileSystemStorage()
        filename=fs.save(file.name,file)
        #url= fs.url(filename)
    
    return HttpResponse("Successfully")


