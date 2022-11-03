from django.shortcuts import render, redirect
import paramiko
from librouteros import connect
from network.models import pool as pool_model,identity as identity_model



######################################## PART IP POOL ########################################################################################

def ippool_list(request):
    if 'host' in request.session :
        ippool=pool_model.objects.all()
        identity=identity_model.objects.all()
        return render(request,'ip/pool_list.html',{'ippool':ippool,'identity':identity})
    else:
        return redirect('login-form')

    


def ippool_add(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        if request.method == 'POST':
            name=request.POST['name']
            address = request.POST['address']
            stdin, stdout, stderr = client.exec_command('/ip pool add name='+name+' ranges='+address)
            return redirect('pool-data')  
        return render(request,'ip/pool_add.html')
    else:
        return redirect('login-form')
    


def ippool_edit(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        ippool=pool_model.objects.get(id=url)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        if request.method == 'POST':
            name=request.POST['name']
            address = request.POST['address']
            pool_id = request.POST['pool_id']
            stdin, stdout, stderr = client.exec_command('/ip pool set name='+name+' ranges='+address+'  number='+pool_id)
            return redirect('pool-data')  
        return render(request,'ip/pool_edit.html',{'ippool':ippool})
    else:
        return redirect('login-form')
    


def ippool_delete(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        ippool=pool_model.objects.get(id=url)
        stdin, stdout, stderr = client.exec_command('/ip pool remove number='+ippool.pool_id)
        ippool.delete()
        return redirect('pool-list') 
    else:
        return redirect('login-form')
    


def ippool_data(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        api = connect(username=username, password=password,host=host)
        ippool_info = api(cmd="/ip/pool/print")
        ippool_del=pool_model.objects.all()
        ippool_del.delete()
        for ippool in ippool_info:
            #print(json.dumps(ippool, indent=4))
            ippoolsave = pool_model(
            pool_id= ippool['.id'],
            pool_name=ippool['name'],
            pool_address=ippool['ranges'],
            )
            ippoolsave.save()
        ippool=pool_model.objects.all()
        return redirect('pool-list')
    else:
        return redirect('login-form')
    
    