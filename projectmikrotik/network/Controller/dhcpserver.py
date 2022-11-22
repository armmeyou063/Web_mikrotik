import json
from django.shortcuts import render, redirect
import paramiko
from librouteros import connect
from network.models import interface as interface_model, dhcpserver as dhcpserver_model,pool as pool_model, dhcpnetwork as  dhcpnetwork_model,dhcplease as dhcplease_model,identity as identity_model



######################################## PART DHCP SERVER ########################################################################################


def dhcpserver_list(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        api = connect(username=username, password=password,host=host)
        dhcplease_info = api(cmd="/ip/dhcp-server/lease/print")
        dhcplease_del=dhcplease_model.objects.all()
        dhcplease_del.delete()
        for dhcplease in dhcplease_info:
            #print(json.dumps(dhcplease, indent=4))
            dhcpleasesave = dhcplease_model(
            dhcp_id=dhcplease['.id'],
            address=dhcplease['address'],
            mac_address=dhcplease['mac-address'],
            status=dhcplease['status'],
            dhcpserver=dhcplease['server']
            )
            dhcpleasesave.save()
        dhcplease=dhcplease_model.objects.all()
        identity=identity_model.objects.all()
        dhcpnetwork=dhcpnetwork_model.objects.all()
        dhcpserver=dhcpserver_model.objects.all()
        return render(request,'ip/dhcpserver_list.html',{'dhcpserver':dhcpserver,'dhcpnetwork':dhcpnetwork,'dhcplease':dhcplease,'identity':identity})
    else:
        return redirect('login-form')
    


def dhcpserver_add(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        if request.method == 'POST':
            name=request.POST['name']
            interface = request.POST['interface']
            address = request.POST['address']
            stdin, stdout, stderr = client.exec_command('/ip dhcp-server add name='+name+' interface='+interface+' address-pool='+address+' disabled=no')
            return redirect('dhcpserver-data')  
        interface=interface_model.objects.all()
        ippool=pool_model.objects.all()
        return render(request,'ip/dhcpserver_add.html',{'interface':interface,'ippool':ippool})
    else:
        return redirect('login-form')
    


def dhcpserver_edit(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        dhcpserver=dhcpserver_model.objects.get(id=url)
        interface=interface_model.objects.all()
        ippool=pool_model.objects.all()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        if request.method == 'POST':
            name=request.POST['name']
            interface = request.POST['interface']
            address = request.POST['address']
            dhcp_id = request.POST['dhcp_id']
            stdin, stdout, stderr = client.exec_command('/ip dhcp-server set name='+name+' interface='+interface+' address-pool='+address+' disabled=no  number='+dhcp_id)
            return redirect('dhcpserver-data')  
        return render(request,'ip/dhcpserver_edit.html',{'interface':interface,'ippool':ippool,'dhcpserver':dhcpserver})
    else:
        return redirect('login-form')
    


def dhcpserver_delete(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        dhcpserver=dhcpserver_model.objects.get(id=url)
        stdin, stdout, stderr = client.exec_command('/ip dhcp-server remove number='+dhcpserver.dhcp_id)
        dhcpserver.delete()
        return redirect('dhcpserver-list')
    else:
        return redirect('login-form')
    
   

def dhcpserver_data(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        api = connect(username=username, password=password,host=host)
        dhcpserver_info = api(cmd="/ip/dhcp-server/print")
        dhcpserver_del=dhcpserver_model.objects.all()
        dhcpserver_del.delete()
        for dhcpserver in dhcpserver_info:
            #print(json.dumps(dhcpserver, indent=4))
            dhcpserver = dhcpserver_model(
            dhcp_id= dhcpserver['.id'],
            name=dhcpserver['name'],
            interface=dhcpserver['interface'],
            address_pool= dhcpserver['address-pool'],
            )
            dhcpserver.save()
        return redirect('dhcpserver-list')
    else:
        return redirect('login-form')
    
    
    
######################################## PART DHCP NETWORK ########################################################################################




def dhcpnetwork_add(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        if request.method == 'POST':
            if 'dns' not in request.POST:
                address=request.POST['address']
                gateway = request.POST['gateway']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-server network add address='+address+' gateway='+gateway)
                return redirect('dhcpnetwork-data')  
            else:
                address=request.POST['address']
                gateway = request.POST['gateway']
                dns = request.POST['dns']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-server network add address='+address+' gateway='+gateway+' dns-server='+dns)
                return redirect('dhcpnetwork-data')  
        return render(request,'ip/dhcpnetwork_add.html')
    else:
        return redirect('login-form')
    
    
    

def dhcpnetwork_edit(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        dhcpnetwork=dhcpnetwork_model.objects.get(id=url)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        if request.method == 'POST':
            if 'dns' not in request.POST:
                address=request.POST['address']
                gateway = request.POST['gateway']
                dhcp_id = request.POST['dhcp_id']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-server network set address='+address+' gateway='+gateway+' number='+dhcp_id)
                return redirect('dhcpnetwork-data')  
            else:
                address=request.POST['address']
                gateway = request.POST['gateway']
                dns = request.POST['dns']
                dhcp_id = request.POST['dhcp_id']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-server network set address='+address+' gateway='+gateway+' dns-server='+dns+' number='+dhcp_id)
                return redirect('dhcpnetwork-data')  
        return render(request,'ip/dhcpnetwork_edit.html',{'dhcpnetwork':dhcpnetwork})
    else:
        return redirect('login-form')
    
    

def dhcpnetwork_delete(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        dhcpnetwork=dhcpnetwork_model.objects.get(id=url)
        stdin, stdout, stderr = client.exec_command('/ip dhcp-server network remove number='+dhcpnetwork.dhcp_id)
        dhcpnetwork.delete()
        return redirect('dhcpserver-list')
    else:
        return redirect('login-form')
    
    
   

def dhcpnetwork_data(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        api = connect(username=username, password=password,host=host)
        dhcpnetwork_info = api(cmd="/ip/dhcp-server/network/print")
        dhcpnetwork_del=dhcpnetwork_model.objects.all()
        dhcpnetwork_del.delete()
        for dhcpnetwork in dhcpnetwork_info:
            print(json.dumps(dhcpnetwork, indent=4))
            dhcpnetworkserver = dhcpnetwork_model(
            dhcp_id=dhcpnetwork['.id'],
            address=dhcpnetwork['address'],
            gateway=dhcpnetwork['gateway'],
            dns=dhcpnetwork['dns-server'],
            )
            dhcpnetworkserver.save()
        return redirect('dhcpserver-list')
    else:
        return redirect('login-form')
    
    