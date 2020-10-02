from django.db import models

# Create your models here.
class Resource(models.Model):
    res_id = models.IntegerField(unique=True)
    res_size = models.FloatField()
    #IntegerField(unique=True)
    res_name = models.CharField(max_length=100)
    res_category = models.CharField(max_length=15,null=True,blank=True)
    res_link = models.CharField(max_length = 10000)
    def upload_dir(self,filename):
        return r"static/" + filename
    res_thumbnail = models.ImageField(upload_to = upload_dir,null=True,blank=True)
    # def __str__(self):
    #     if not self.player_team:
    #         a = "None"
    #     else:
    #         a = self.player_team
    #     return self.player_name+" - "+a
    