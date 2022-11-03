from django.shortcuts import render, redirect
import paramiko
from librouteros import connect
from network.models import interface as interface_model, dhcpclient as dhcpclient_model, dhcpclienttype as dhcpclienttype_model,identity as identity_model



######################################## PART DHCP Client ########################################################################################

def dhcpclient_list(request):
    if 'host' in request.session :
        identity=identity_model.objects.all()
        dhcpclient=dhcpclient_model.objects.all()
        return render(request,'ip/dhcpclient_list.html',{'dhcpclient':dhcpclient,'identity':identity})
    else:
        return redirect('login-form')
    
    

def dhcpclient_add(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        typedhcp=dhcpclienttype_model.objects.all()
        interface=interface_model.objects.all()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        if request.method == 'POST':
            if 'dns' not in request.POST and 'ntp' in request.POST:
                interface=request.POST['interface']
                route = request.POST['route']
                ntp = request.POST['ntp']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-client add interface='+interface+' use-peer-dns=no  use-peer-ntp=yes add-default-route='+route+' disabled=no')
                return redirect('dhcpclient-data')
            elif 'ntp' not in request.POST and 'dns' in request.POST:
                interface=request.POST['interface']
                route = request.POST['route']
                dns = request.POST['dns']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-client add interface='+interface+' use-peer-dns=yes  use-peer-ntp=no add-default-route='+route+' disabled=no')
                return redirect('dhcpclient-data')
            elif 'dns' not in request.POST and 'ntp' not in request.POST :
                interface=request.POST['interface']
                route = request.POST['route']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-client add interface='+interface+' use-peer-dns=no  use-peer-ntp=no add-default-route='+route+' disabled=no')
                return redirect('dhcpclient-data')
            else:
                interface=request.POST['interface']
                route = request.POST['route']
                dns = request.POST['dns']
                ntp = request.POST['ntp']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-client add interface='+interface+' use-peer-dns='+dns+'  use-peer-ntp='+ntp+' add-default-route='+route+' disabled=no')
                return redirect('dhcpclient-data')
        return render(request,'ip/dhcpclient_add.html',{'interface':interface,'dhcptype':typedhcp})
    else:
        return redirect('login-form')
    
    

def dhcpclient_edit(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        typedhcp=dhcpclienttype_model.objects.all()
        dhcpclient=dhcpclient_model.objects.get(id=url)
        interface=interface_model.objects.all()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        if request.method == 'POST':
            if 'dns' not in request.POST and 'ntp' in request.POST:
                interface=request.POST['interface']
                route = request.POST['route']
                ntp = request.POST['ntp']
                dhcp_id = request.POST['dhcp_id']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-client set interface='+interface+' use-peer-dns=no  use-peer-ntp=yes add-default-route='+route+' disabled=no'+' number='+dhcp_id)
                return redirect('dhcpclient-data')
            elif 'ntp' not in request.POST and 'dns' in request.POST:
                interface=request.POST['interface']
                route = request.POST['route']
                dns = request.POST['dns']
                dhcp_id = request.POST['dhcp_id']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-client set interface='+interface+' use-peer-dns=yes  use-peer-ntp=no add-default-route='+route+' disabled=no'+' number='+dhcp_id)
                return redirect('dhcpclient-data')
            elif 'dns' not in request.POST and 'ntp' not in request.POST :
                interface=request.POST['interface']
                route = request.POST['route']
                dhcp_id = request.POST['dhcp_id']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-client set interface='+interface+' use-peer-dns=no  use-peer-ntp=no add-default-route='+route+' disabled=no'+' number='+dhcp_id)
                return redirect('dhcpclient-data')
            else:
                interface=request.POST['interface']
                route = request.POST['route']
                dhcp_id = request.POST['dhcp_id']
                dns = request.POST['dns']
                ntp = request.POST['ntp']
                stdin, stdout, stderr = client.exec_command('/ip dhcp-client set interface='+interface+' use-peer-dns='+dns+'  use-peer-ntp='+ntp+' add-default-route='+route+' disabled=no'+' number='+dhcp_id)
                return redirect('dhcpclient-data')
        return render(request,'ip/dhcpclient_edit.html',{'interface':interface,'dhcpclient':dhcpclient,'dhcptype':typedhcp})
    else:
        return redirect('login-form')
    
    

def dhcpclient_delete(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        dhcpclient=dhcpclient_model.objects.get(id=url)
        stdin, stdout, stderr = client.exec_command('/ip dhcp-client remove number='+dhcpclient.dhcp_id)
        dhcpclient.delete()
        return redirect('dhcpclient-list') 
    else:
        return redirect('login-form')
    
   

def dhcpclient_data(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        api = connect(username=username, password=password,host=host)
        dhcpclient_info = api(cmd="/ip/dhcp-client/print")
        dhcpclient_del=dhcpclient_model.objects.all()
        dhcpclient_del.delete()
        for dhcpclient in dhcpclient_info:
            #print(json.dumps(dhcpclient, indent=4))
            dhcpclientsave = dhcpclient_model(
            dhcp_id= dhcpclient['.id'],
            interface=dhcpclient['interface'],
            address=dhcpclient['address'],
            status= dhcpclient['status'],
            route=dhcpclient['add-default-route'],
            dns=dhcpclient['use-peer-dns'],
            ntp=dhcpclient['use-peer-ntp']
            )
            dhcpclientsave.save()
        return redirect('dhcpclient-list')
    else:
        return redirect('login-form')
    

    