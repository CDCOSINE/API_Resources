from django.db import models
from datetime import datetime
# Create your models here.
class Resource(models.Model):
    res_id = models.IntegerField(unique=True)
    res_size = models.FloatField()
    res_name = models.CharField(max_length=100)
    res_category = models.CharField(max_length=15,null=True,blank=True)
    res_time = models.CharField(max_length=1000,default = str(datetime.now().time()))
    res_thumbnail = models.FileField(upload_to=r'SECRET/sec/waste')