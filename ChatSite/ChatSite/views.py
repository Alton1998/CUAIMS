from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .logic import measure
from .fusioncharts import FusionCharts
from chatsiteapp.models import Data_LogC,Data_LogD,Data_LogB,Data_LogA,Access_Log,FeedBack
import time
import smtplib
#use the decorator @login_required only when you want to restrict a page to only logged in user
# never use the '' as a link for the login url since it never works
# you can however use '' as link for your landing page
# function for the sign in page
def landing(request):
    return render(request,'landing.html',{})

# Block A page
@login_required(login_url='/landing/')
def mainpage(request):
    per=300
    perc=(per/415)*100
    per1=100
    perc1 = (per1/ 415) * 100
    return render(request,'main.html',{"per":per,"per1":per1,"perc":perc,"perc1":perc1})
# Block B page
@login_required(login_url='/landing/')
def Bmain(request):
    per=90
    per1=300
    return render(request,'Bmain.html',{"per":per,"per1":per1})

# Block C page
@login_required(login_url='/landing/')
def Cmain(request):
    per=90
    per1=300
    return render(request,'Cmain.html',{"per":per,"per1":per1})

# Block D page
@login_required(login_url='/landing/')
def Dmain(request):
    per=90
    per1=300
    return render(request,'Dmain.html',{"per":per,"per1":per1})

# Block A tank page
@login_required(login_url='/landing/')
def mainpageTank(request):
    per=100
    per1=300
    return render(request,'mainTank.html',{"per":per,"per1":per1})

# Block B tank page
@login_required(login_url='/landing/')
def BmainTank(request):
    per=100
    per1=300
    return render(request,'BmainTank.html',{"per":per,"per1":per1})

# Block C tank page
@login_required(login_url='/landing/')
def CmainTank(request):
    per=100
    per1=300
    return render(request,'CmainTank.html',{"per":per,"per1":per1})

# Block D tank page
@login_required(login_url='/landing/')
def DmainTank(request):
    per=100
    per1=300
    return render(request,'DmainTank.html',{"per":per,"per1":per1})

#form action function for logout
def logout(request):
    auth.logout(request)
    return render(request, 'landing.html', {})

# form action function for login
def login(request):
    if request.method=="POST":
        username=request.POST["Username"]
        password=request.POST["Password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            access=Access_Log.objects.create()
            access.User = username
            access.time = "" + time.strftime("%d/%m/%Y %H:%M:%S")
            access.save()
            return HttpResponseRedirect('/main/')
        else:
            stats="User Not Available"
            return render(request, 'landing.html', {"stats":stats})

# function to render signupform
def signupform(request):
    return render(request,'signupform.html',{})

# form action function for signing up
def signup(request):
    if request.method=="POST":
        username=request.POST['Username']
        password=request.POST['Password']
        confirmpassword=request.POST['Confirm_Password']
        if password==confirmpassword:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            return HttpResponseRedirect('/landing')
        else:
            stats="Passwords Do Not Match"
            return render(request, "signupform.html", {"stats":stats})

@login_required(login_url='/landing/')
def chart(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json",
                            # The data is passed as a string in the `dataSource` as parameter.
                            """{  
                                  "chart":{  
                                    "caption":"Water Available",
                                    "subCaption":"",
                                    "numberPrefix":"",
                                    "theme":"ocean"
                                  },
                                  "data":[  
                                    {"label":"Block A", "value":"880"},
                                    {"label":"Block B", "value":"530"},
                                    {"label":"Block C", "value":"590"},
                                    {"label":"Block D", "value":"520"},
                                  ]
                              }""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'fusioncharts-html-template.html', {'output': column2d.render()})

@login_required(login_url='/landing/')
def chartA(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json",
                            # The data is passed as a string in the `dataSource` as parameter.
                            """{  
                                  "chart":{  
                                    "caption":"Block A",
                                    "subCaption":"",
                                    "numberPrefix":"",
                                    "theme":"ocean"
                                  },
                                  "data":[  
                                    {"label":"Sump", "value":"880"},
                                    {"label":"Tank", "value":"530"},
                                    {"label":"Reservoir", "value":"590"},
                                  ]
                              }""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'GraphA.html', {'output': column2d.render()})
@login_required(login_url='/landing/')
def chartB(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json",
                            # The data is passed as a string in the `dataSource` as parameter.
                            """{  
                                  "chart":{  
                                    "caption":"Block B",
                                    "subCaption":"",
                                    "numberPrefix":"",
                                    "theme":"ocean"
                                  },
                                  "data":[  
                                    {"label":"Sump", "value":"880"},
                                    {"label":"Tank", "value":"530"},
                                    {"label":"Reservoir", "value":"590"},
                                  ]
                              }""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'GraphB.html', {'output': column2d.render()})

def chartC(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json",
                            # The data is passed as a string in the `dataSource` as parameter.
                            """{  
                                  "chart":{  
                                    "caption":"Block C",
                                    "subCaption":"",
                                    "numberPrefix":"",
                                    "theme":"ocean"
                                  },
                                  "data":[  
                                    {"label":"Sump", "value":"880"},
                                    {"label":"Tank", "value":"530"},
                                    {"label":"Reservoir", "value":"590"},
                                  ]
                              }""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'GraphC.html', {'output': column2d.render()})

def chartD(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json",
                            # The data is passed as a string in the `dataSource` as parameter.
                            """{  
                                  "chart":{  
                                    "caption":"Block D",
                                    "subCaption":"",
                                    "numberPrefix":"",
                                    "theme":"ocean"
                                  },
                                  "data":[  
                                    {"label":"Sump", "value":"880"},
                                    {"label":"Tank", "value":"530"},
                                    {"label":"Reservoir", "value":"590"},
                                  ]
                              }""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'GraphD.html', {'output': column2d.render()})

# measurement function from the sensor
@login_required(login_url='/landing/')
def measurement(request):
    p=measure();
    return HttpResponse(str(p))
def dataA(request,Sump,Tank,Reservoir):
    data=Data_LogA()
    data.Sump=Sump
    data.Reservoir=Reservoir
    data.Tank=Tank
    data.time = "" + time.strftime("%d/%m/%Y %H:%M:%S")
    data.save()
    return HttpResponse("Works")

def dataB(request,Sump,Tank,Reservoir):
    data=Data_LogB()
    data.Sump=Sump
    data.Reservoir=Reservoir
    data.Tank=Tank
    data.time = "" + time.strftime("%d/%m/%Y %H:%M:%S")
    data.save()
    return HttpResponse("Works")

def dataC(request,Sump,Tank,Reservoir):
    data=Data_LogC()
    data.Sump=Sump
    data.Reservoir=Reservoir
    data.Tank=Tank
    data.save()
    return HttpResponse("Works")

def dataD(request,Sump,Tank,Reservoir):
    data=Data_LogD()
    data.Sump=Sump
    data.Reservoir=Reservoir
    data.Tank=Tank
    data.time=""+ time.strftime("%d/%m/%Y %H:%M:%S")
    data.save()
    return HttpResponse("Works")

@login_required(login_url='/landing/')
def feedBack(request):
    return render(request,'FeedBack.html',{})

@login_required(login_url='/landing/')
def submitFeedBack(request):
    if request.method=="POST":
        feedback=request.POST["feedback"]
        f=FeedBack.objects.create()
        f.User=request.user.username
        f.FeedBack=feedback
        content=feedback
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login("alton.dsouza@btech.christuniversity.in","armourofgod")
        mail.sendmail("alton.dsouza@btech.christuniversity.in", "alton.dsouza@btech.christuniversity.in",content)
        mail.close()
        f.save()
        return HttpResponseRedirect('/main/')

@login_required(login_url='/landing/')
def AboutUs(request):
    return render(request,'AboutUs.html',{})