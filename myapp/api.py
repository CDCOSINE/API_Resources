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

def download(request, file_path):
    try:
        wrapper = FileWrapper(open(file_path, 'rb'))
        response = HttpResponse(wrapper, content_type='application/force-download')
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    except Exception as e:
        return None







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
        currenttime = str(datetime.now().time()).split(':')
        chhr = int(currenttime[0])
        chm = int(currenttime[1])
        chs = int(float(currenttime[2]))
        thattime = str(serializer.data['res_time']).split(':')
        thhr = int(thattime[0])
        thm = int(thattime[1])
        ths = int(float(thattime[2]))
        abc = (chhr-thhr)*3600 + (thm-chm)*60 + (ths-chs)
        print(currenttime, ' --> ', thattime)
        print(abc)
        if( int(abc) <= int(10800) ):
             return download(request, r'C:/Users/User/Desktop/newpojectt'+pathh)
        else:
            return render(request,'expired.html',{})
        #return Response(serializer.data)
  
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
    
    def post(self,request):
            rid = request.POST['rid']
            size = request.POST['rsiz']
            name = request.POST['rname']
            cat = request.POST['rcat']
            link = request.POST['rlink']
            # thumb = '/' + thumb
            #thumb = thumb.file
            # thumb = 'abcdef'
            abc = r'C:/Users/User/Desktop/g1.PNG'
            img  = Image.open(abc)
            serializer = ResSerializer(data={'res_id':rid,'res_size':size,'res_name':name,'res_category':cat,'res_link':link})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return self.get(request)
            else:
                return render(request,"badreq.html")
            # else:
            #     return "abcedhvdebeh"
        # except:
        #     render(request,"badreq.html")
        
class Add_Res(APIView):
    def get(self,request):
        return render(request,'add_Res.html')
        # def post(self,request):
        #    