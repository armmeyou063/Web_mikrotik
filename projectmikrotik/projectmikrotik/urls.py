"""projectmikrotik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import ipaddress
from django.contrib import admin
from django.urls import path
from network.Controller import dashboard, interface ,bridge, ip,login,dhcpclient,dhcpserver,ippool,route,system,dns,firewall,hotspot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard.Dashboard),
    #login
    path('loginform/',login.loginform,name='login-form'),
    path('login/',login.login,name='login'),
    path('logout/',login.logout,name='logout'),
    #Interface
    path('interface/',interface.interface_list,name='interface-list'),
    path('interface/edit/<int:url>',interface.interface_edit,name='interface-edit'),
    path('interface/data',interface.interface_data,name='interface-data'),
    #VLAN
    path('vlan/add',interface.vlan_add , name='vlan-add'),
    path('vlan/edit/<int:url>',interface.vlan_edit , name='vlan-edit'),
    path('vlan/delete/<int:url>',interface.vlan_delete,name='vlan-delete'),
    path('vlan/data',interface.vlan_data,name='vlan-data'),
    #Bridge
    path('bridge/',bridge.bridge_list, name='bridge-list'),
    path('bridge/add',bridge.bridge_add, name='bridge-add'),
    path('bridge/edit/<int:url>/',bridge.bridge_edit,name='bridge-edit'),
    path('bridge/delete/<int:url>',bridge.bridge_delete, name='bridge-delete'),
    path('bridge/data',bridge.bridge_data, name='bridge-data'),
    #Bridge Port
    path('port/add',bridge.port_add ,name='port-add'),
    path('port/edit/<int:url>/',bridge.port_edit, name='port-edit'),
    path('port/delete/<int:url>/',bridge.port_delete, name='port-delete'),
    path('port/data',bridge.port_data, name='port-data'),
    #Bridge Vlans
    path('vlans/add',bridge.vlans_add,name='vlans-add'),
    path('vlans/edit/<int:url>/',bridge.vlans_edit,name='vlans-edit'),
    path('vlans/delete/<int:url>/',bridge.vlans_delete,name='vlans-delete'),
    path('vlans/data',bridge.vlans_data,name='vlans-data'),
    #IP Address
    path('address/',ip.address_list,name='address-list'),
    path('address/add',ip.address_add,name='address-add'),
    path('address/edit/<int:url>/',ip.address_edit,name='address-edit'),
    path('address/delete/<int:url>',ip.address_delete,name='address-delete'),
    path('address/data',ip.address_data,name='address-data'),
    #DHCP Client
    path('dhcpclient/',dhcpclient.dhcpclient_list,name='dhcpclient-list'),
    path('dhcpclient/add',dhcpclient.dhcpclient_add,name='dhcpclient-add'),
    path('dhcpclient/edit/<int:url>',dhcpclient.dhcpclient_edit,name='dhcpclient-edit'),
    path('dhcpclient/delete/<int:url>',dhcpclient.dhcpclient_delete,name='dhcpclient-delete'),
    path('dhcpclient/data',dhcpclient.dhcpclient_data,name='dhcpclient-data'),
    #DHCP Server
    path('dhcpserver/',dhcpserver.dhcpserver_list,name='dhcpserver-list'),
    path('dhcpserver/add',dhcpserver.dhcpserver_add,name='dhcpserver-add'),
    path('dhcpserver/edit/<int:url>',dhcpserver.dhcpserver_edit,name='dhcpserver-edit'),
    path('dhcpserver/delete/<int:url>',dhcpserver.dhcpserver_delete,name='dhcpserver-delete'),
    path('dhcpserver/data',dhcpserver.dhcpserver_data,name='dhcpserver-data'),
    # DHCP Network
    path('dhcpnetwork/add',dhcpserver.dhcpnetwork_add,name='dhcpnetwork-add'),
    path('dhcpnetwork/edit/<int:url>',dhcpserver.dhcpnetwork_edit,name='dhcpnetwork-edit'),
    path('dhcpnetwork/delete/<int:url>',dhcpserver.dhcpnetwork_delete,name='dhcpnetwork-delete'),
    path('dhcpnetwork/data',dhcpserver.dhcpnetwork_data,name='dhcpnetwork-data'),
    #IP POOL
    path('pool/',ippool.ippool_list,name='pool-list'),
    path('pool/add',ippool.ippool_add,name='pool-add'),
    path('pool/edit/<int:url>',ippool.ippool_edit,name='pool-edit'),
    path('pool/delete/<int:url>',ippool.ippool_delete,name='pool-delete'),
    path('pool/data',ippool.ippool_data,name='pool-data'),
    #DNS
    path('dns/',dns.dns_list,name='dns-list'),
    path('dns/edit/<int:url>',dns.dns_edit,name='dns-edit'),
    path('dns/data',dns.dns_data,name='dns-data'),
    #Firewall
    path('firewall/',firewall.firewall_list,name='firewall-list'),
    #hotspot server
    path('hotspot/',hotspot.hotspot_list,name='hotspot-list'),
    path('server/add/',hotspot.server_add,name='server-add'),
    path('server/edit/<int:url>',hotspot.server_edit,name='server-edit'),
    path('server/delete/<int:url>',hotspot.server_delete,name='server-delete'),
    path('server/data/',hotspot.server_data,name='server-data'),
    #server profile
    path('serverprofile/add/',hotspot.serverprofile_add,name='serverprofile-add'),   
    path('serverprofile/edit/<int:url>',hotspot.serverprofile_edit,name='serverprofile-edit'),   
    path('serverprofile/delete/<int:url>',hotspot.serverprofile_delete,name='serverprofile-delete'),   
    path('serverprofile/data/',hotspot.serverprofile_data,name='serverprofile-data'),
    #users
    path('users/add/',hotspot.users_add,name='users-add'),   
    path('users/edit/<int:url>',hotspot.users_edit,name='users-edit'),  
    path('users/delete/<int:url>',hotspot.users_delete,name='users-delete'),   
    path('users/data/',hotspot.users_data,name='users-data'),   
    #User profile
    path('userprofile/add',hotspot.userprofile_add,name='userprofile-add'),
    path('userprofile/edit/<int:url>',hotspot.userprofile_edit,name='userprofile-edit'),
    path('userprofile/delete/<int:url>',hotspot.userprofile_delete,name='userprofile-delete'),
    path('userprofile/data',hotspot.userprofile_data,name='userprofile-data'),
    #IP Binding
    path('binding/add/',hotspot.binding_add,name='binding-add'),
    path('binding/edit/<int:url>',hotspot.binding_edit,name='binding-edit'),
    path('binding/delete/<int:url>',hotspot.binding_delete,name='binding-delete'),
    path('binding/data/',hotspot.binding_data,name='binding-data'),
    
    
    # Route
    path('route/',route.route_list,name='route-list'),
    path('route/add',route.route_add,name='route-add'),
    path('route/edit/<int:url>',route.route_edit,name='route-edit'),
    path('route/delete/<int:url>',route.route_delete,name='route-delete'),
    path('route/data',route.route_data,name='route-data'),
    #User
    path('user/',system.user_list,name='user-list'),
    path('user/add',system.user_add,name='user-add'),
    path('user/edit/<int:url>',system.user_edit,name='user-edit'),
    path('user/delete/<int:url>',system.user_delete,name='user-delete'),
    path('user/data',system.user_data,name='user-data'),
    #identity
    path('identity/',system.identity_list,name='identity-list'),
    path('identity/edit/<int:url>',system.identity_edit,name='identity-edit'),
    path('identity/data',system.identity_data,name='identity-data'),
    #reboot
    path('reboot/',system.reboot,name='reboot'),
    path('shutdown/',system.shutdown,name='shutdown'),
]
