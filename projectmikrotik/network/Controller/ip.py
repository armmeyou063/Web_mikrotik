import json
from multiprocessing import context
from django.shortcuts import render, redirect
import paramiko
from librouteros import connect
from network.models import interface as interface_model, ipaddress as ipaddress_model,identity as identity_model

######################################## PART Address ########################################################################################


def address_list(request):
    address=ipaddress_model.objects.all()
    identity=identity_model.objects.all()
    return render(request,'ip/address_list.html',{'address':address,'identity':identity})


def address_add(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    interface=interface_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        address=request.POST['address']
        network = request.POST['network']
        interface = request.POST['interface']
        stdin, stdout, stderr = client.exec_command('/ip address add address='+address+' network='+network+' interface='+interface)
        return redirect('address-data')
    return render(request,'ip/address_add.html',{'interface':interface})



def address_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    address=ipaddress_model.objects.get(id=url)
    interface=interface_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        address=request.POST['address']
        network = request.POST['network']
        interface = request.POST['interface']
        address_id = request.POST['address_id']
        stdin, stdout, stderr = client.exec_command('/ip address set address='+address+' network='+network+' interface='+interface+' number='+address_id)
        return redirect('address-data')
    return render(request,'ip/address_edit.html',{'interface':interface,'address':address})
    



def address_delete(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    address=ipaddress_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/ip address remove number='+address.address_id)
    address.delete()
    return redirect('address-list') 
    

def address_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    api = connect(username=username, password=password,host=host)
    ipaddress_info = api(cmd="/ip/address/print")
    ipaddress_del=ipaddress_model.objects.all()
    ipaddress_del.delete()
    for ipaddress in ipaddress_info:
        #print(json.dumps(ipaddress, indent=4))
        ipaddresssave = ipaddress_model(
        address_id= ipaddress['.id'],
        address=ipaddress['address'],
        network= ipaddress['network'],
        interface=ipaddress['interface'],
        dynamic=ipaddress['dynamic']
        )
        ipaddresssave.save()
    return redirect('address-list')


