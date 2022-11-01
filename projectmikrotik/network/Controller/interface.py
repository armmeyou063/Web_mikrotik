import json
from django.shortcuts import render, redirect
from librouteros import connect
import paramiko
from network.models import interface as interface_model , ethernet as ethernet_model , vlan as vlan_model,identity as identity_model


######################################## PART INTERFACE ########################################################################################
def interface_list(request):
    vlan=vlan_model.objects.all()
    ether=ethernet_model.objects.all()
    interface=interface_model.objects.all()
    identity=identity_model.objects.all()
    return render(request,'interface/interface_list.html',{'interface':interface,'ether':ether,'vlan':vlan,'identity':identity})
  
  
def interface_edit(request,url):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
    else:
        return redirect('login-form')
    data=interface_model.objects.get(id=url)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        interface_name = request.POST['interface_name']
        interface_id = request.POST['interface_id']
        stdin, stdout, stderr = client.exec_command('/interface set  name='+interface_name+' number='+interface_id)
        return redirect('interface-data')
    return render(request,'interface/interface_edit.html',{'interfaceedit':data})
  
  

def interface_data(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
    else:
        return redirect('login-form')
    api = connect(username=username, password=password,host=host)
    interface_info = api(cmd="/interface/print")
    interface_del=interface_model.objects.all()
    interface_del.delete()
    for interface in interface_info:
          # print(json.dumps(interface, indent=4))
          interfacesave = interface_model(
            interface_id=interface['.id'],
            interface_name=interface['name'],
            typeinterface=interface['type'],
            actualmtu=interface['actual-mtu'],
            l2mtu=interface['l2mtu'],
            )
          interfacesave.save()
    return redirect('interface-list')
    

######################################## PART VLAN ########################################################################################

def vlan_add(request):
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
        interface=request.POST['interface']
        vlan_name = request.POST['vlan_name']
        vlan_id = request.POST['vlan_id']
        stdin, stdout, stderr = client.exec_command('/interface vlan add name='+vlan_name+' vlan-id='+vlan_id+' interface='+interface)
        return redirect('vlan-data')  
  interface=interface_model.objects.all()
  return render(request,'interface/vlan_add.html',{'interface':interface})


def vlan_edit(request,url):
  if 'host' in request.session :
      host = request.session['host']
      username = request.session['username']
      password = request.session['password']
  else:
      return redirect('login-form')
  vlan=vlan_model.objects.get(id=url)
  interface=interface_model.objects.all()
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(host, username=username, password=password)
  if request.method == 'POST':
        interface=request.POST['interface']
        vlan_name = request.POST['vlan_name']
        vlan_id = request.POST['vlan_id']
        vlanid = request.POST['vlanid']
        stdin, stdout, stderr = client.exec_command('/interface vlan set interface='+interface+' name='+vlan_name+' vlan-id='+vlan_id+' number='+vlanid)
        return redirect('vlan-data')  
  return render(request,'interface/vlan_edit.html',{'interface':interface,'vlanedit':vlan})
    
    
def vlan_delete(request,url):
    
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    vlan=vlan_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/interface vlan remove number='+vlan.vlanid)
    vlan.delete()
    return redirect('interface-list')
  
  
def vlan_data(request):
  if 'host' in request.session :
      host = request.session['host']
      username = request.session['username']
      password = request.session['password']
  else:
      return redirect('login-form')
  api = connect(username=username, password=password,host=host)
  vlan_info = api(cmd="/interface/vlan/print")
  vlan_del=vlan_model.objects.all()
  vlan_del.delete()
  if vlan_info:
      for vlan in vlan_info:
          #print(json.dumps(vlan, indent=4)) 
          vlansave = vlan_model(
          vlanid=vlan['.id'],
          vlan_name=vlan['name'],
          vlan_id=vlan['vlan-id'],
          vlan_interface=vlan['interface'],
          vlan_type='vlan',
          )
          vlansave.save()
  return redirect('interface-list')
      