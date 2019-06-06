import os
import json
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .forms import UploadFileForm
# Create your views here.

class index_view(View):
    '''
    主页
    '''
    def get(self,request):
        msg = "nihao"
        return render(request, 'pc/index.html', {"msg": msg})

def handle_uploaded_file(f):
    if os.path.exists('uploads/'+f.name):
        return False
    else:
        with open('uploads/'+f.name, 'ab+') as destination:
            for chunk in f.chunks():
                # destination.write(chunk.decode('utf-8'))
                destination.write(chunk)
        return True

def upload_file(request):
    data={'name':''}
    if request.method == 'GET':
        form = UploadFileForm()
        return render(request, 'pc/upload.html', {'form': form})
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if not handle_uploaded_file(request.FILES['docfile']):
            data["name"] = "false"
            return HttpResponse(json.dumps(data))
        data["name"] = "true"
        return HttpResponse(json.dumps(data))
    else:
        form = UploadFileForm()
    return render(request, 'pc/upload.html', {'form': form})