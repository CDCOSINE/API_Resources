from django.db import models
from datetime import datetime
# Create your models here.
class Resource(models.Model):
    res_id = models.IntegerField(unique=True)
    res_size = models.FloatField()
    #IntegerField(unique=True)
    res_name = models.CharField(max_length=100)
    res_category = models.CharField(max_length=15,null=True,blank=True)
    res_link = models.CharField(max_length = 10000)
    res_time = models.CharField(max_length=1000,default = str(datetime.now().time()))
    res_thumbnail = models.FileField()
    #res_path = models.CharField(max_length=10000000000, default = self.upload_to())
    # def __str__(self):
    #     if not self.player_team:
    #         a = "None"
    #     else:
    #         a = self.player_team
    #     return self.player_name+" - "+a
    