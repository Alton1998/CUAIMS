from django.contrib import admin
from chatsiteapp.models import Data_LogA,Data_LogB,Data_LogD,Data_LogC,Access_Log,FeedBack
# Register your models here.
admin.site.register(Data_LogC)
admin.site.register(Data_LogA)
admin.site.register(Data_LogD)
admin.site.register(Data_LogB)
admin.site.register(Access_Log)
admin.site.register(FeedBack)
