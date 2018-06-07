"""ChatSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from chatsiteapp import views1
urlpatterns = [
    path('admin/', admin.site.urls),
    # landing page which is the sign in made using bootstraps example templates
    path('landing/',views.landing,name='landing'),
    # form action link this uses django's in  built authentication
    path('login/',views.login,name='login'),
    # the sign up form
    path('signup/',views.signupform,name='signupform'),
    # form action link for signing up
    path('signupsucces/',views.signup,name='signup'),
    #first page you see after successfully logging in which contains information about Block A
    path('main/',views.mainpage,name='main'),
    # This link directs you to a page where info about Block B is displayed
    path('Bmain/',views.Bmain,name='Bmain'),
    # This link directs you to a page where info about Block C is displayed
    path('Cmain/',views.Cmain,name='Cmain'),
    # This link directs you to a page where info about Block D is displayed
    path('Dmain/',views.Dmain,name='Dmain'),
    # This link directs you to a page where the Tank info about Block A is displayed
    path('mainTank/',views.mainpageTank,name='mainTank'),
    # This link directs you to a page where the Tank info about Block B is displayed
    path('BmainTank/',views.BmainTank,name='BmainTank'),
    # This link directs you to a page where the Tank info about Block C is displayed
    path('CmainTank/',views.CmainTank,name='CmainTank'),
    # This link directs you to a page where the Tank info about Block D is displayed
    path('DmainTank/',views.DmainTank,name='DmainTank'),
    # form action for logout
    path('logout/',views.logout,name='logout'),
    # This link displays  a chart for water available on campus
    path('chart/',views.chart,name='chart'),
    # Block A chart
    path('chartA/',views.chartA,name='chartA'),
    # Block B chart
    path('chartB/',views.chartB, name='chartB'),
    # Block C chart
    path('chartC/',views.chartC, name='chartC'),
    # Block D chart
    path('chartD/',views.chartD, name='chartD'),
    # Take readings from the sensor
    path('measure',views.measurement,name='measure'),
    path('Access_log/', views1.Access_LogList.as_view()),
    path('Data_logA/', views1.Data_LogAList.as_view()),
    path('Data_logB/', views1.Data_LogBList.as_view()),
    path('Data_logC/', views1.Data_LogCList.as_view()),
    path('Data_logD/', views1.Data_LogDList.as_view()),
    path('feedbacklist/',views1.FeedBackList.as_view()),
    path('User/', views1.UserList.as_view()),
    path('DataA/<int:Sump>/<int:Tank>/<int:Reservoir>',views.dataA),
    path('DataB/<int:Sump>/<int:Tank>/<int:Reservoir>',views.dataB),
    path('DataC/<int:Sump>/<int:Tank>/<int:Reservoir>',views.dataC),
    path('DataD/<int:Sump>/<int:Tank>/<int:Reservoir>', views.dataD),
    path('FeedBack/',views.feedBack,name='FeedBack'),
    path('AboutUs/',views.AboutUs,name='AboutUs'),
    path('submitFeedBack/',views.submitFeedBack,name='submitFeedBack'),

]
