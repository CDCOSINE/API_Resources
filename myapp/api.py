from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView

from rest_framework.response import Response

from .serializers import *
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

class Base(APIView):
    def get(self,request):
        return render(request,'home.html')
   
class ResList(APIView):
    def get(self,request):
        model = Resource.objects.all()
        serializer = ResSerializer(model,many=True)
        
        list2=[]
        
        for i in range(len(serializer.data)):
            cnt=0
            list1=[]
            for value in serializer.data[i].values():
                cnt+=1
                list1.append((cnt,value))
            list2.append(list1)   
        
        return render(request,'res_list.html',{'model':list2})