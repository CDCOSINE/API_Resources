from rest_framework import serializers
from myapp.models import Resource
from datetime import datetime

class ResSerializer(serializers.ModelSerializer):
    res_id = serializers.IntegerField()
    res_size = serializers.FloatField()
    #IntegerField(unique=True)
    res_name = serializers.CharField(max_length=100)
    res_category = serializers.CharField(max_length=15)
    res_thumbnail = serializers.FileField()
    res_time = serializers.CharField(max_length=1000,default = str(datetime.now().time()))
    class Meta:
        model = Resource
        fields = '__all__'
