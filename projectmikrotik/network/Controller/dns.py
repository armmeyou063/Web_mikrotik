
import json
from django.shortcuts import render, redirect
import paramiko
from librouteros import connect
from network.models import  dns as dns_model,identity as identity_model

def dns_list(request):
    dns=dns_model.objects.all()
    return render(request,'dns/dns_list.html',{'dns':dns})


def dns_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    dns=dns_model.objects.get(id=url)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        if 'allow' not in request.POST:
            servers=request.POST['servers']
            dynamic = request.POST['dynamic']
            stdin, stdout, stderr = client.exec_command('/ip dns set  server='+servers+' allow-remote-requests=no')
            return redirect('dns-data')  
        else:
            servers=request.POST['servers']
            dynamic = request.POST['dynamic']
            allow= request.POST['allow']
            stdin, stdout, stderr = client.exec_command('/ip dns set  server='+servers+' allow-remote-requests=yes')
            return redirect('dns-data') 
    identity=identity_model.objects.all()
    return render(request,'dns/dns_edit.html',{'dns':dns,'identity':identity})


def dns_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    api = connect(username=username, password=password,host=host)
    dns_info = api(cmd="/ip/dns/print")
    dns_del=dns_model.objects.all()
    dns_del.delete()
    for dns in dns_info:
            #print(json.dumps(dns, indent=4))
            dnssave = dns_model(
            server= dns['servers'],
            dynamic=dns['dynamic-servers'],
            allow=dns['allow-remote-requests']
            )
            dnssave.save()
    return redirect('dns-list')