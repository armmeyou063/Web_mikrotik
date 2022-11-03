import json
from django.shortcuts import render, redirect
import paramiko
from librouteros import connect
from network.models import  identity as identity_model,interface as interface_model,pool as pool_model,serverprofile as serverprofile_model,server as server_model,userprofile as userprofile_model,users as users_model,binding as binding_model

def hotspot_list(request):
    if 'host' in request.session :
        binding=binding_model.objects.all()
        users=users_model.objects.all()
        userprofile=userprofile_model.objects.all()
        server=server_model.objects.all()
        serverprofile=serverprofile_model.objects.all()
        identity=identity_model.objects.all()
        return render(request,'hotspot/hotspot_list.html',{'identity':identity,'server':server,'serverprofile':serverprofile,'userprofile':userprofile,'users':users,'binding':binding})
    else:
        return redirect('login-form')
    

def server_add(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    interface=interface_model.objects.all()
    pool=pool_model.objects.all()
    serverprofile=serverprofile_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        name=request.POST['name']
        interface = request.POST['interface']
        pool = request.POST['pool']
        profile = request.POST['profile']
        stdin, stdout, stderr = client.exec_command('/ip hotspot add name='+name+' interface='+interface+' address-pool='+pool+' profile='+profile +' disabled=no')
        return redirect('server-data')
    return render(request,'hotspot/server_add.html',{'interface':interface,'pool':pool,'serverprofile':serverprofile})


def server_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    server=server_model.objects.get(id=url)
    interface=interface_model.objects.all()
    pool=pool_model.objects.all()
    serverprofile=serverprofile_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        name=request.POST['name']
        interface = request.POST['interface']
        address = request.POST['address']
        profile = request.POST['profile']
        server_id = request.POST['server_id']
        stdin, stdout, stderr = client.exec_command('/ip hotspot set name='+name+' interface='+interface+' address-pool='+address+' profile='+profile +' disabled=no  number='+server_id)
        return redirect('server-data')
    return render(request,'hotspot/server_edit.html',{'interface':interface,'pool':pool,'server':server,'serverprofile':serverprofile})


def server_delete(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    server=server_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/ip hotspot remove number='+server.server_id)
    server.delete()
    return redirect('hotspot-list')


def server_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    api = connect(username=username, password=password,host=host)
    server_info = api(cmd="/ip/hotspot/print")
    server_del=serverprofile_model.objects.all()
    server_del.delete()
    for server in server_info:
            #print(json.dumps(server, indent=4))
                serversave = server_model(
                server_id= server['.id'],
                server_name=server['name'],
                server_interface=server['interface'],
                server_pool=server['address-pool'],
                server_profile=server['profile'],
                )
                serversave.save()
    return redirect('hotspot-list')

############################################### Server profile ######################################################################


def serverprofile_add(request):
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
        if 'dns' not in request.POST:
             name=request.POST['name']
             address = request.POST['address']
             stdin, stdout, stderr = client.exec_command('/ip hotspot profile add  name='+name+' hotspot-address='+address)
        else:
            name=request.POST['name']
            address = request.POST['address']
            dns = request.POST['dns']
            stdin, stdout, stderr = client.exec_command('/ip hotspot profile add  name='+name+' hotspot-address='+address+' dns-name='+dns)
        return redirect('serverprofile-data')
    return render(request,'hotspot/serverprofile_add.html')
    
    
def serverprofile_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    serverprofile=serverprofile_model.objects.get(id=url)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
       print(request.POST)
       if  request.POST['dns'] == '':
             name=request.POST['name']
             address = request.POST['address']
             ser_id = request.POST['ser_id']
             stdin, stdout, stderr = client.exec_command('/ip hotspot profile set  name='+name+' hotspot-address='+address+' number='+ser_id)
       else:
            name=request.POST['name']
            address = request.POST['address']
            dns = request.POST['dns']
            ser_id =request.POST['ser_id']
            stdin, stdout, stderr = client.exec_command('/ip hotspot profile set  name='+name+' hotspot-address='+address+' dns-name='+dns+' number='+ser_id) 
       return redirect('serverprofile-data')
    return render(request,'hotspot/serverprofile_edit.html',{'serverprofile':serverprofile})
   
   
def serverprofile_delete(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    serverprofile=serverprofile_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/ip hotspot profile remove number='+serverprofile.ser_id)
    serverprofile.delete()
    return redirect('hotspot-list')


def serverprofile_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    
    api = connect(username=username, password=password,host=host)
    serverprofile_info = api(cmd="/ip/hotspot/profile/print")
    serverprofile_del=serverprofile_model.objects.all()
    serverprofile_del.delete()
    for serverprofile in serverprofile_info:
            #print(json.dumps(serverprofile, indent=4))
            dns = serverprofile['dns-name']
            if dns == '':
                serverprosave = serverprofile_model(
                ser_id= serverprofile['.id'],
                ser_name=serverprofile['name'],
                ser_address=serverprofile['hotspot-address'],
                ser_dns = ''
                )
            else:
                serverprosave = serverprofile_model(
                ser_id= serverprofile['.id'],
                ser_name=serverprofile['name'],
                ser_address=serverprofile['hotspot-address'],
                ser_dns = serverprofile['dns-name']
                )
            serverprosave.save()
    return redirect('hotspot-list')

######################################### Users ###################################################################################################


def users_add(request):
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
        if request.POST['password'] == '':
            name=request.POST['name']
            server=request.POST['server']
            profile=request.POST['profile']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user add  name='+name+' profile='+profile+' server='+server)
        else:
            name=request.POST['name']
            server=request.POST['server']
            profile=request.POST['profile']
            password=request.POST['password']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user add  name='+name+' profile='+profile+' server='+server+' password='+password)
        return redirect('users-data')
    userprofile=userprofile_model.objects.all()
    server=server_model.objects.all()
    return render(request,'hotspot/users_add.html',{'userprofile':userprofile,'server':server})


def users_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    users=users_model.objects.get(id=url)
    userprofile=userprofile_model.objects.all()
    server=server_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        if request.POST['password'] == '':
            name=request.POST['name']
            server=request.POST['server']
            profile=request.POST['profile']
            user_id = request.POST['user_id']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user set  name='+name+' profile='+profile+' server='+server+' number='+user_id)
        else:
            name=request.POST['name']
            server=request.POST['server']
            profile=request.POST['profile']
            password=request.POST['password']
            user_id = request.POST['user_id']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user set  name='+name+' profile='+profile+' server='+server+' password='+password+' number='+user_id)
        return redirect('users-data')
    return render(request,'hotspot/users_edit.html',{'userprofile':userprofile,'server':server,'users':users})

def users_delete(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    users=users_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/ip hotspot user remove number='+users.user_id)
    users.delete()
    return redirect('hotspot-list')


def users_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    api = connect(username=username, password=password,host=host)
    users_info = api(cmd="/ip/hotspot/user/print")
    users_del=users_model.objects.all()
    users_del.delete()
    for users in users_info:
        print(json.dumps(users, indent=4))
        if users.get('server') == None and users.get('profile') == None:
            print('aa')
            userssave = users_model(
            user_id= users['.id'],
            user_ser='',
            user_name=users['name'],
            user_pass='',
            user_pro=''
            )
        elif users.get('server') == None and users.get('password') == None:
            print('bb')
            userssave = users_model(
            user_id= users['.id'],
            user_ser='all',
            user_name=users['name'],
            user_pass='',
            user_pro=users['profile'],
            )
        elif users.get('server') == None and users.get('password') != None :
            print('ccc')
            userssave = users_model(
            user_id= users['.id'],
            user_ser='all',
            user_name=users['name'],
            user_pass=users['password'],
            user_pro=users['profile'],
            )
        else:
            print('ddd')
            userssave = users_model(
            user_id= users['.id'],
            user_ser=users['server'],
            user_name=users['name'],
            user_pass=users['password'],
            user_pro=users['profile'],
            )
        userssave.save()
    return redirect('hotspot-list')


######################################### Users Profile ###################################################################################################



def userprofile_add(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    pool=pool_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        print(request.POST)
        if request.POST['address'] == '' and request.POST['rate'] == '':
            name=request.POST['name']
            share=request.POST['share']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user profile add  name='+name+' shared-users='+share)
        elif request.POST['address'] != '' and request.POST['rate'] == '':
            name=request.POST['name']
            address=request.POST['address']
            share=request.POST['share']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user profile add  name='+name+' address-pool='+address+' shared-users='+share)
        elif request.POST['address'] == '' and request.POST['rate'] != '':
            name=request.POST['name']
            share=request.POST['share']
            rate=request.POST['rate']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user profile add  name='+name+' shared-users='+share+' rate-limit='+rate)
        else:
            name=request.POST['name']
            share=request.POST['share']
            address=request.POST['address']
            rate=request.POST['rate']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user profile add  name='+name+' shared-users='+share+' address-pool='+address+' rate-limit='+rate)
        return redirect('userprofile-data')
    
    return render(request,'hotspot/userprofile_add.html',{'pool':pool})
    

def userprofile_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    userprofile=userprofile_model.objects.get(id=url)
    pool=pool_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        print(request.POST)
        if request.POST['address'] == '' and request.POST['rate'] == '':
            name=request.POST['name']
            share=request.POST['share']
            userpro_id=request.POST['userpro_id']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user profile set  name='+name+' shared-users='+share+' number='+userpro_id)
        elif request.POST['address'] != '' and request.POST['rate'] == '':
            name=request.POST['name']
            address=request.POST['address']
            share=request.POST['share']
            userpro_id=request.POST['userpro_id']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user profile set  name='+name+' address-pool='+address+' shared-users='+share+' number='+userpro_id)
        elif request.POST['address'] == '' and request.POST['rate'] != '':
            name=request.POST['name']
            share=request.POST['share']
            rate=request.POST['rate']
            userpro_id=request.POST['userpro_id']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user profile set  name='+name+' shared-users='+share+' rate-limit='+rate+' number='+userpro_id)
        else:
            name=request.POST['name']
            share=request.POST['share']
            address=request.POST['address']
            rate=request.POST['rate']
            userpro_id=request.POST['userpro_id']
            stdin, stdout, stderr = client.exec_command('/ip hotspot user profile set  name='+name+' shared-users='+share+' address-pool='+address+' rate-limit='+rate+' number='+userpro_id)
        return redirect('userprofile-data')
    return render(request,'hotspot/userprofile_edit.html',{'pool':pool,'userprofile':userprofile})


def userprofile_delete(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    userprofile=userprofile_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/ip hotspot user profile remove number='+userprofile.userpro_id)
    userprofile.delete()
    return redirect('hotspot-list')


def userprofile_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    
    api = connect(username=username, password=password,host=host)
    userprofile_info = api(cmd="/ip/hotspot/user/profile/print")
    userprofile_del=userprofile_model.objects.all()
    userprofile_del.delete()
    for userprofile in userprofile_info:
        
        if userprofile.get('address-pool') == None and userprofile.get('rate-limit') == None:
            #print('111')
            userprosave = userprofile_model(
            userpro_id= userprofile['.id'],
            userpro_name=userprofile['name'],
            userpro_share=userprofile['shared-users'],
            userpro_address='',
            userpro_rate=''
            )
            userprosave.save()
        elif userprofile.get('address-pool') != None and  userprofile.get('rate-limit') == None:
            #print('222')
            userprosave = userprofile_model(
            userpro_id= userprofile['.id'],
            userpro_name=userprofile['name'],
            userpro_share=userprofile['shared-users'],
            userpro_address=userprofile['address-pool'],
            userpro_rate='',
            )
            userprosave.save()
        elif userprofile.get('address-pool') == None and userprofile.get('rate-limit') != None:
            #print('333')
            userprosave = userprofile_model(
            userpro_id= userprofile['.id'],
            userpro_name=userprofile['name'],
            userpro_share=userprofile['shared-users'],
            userpro_address='',
            userpro_rate=userprofile['rate-limit'],
            )
            userprosave.save()
        else:
            #print('444')
            userprosave = userprofile_model(
            userpro_id= userprofile['.id'],
            userpro_name=userprofile['name'],
            userpro_share=userprofile['shared-users'],
            userpro_address=userprofile['address-pool'],
            userpro_rate=userprofile['rate-limit'],
            )
            userprosave.save()
    return redirect('hotspot-list')
 
 
 ######################################### IP Binding ###################################################################################################


def binding_add(request):
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
        if request.POST['address'] == '':
            mac_address=request.POST['mac_address']
            server=request.POST['server']
            typebinding=request.POST['typebinding']
            stdin, stdout, stderr = client.exec_command('/ip hotspot ip-binding add mac-address='+mac_address+' server='+server+' type='+typebinding)
        else:
            mac_address=request.POST['mac_address']
            server=request.POST['server']
            typebinding=request.POST['typebinding']
            address=request.POST['address']
            stdin, stdout, stderr = client.exec_command('/ip hotspot ip-binding add mac-address='+mac_address+' server='+server+' type='+typebinding+' address='+address)
        return redirect('binding-data')
    server=server_model.objects.all()
    return render(request,'hotspot/binding_add.html',{'server':server})

def binding_edit(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    binding=binding_model.objects.get(id=url)
    server=server_model.objects.all()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    if request.method == 'POST':
        if request.POST['address'] == '':
            mac_address=request.POST['mac_address']
            server=request.POST['server']
            typebinding=request.POST['typebinding']
            binding_id = request.POST['binding_id']
            stdin, stdout, stderr = client.exec_command('/ip hotspot ip-binding set mac-address='+mac_address+' server='+server+' type='+typebinding+' number='+binding_id)
        else:
            binding_id = request.POST['binding_id']
            mac_address=request.POST['mac_address']
            server=request.POST['server']
            typebinding=request.POST['typebinding']
            address=request.POST['address']
            stdin, stdout, stderr = client.exec_command('/ip hotspot ip-binding set mac-address='+mac_address+' server='+server+' type='+typebinding+' address='+address+' number='+binding)
        return redirect('binding-data')
    return render(request,'hotspot/binding_edit.html',{'server':server,'binding':binding})


def binding_delete(request,url):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    binding=binding_model.objects.get(id=url)
    stdin, stdout, stderr = client.exec_command('/ip hotspot ip-binding remove number='+binding.binding_id)
    binding.delete()
    return redirect('hotspot-list')


def binding_data(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')
    api = connect(username=username, password=password,host=host)
    binding_info = api(cmd="/ip/hotspot/ip-binding/print")
    binding_del=binding_model.objects.all()
    binding_del.delete()
    for binding in binding_info:
        print(json.dumps(binding, indent=4))
        if binding.get('server') == None and binding.get('address') == None:
            #print('aaa')
            bindingsave = binding_model(
            binding_id= binding['.id'],
            binding_mac=binding['mac-address'],
            binding_ser='all',
            binding_type=binding['type'],
            binding_address=''
            )
        elif binding.get('server') == None and binding.get('address') != None:
            #print('bbb')
            bindingsave = binding_model(
            binding_id= binding['.id'],
            binding_mac=binding['mac-address'],
            binding_ser='all',
            binding_type=binding['type'],
            binding_address=binding['address']
            )
        elif binding.get('server') != None and binding.get('address') == None:
            #print('ccc')
            bindingsave = binding_model(
            binding_id= binding['.id'],
            binding_mac=binding['mac-address'],
            binding_ser=binding['server'],
            binding_type=binding['type'],
            binding_address=''
            )
        else:
            #print('ddd')
            bindingsave = binding_model(
            binding_id= binding['.id'],
            binding_mac=binding['mac-address'],
            binding_ser=binding['server'],
            binding_type=binding['type'],
            binding_address=binding['address']
            )
        bindingsave.save()
    return redirect('hotspot-list')