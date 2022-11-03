import json
from django.shortcuts import render, redirect
import paramiko
from librouteros import connect
from network.models import  interface as interface_model, route as route_model,identity as identity_model



######################################## PART IP Route ########################################################################################


def route_list(request):
    if 'host' in request.session :
        route=route_model.objects.all()
        identity=identity_model.objects.all()
        return render(request,'route/route_list.html',{'route':route,'identity':identity})
    else:
        return redirect('login-form')
    


def route_add(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        interface=interface_model.objects.all()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        if request.method == 'POST':
            dst_address=request.POST['dst_address']
            gateway = request.POST['gateway']
            stdin, stdout, stderr = client.exec_command('/ip route add dst-address='+dst_address+' gateway='+gateway)
            return redirect('route-data')  
        return render(request,'route/route_add.html',{'interface':interface})
    else:
        return redirect('login-form')
    

def route_edit(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        interface=interface_model.objects.all()
        route=route_model.objects.get(id=url)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        if request.method == 'POST':
            dst_address=request.POST['dst_address']
            gateway = request.POST['gateway']
            route_id= request.POST['route_id']
            stdin, stdout, stderr = client.exec_command('/ip route set dst-address='+dst_address+' gateway='+gateway+' number='+route_id)
            return redirect('route-data')  
        return render(request,'route/route_edit.html',{'route':route,'interface':interface})
    else:
        return redirect('login-form')
    


def route_delete(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        route=route_model.objects.get(id=url)
        #print(route.route_id)
        stdin, stdout, stderr = client.exec_command('/ip route remove number='+route.route_id)
        route.delete()
        return redirect('route-list')  
    else:
        return redirect('login-form')
    


def route_data(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        api = connect(username=username, password=password,host=host)
        route_info = api(cmd="/ip/route/print")
        route_del=route_model.objects.all()
        route_del.delete()
        for route in route_info:
            #print(json.dumps(route, indent=4))
            if route.get('dynamic') == None:
                routesave = route_model(
                route_id= route['.id'],
                dst_address=route['dst-address'],
                gateway=route['gateway'],
                status=route['gateway-status'],
                distance=route['distance'],
                dynamic=''
                )
            else:
                routesave = route_model(
                route_id= route['.id'],
                dst_address=route['dst-address'],
                gateway=route['gateway'],
                status=route['gateway-status'],
                distance=route['distance'],
                dynamic=route['dynamic']
                )
            routesave.save()
        return redirect('route-list')
    else:
        return redirect('login-form')
    
    