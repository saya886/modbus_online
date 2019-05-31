import json


from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from .models import data_history,sensor_data


class modbus_method_01(View):

    def get(self,request):
        res_data = data_history.objects.last().value
        return JsonResponse({'data': res_data, 'status': '1', 'msg': '执行成功'}, content_type="application/json")

    def post(self,request):
        json_str = request.POST.get("json_str","")
        sensor_id = "1"
        try:
            py_data = json.loads(json_str)
            for i in py_data["data"]:
                int(i, 16)
            # data_history(value=",".join(py_data["data"])).save()
            sensor_data.objects.filter(id=sensor_id).update(data=",".join(py_data["data"]))
        except:
            return JsonResponse({'data': [], 'status': '0', 'msg': '参数错误'}, content_type="application/json")

        return JsonResponse({'data': [], 'status': '1', 'msg': '执行成功'}, content_type="application/json")