from django.db import models
# Create your models here.
class Access_Log(models.Model):
    User=models.CharField(max_length=255)
    time=models.CharField(max_length=25)

    def __str__(self):
        return self.User,self.time

class Data_LogA(models.Model):
    Sump=models.FloatField()
    Tank=models.FloatField()
    Reservoir=models.FloatField()
    time=models.CharField(max_length=25)

    def __str__(self):
        return self.Sump,self.Tank,self.Reservoir,self.time
class Data_LogB(models.Model):
    Sump=models.FloatField()
    Tank=models.FloatField()
    Reservoir=models.FloatField()
    time=models.CharField(max_length=25)

    def __str__(self):
        return self.Sump, self.Tank, self.Reservoir, self.time

class Data_LogC(models.Model):
    Sump=models.FloatField()
    Tank=models.FloatField()
    Reservoir=models.FloatField()
    time=models.CharField(max_length=25)

    def __str__(self):
        return self.Sump, self.Tank, self.Reservoir, self.time

class Data_LogD(models.Model):
    Sump=models.FloatField()
    Tank=models.FloatField()
    Reservoir=models.FloatField()
    time=models.CharField(max_length=25)

    def __str__(self):
        return self.Sump, self.Tank, self.Reservoir, self.time

class FeedBack(models.Model):
    User=models.CharField(max_length=300)
    FeedBack=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.User,self.time,self.FeedBack