from django.http import JsonResponse
from .models import DeviceModel
from django.core.exceptions import ObjectDoesNotExist
import json

# Create your views here.


def hello(request):
    return JsonResponse({"message": "Hi"})


def device(request):
    if request.method == "POST":
        device_ob = DeviceModel.objects.create(
            mac_address=json.loads(request.body).get('mac_address')
        )
        device_ob.save()
        return JsonResponse(status=201, data={
                'mac_address': device_ob.mac_address,
                'is_active': device_ob.is_active
            }, safe=False)
    else:
        try:
            device_ob = DeviceModel.objects.get(pk=request.GET.get('mac_address'))
            return JsonResponse(status=200, data={
                'mac_address': device_ob.mac_address,
                'is_active': device_ob.is_active
            })
        except ObjectDoesNotExist:
            return JsonResponse(status=404, data="Does Not exist", safe=False)
