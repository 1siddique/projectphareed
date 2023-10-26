from django.shortcuts import render
from .forms import SignupForm ,Feedback,contact
from django.contrib.auth import authenticate, login, logout,forms
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
def appTHREE_RI(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/signin')

    else:
        fm = SignupForm()
    return render(request, "register.html", {'form':fm})




def signout(request):
    logout(request)
    return redirect("/signin")


def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)

            if user is not None:
                login(request, user)
                return redirect("/feedback")

    else:
        fm = AuthenticationForm()
    return render(request,"signin.html",{'form':fm})






def feedback(request):
    if request.method == "POST":
        f1 = Feedback(request.POST)
        if f1.is_valid():
            f1.save()
            return redirect("/SingUp")
    else:
        f1 = Feedback()
    return render(request,"feedback.html",{'feed':f1})



def Contact(request):
    if request.method == "POST":
        f1 = contact(request.POST)
        if f1.is_valid():
            f1.save()
    else:
        f1 = contact()
    return render(request,"contact.html",{'feed':f1})






def Aboutus(request):
    return render(request,'Aboutus.html')

def contact(request):
    return render(request,'contact.html')


def course(request):
    return render(request,'course.html')


def index(request):
    return render(request,'index.html')

# Create your views here.






