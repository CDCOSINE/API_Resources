from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from PIL import Image

from rest_framework.response import Response

from .serializers import *
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from datetime import datetime
from django.http import HttpResponse
from wsgiref.util import FileWrapper

import os

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return [hour, minutes, seconds] 


def download(serializer,request, file_path):
    
    wrapper = FileWrapper(open(file_path,'rb'))
    response = HttpResponse(wrapper, content_type='application/force-download')
    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    currenttime = str(datetime.now().time()).split(':')
    chhr = int(currenttime[0])
    chm = int(currenttime[1])
    chs = int(float(currenttime[2]))
    thattime = str(serializer.data['res_time']).split(':')
    thhr = int(thattime[0])
    thm = int(thattime[1])
    ths = int(float(thattime[2]))
    abc = (chhr-thhr)*3600 + (chm-thm)*60 + (chs-ths)
    if( int(abc) <= int(3600) ):
        return response
    else:
        li = convert(abc-3600)
        hr = li[0]
        minn = li[1]
        sec = li[2]
        li2 = convert(3600)
        trhr = li2[0]
        trminn = li2[1]
        trsec = li2[2]
        return render(request,'expired.html',{'tdiff':[hr,minn,sec,trhr,trminn,trsec]})



class Base(APIView):
    def get(self,request):
        return render(request,'home.html')

class DownRes(APIView):
    
    def get_user(self,res_id):
        try:
            res_id = int(res_id)
            model = Resource.objects.get(res_id=res_id)
            return model
        except Resource.DoesNotExist:
            return 
        
    
    def get(self,request,res_id):
        
        if not self.get_user(res_id):
            return Response(f'Resource with ID = {res_id} Not Found',status = status.HTTP_404_NOT_FOUND)
        
        serializer = ResSerializer(self.get_user(res_id))
        pathh = serializer.data['res_thumbnail']
        return download(serializer,request, r'C:/Users/User/Desktop/newpojectt'+pathh)

        
  
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
    
