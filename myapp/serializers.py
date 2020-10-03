from rest_framework import serializers
from myapp.models import Resource

class ResSerializer(serializers.ModelSerializer):
    res_id = serializers.IntegerField()
    res_size = serializers.FloatField()
    #IntegerField(unique=True)
    res_name = serializers.CharField(max_length=100)
    res_category = serializers.CharField(max_length=15)
    res_link = serializers.CharField(max_length = 10000)
    #def upload_dir(self,filename):
     #   return r"C:/abc/" + filename
    res_thumbnail = serializers.ImageField()
    res_path = serializers.CharField(allow_null=True)
    res_time = serializers.DateTimeField()
    class Meta:
        model = Resource
        fields = '__all__'
