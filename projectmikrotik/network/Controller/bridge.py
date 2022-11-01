import json
from multiprocessing import context
from django.shortcuts import render, redirect
import paramiko
from librouteros import connect
from network.models import bridge as bridge_model, port as port_model,interface as interface_model, vlans as vlans_model,identity as identity_model


######################################## PART BRIDGE ########################################################################################
def bridge_list(request):
    ident=identity_model.objects.all()
    vlans=vlans_model.objects.all()
    bridge=bridge_model.objects.all()
    port=port_model.objects.all()
    return render(request,'bridge/bridge_list.html',{ 'bridge':bridge ,'port':port,'vlans':vlans,'identity':ident})
    
    
def bridge_add(request):
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
        bridge = request.POST['bridge']
        if 'filtering' not in request.POST :
            stdin, stdout, stderr = client.exec_command('/interface bridge add name='+bridge)
            return redirect('bridge-data')
        else:
            stdin, stdout, stderr = client.exec_command('/interface bridge add vlan-filtering=yes name='+bridge)
            return redirect('bridge-data')
    return render(request,'bridge/bridge_add.html')


def bridge_edit(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
    else:
        return redirect('login-form')
    data=bridge_model.objects.get(id=url)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        bridge = request.POST['bridge']
        bridge_id = request.POST['bridge_id']
        if 'filtering' not in request.POST :
            stdin, stdout, stderr = client.exec_command('/interface bridge set name='+bridge+' number='+bridge_id)
            return redirect('bridge-data')
        else:
            stdin, stdout, stderr = client.exec_command('/interface bridge set vlan-filtering=yes name='+bridge+' number='+bridge_id)
            return redirect('bridge-data')
    return render(request,'bridge/bridge_edit.html',{'bridgeedit':data})


def bridge_delete(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    data=bridge_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/interface bridge remove number='+data.bridge_id)
    data.delete()
    return redirect('bridge-list')


def bridge_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    api = connect(username=username, password=password,host=host)
    bridge_info = api(cmd="/interface/bridge/print")
    bridge_del=bridge_model.objects.all()
    bridge_del.delete()
    for bridge in bridge_info:
        if bridge['vlan-filtering'] == False:
            bridgesave = bridge_model(
            name= bridge['name'],
            typebridge='Bridge',
            actualmtu= bridge['actual-mtu'],
            l2mtu=bridge['l2mtu'],
            bridge_id=bridge['.id']
            )
        else:
            bridgesave = bridge_model(
            name= bridge['name'],
            typebridge='Bridge',
            actualmtu= bridge['actual-mtu'],
            l2mtu=bridge['l2mtu'],
            bridge_id=bridge['.id'],
            vlan=1
            )
        bridgesave.save()
    return redirect('bridge-list')







######################################## PART PORT ########################################################################################




def port_add(request):
    
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    
    interface=interface_model.objects.all()
    bridge_data=bridge_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        interface=request.POST['interface']
        bridge = request.POST['bridge']
        pvid = request.POST['pvid']
        stdin, stdout, stderr = client.exec_command('/interface bridge port add interface='+interface+' bridge='+bridge+' pvid='+pvid)
        return redirect('port-data')
    return render(request,'bridge/port_add.html',{'bridge':bridge_data,'interface':interface})


def port_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    
    
    port=port_model.objects.get(id=url)
    bridge_data=bridge_model.objects.all()
    interface=interface_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        interface=request.POST['interface']
        bridge = request.POST['bridge']
        pvid = request.POST['pvid']
        portid = request.POST['portid']
        stdin, stdout, stderr = client.exec_command('/interface bridge port set interface='+interface+' bridge='+bridge+' pvid='+pvid+' number='+portid)
        return redirect('port-data')
    return render(request,'bridge/port_edit.html',{'bridge':bridge_data,'interface':interface,'port':port})

def port_delete(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    port=port_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/interface bridge port remove  number='+port.port_id)
    port.delete()
    return redirect('bridge-list')
   

def port_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    
    api = connect(username=username, password=password,host=host)
    port_info = api(cmd="/interface/bridge/port/print")
    port_del=port_model.objects.all()
    port_del.delete()
    for port in port_info:
        # print(json.dumps(bridge, indent=4))
        portsave = port_model(
        port_id= port['.id'],
        interface=port['interface'],
        bridge= port['bridge'],
        pvid=port['pvid'],
        frametypes=port['frame-types']
        )
        portsave.save()
    return redirect('bridge-list')






######################################## PART VLANS ########################################################################################




def vlans_add(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    
    interface=interface_model.objects.all()
    bridge_data=bridge_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        if request.POST['tagged2'] == '' :
            bridge = request.POST['bridge']
            vlans = request.POST['vlans']
            tagged1 = request.POST['tagged1']
            untagged= request.POST['untagged']
            stdin, stdout, stderr = client.exec_command('/interface bridge vlan add bridge='+bridge+' vlan-ids='+vlans+' tagged='+tagged1+' untagged='+untagged)
            return redirect('vlans-data')
        else:
            bridge = request.POST['bridge']
            vlans = request.POST['vlans']
            tagged1 = request.POST['tagged1']
            tagged2 = request.POST['tagged2']
            untagged= request.POST['untagged']
            stdin, stdout, stderr = client.exec_command('/interface bridge vlan add bridge='+bridge+' vlan-ids='+vlans+' tagged='+tagged1+','+tagged2+' untagged='+untagged)
            return redirect('vlans-data')
        
    return render(request,'bridge/vlans_add.html',{'bridge':bridge_data,'interface':interface})

def vlans_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    
    vlans=vlans_model.objects.get(id=url)
    tag = vlans.tagged.split(",")
    tag1 = str(tag[0])
    tag2 = str(tag[1])
    bridge_data=bridge_model.objects.all()
    interface=interface_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        if request.POST['tagged2'] == '' :
            bridge = request.POST['bridge']
            vlans = request.POST['vlans']
            tagged1 = request.POST['tagged1']
            untagged= request.POST['untagged']
            vlansid = request.POST['vlansid']
            stdin, stdout, stderr = client.exec_command('/interface bridge vlan set bridge='+bridge+' vlan-ids='+vlans+' tagged='+tagged1+' untagged='+untagged+' number='+vlansid)
            return redirect('vlans-data')
        else:
            bridge = request.POST['bridge']
            vlans = request.POST['vlans']
            tagged1 = request.POST['tagged1']
            tagged2 = request.POST['tagged2']
            untagged= request.POST['untagged']
            vlansid = request.POST['vlansid']
            stdin, stdout, stderr = client.exec_command('/interface bridge vlan set bridge='+bridge+' vlan-ids='+vlans+' tagged='+tagged1+','+tagged2+' untagged='+untagged+' number='+vlansid)
            return redirect('vlans-data')
        
    return render(request,'bridge/vlans_edit.html',{'bridge':bridge_data,'interface':interface,'vlans':vlans,'tag1':tag1,'tag2':tag2})
    
def vlans_delete(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    vlans=vlans_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/interface bridge vlan remove  number='+vlans.vlansid)
    vlans.delete()
    return redirect('bridge-list')


def vlans_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    
    api = connect(username=username, password=password,host=host)
    vlans_info = api(cmd="/interface/bridge/vlan/print")
    vlans_del=vlans_model.objects.all()
    vlans_del.delete()
    for vlans in vlans_info:
          #print(json.dumps(vlans, indent=4))
          vlanssave = vlans_model(
            vlansid=vlans['.id'],
            vlans_bridge=vlans['bridge'],
            vlans_ids=vlans['vlan-ids'],
            tagged=vlans['tagged'],
            untagged=vlans['untagged'],
            )
          vlanssave.save()
    return redirect('bridge-list')
    