from django.shortcuts import render, redirect
import json
import paramiko
from librouteros import connect
from network.models import  interface as interface_model ,ethernet as ethernet_model , vlan as vlan_model  , bridge as bridge_model,dhcpclient as dhcpclient_model,dhcpserver as dhcpserver_model,dns as dns_model,connection as firewall_model,serverprofile as serverprofile_model,server as server_model,users as users_model, userprofile as userprofile_model,binding as binding_model,ipaddress as ipaddress_model,pool as pool_model,route as route_model,user as user_model,identity as identity_model


def loginform(request):
    return render(request, 'login/login.html',)


def login(request):
    if 'host' in request.session :
         host = request.session['host']
         username = request.session['username']
         password = request.session['password']
    else:
        return redirect('login-form')

    request.session['host'] = host
    request.session['username'] = username
    request.session['password'] = password
    
    api = connect(username=username, password=password,host=host)
    ##################### Bridge ######################################
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
    ##################### dhcp Client ######################################
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
     ##################### dhcp server ######################################
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
    #####################  dns ######################################    
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
    #####################  firewall ######################################    
    connection_info = api(cmd="/ip/firewall/connection/print")
    firewall_del=firewall_model.objects.all()
    firewall_del.delete()
    for con in connection_info:
            print(json.dumps(con, indent=4))
            dnssave = firewall_model(
            con_id= con['.id'],
            protocal=con['protocol'],
            src=con['src-address'],
            dst=con['dst-address'],
            reply_src=con['reply-src-address'],
            reply_dst=con['reply-dst-address'],
            repl_byte=con['repl-bytes'],
            repl_packet=con['repl-packets'],
            orig_packet=con['orig-packets'],
            orig_byte=con['orig-bytes']
            )
            dnssave.save()
     ##################### hotspot server ######################################
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
   ##################### hotspot serverprofile ######################################
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
    ##################### hotspot users ######################################  
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
    ##################### hotspot users profile ######################################     
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
     ##################### hotspot ip binding ######################################   
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
    ##################### interface  ###################################### 
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
    ##################### interface vlan ######################################   
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
    #####################  ip  ###################################### 
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
    #####################  ip pool  ###################################### 
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
    #####################  ip route  ###################################### 
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
    #####################  user  ###################################### 
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
    #####################  identity  ###################################### 
    identity_info = api(cmd="/system/identity/print")
    identity_del=identity_model.objects.all()
    identity_del.delete()
    for identity in identity_info:
            #print(json.dumps(user, indent=4))
            identitysave = identity_model(
            name=identity['name'],
            )
            identitysave.save()
    return redirect('interface-list')

def logout(request):
    del request.session['host']
    del request.session['username'] 
    del request.session['password'] 
    return redirect('login-form')