from django.shortcuts import render


# Create your views here.
vali={}
def selector(request):
    if request.GET['submit']=='SignUp':
        email_id=request.GET['email_id']
        password=request.GET['password_signup']
        cnfpass=request.GET['conf_password']
        if password == cnfpass:
            vali[email_id]=password
            return render(request,'selector.html',{'welcome':"Welcome : "+email_id})
        else:
            return render(request,'signup.html',{'error':'Check your Email and Password combination','display':'block'})

    elif request.GET['submit']=='Login':
        if request.GET['email'] in vali.keys():
            if vali[request.GET['email']]== request.GET['password']:
                return render(request,'selector.html',{'welcome':'Welcome : '+request.GET['email']})
        else:
            return render(request,'login.html',{'error':'Please check the username & password','inli':'block'})
