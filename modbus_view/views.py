from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

# Create your views here.

class index_view(View):
    '''
    主页
    '''
    def get(self,request):
        msg = "nihao"
        return render(request, 'pc/index.html', {"msg": msg})