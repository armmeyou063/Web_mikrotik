from django.shortcuts import render, redirect
from network.models import  identity as identity_model ,device as device_model


def Dashboard(request):
     identity=identity_model.objects.all()
     return render(request, 'dashboard/dashboard.html',{'identity':identity})


def register(request):
     identity=identity_model.objects.all()
     return render(request, 'dashboard/dashboard.html',{'identity':identity})

def register_device(request):
     identity=identity_model.objects.all()
     return render(request, 'dashboard/dashboard.html',{'identity':identity})

def device_list(request):
     device=device_model.objects.all()
     return render(request, 'dashboard/device_list.html',{'device':device})

def device_add(request):
     if request.method == 'POST':
          name=request.POST['name']
          host=request.POST['host']
          username=request.POST['username']
          password=request.POST['password']
          device = device_model(
            name= name,
            host=host,
            username=username,
            password= password
            )
          device.save()
          return redirect('device-list')
     return render(request, 'dashboard/device_add.html')

def device_edit(request,url):
     device=device_model.objects.get(id=url)
     if request.method == 'POST':
          name=request.POST['name']
          host=request.POST['host']
          username=request.POST['username']
          password=request.POST['password']
          device.name= name
          device.host= host
          device.username= username
          device.password= password
          print(device.name)
          device.save()
          return redirect('device-list')
     return render(request, 'dashboard/device_edit.html',{'device':device})

def device_delete(request,url):
     device=device_model.objects.get(id=url)
     device.delete()
     return redirect('device-list')  
