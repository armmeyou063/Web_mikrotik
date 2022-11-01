
import json
from django.shortcuts import render, redirect
import paramiko
from librouteros import connect
from network.models import  identity as identity_model,user as user_model,identity as identity_model



######################################## PART IP Route ########################################################################################


def user_list(request):
    user=user_model.objects.all()
    identity=identity_model.objects.all()
    return render(request,'system/user_list.html',{'user':user,'identity':identity})


def user_add(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        if 'password' not in request.POST:
            name=request.POST['name']
            group = request.POST['group']
            stdin, stdout, stderr = client.exec_command('/user add name='+name+' group='+group)
            return redirect('user-data')  
        else:
            name=request.POST['name']
            group = request.POST['group']
            password=request.POST['password']
            stdin, stdout, stderr = client.exec_command('/user add name='+name+' group='+group+' password='+password)
            return redirect('user-data')  
    return render(request,'system/user_add.html')


def user_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    user=user_model.objects.get(id=url)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        if request.POST['password'] == '':
            print("1111111")
            name=request.POST['name']
            group = request.POST['group']
            name_id =request.POST['name_id']
            stdin, stdout, stderr = client.exec_command('/user set name='+name+' group='+group+' number='+name_id)
            return redirect('user-data')  
        else:
            name=request.POST['name']
            group = request.POST['group']
            password=request.POST['password']
            name_id =request.POST['name_id']
            stdin, stdout, stderr = client.exec_command('/user set name='+name+' group='+group+' password='+password+' number='+name_id)
            return redirect('user-data')  
    return render(request,'system/user_edit.html',{'user':user})


def user_delete(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    user=user_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/user remove number='+user.user_id)
    user.delete()
    return redirect('user-list') 


def user_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    api = connect(username=username, password=password,host=host)
    user_info = api(cmd="/user/print")
    user_del=user_model.objects.all()
    user_del.delete()
    for user in user_info:
            #print(json.dumps(user, indent=4))
            usersave = user_model(
            user_id= user['.id'],
            name=user['name'],
            group=user['group']
            )
            usersave.save()
    return redirect('user-list')

####################################### system identity ########################################################################################

def identity_list(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    api = connect(username=username, password=password,host=host)
    identity_info = api(cmd="/system/identity/print")
    identity_del=identity_model.objects.all()
    identity_del.delete()
    for identity in identity_info:
            #print(json.dumps(user, indent=4))
            identitysave = identity_model(
            name=identity['name'],
            )
            identitysave.save()
    identity=identity_model.objects.all()
    return render(request,'system/identity_list.html',{'identity':identity})


def identity_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    identity=identity_model.objects.get(id=url)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
            name = request.POST['name']
            stdin, stdout, stderr = client.exec_command('/system  identity set name='+name)
            return redirect('identity-data')  
    return render(request,'system/identity_edit.html',{'identity':identity})


def identity_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    api = connect(username=username, password=password,host=host)
    identity_info = api(cmd="/system/identity/print")
    identity_del=identity_model.objects.all()
    identity_del.delete()
    for identity in identity_info:
            #print(json.dumps(user, indent=4))
            identitysave = identity_model(
            name=identity['name'],
            )
            identitysave.save()
    return redirect('identity-list')

####################################### system reboot ########################################################################################
    
    
def reboot(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    stdin, stdout, stderr = client.exec_command('/system reboot')
    return redirect('login-form')


def shutdown(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    stdin, stdout, stderr = client.exec_command('/system shutdown')
    return redirect('login-form')