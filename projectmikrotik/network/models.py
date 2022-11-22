from unicodedata import name
from django.db import models
from django.forms import CharField
# from django import forms
# Create your models here.

class bridge(models.Model):
    name=models.CharField(max_length=45)
    typebridge=models.CharField(max_length=45)
    actualmtu=models.CharField(max_length=45)
    l2mtu=models.CharField(max_length=45)
    vlan=models.BooleanField(default=False)
    bridge_id=models.CharField(max_length=45)
    

class port(models.Model):
    port_id=models.CharField(max_length=45)
    interface=models.CharField(max_length=45)
    bridge=models.CharField(max_length=45)
    pvid=models.CharField(max_length=45)
    frametypes=models.CharField(max_length=45)
    
class vlans(models.Model):
    vlansid=models.CharField(max_length=45)
    vlans_bridge=models.CharField(max_length=45)
    vlans_ids=models.CharField(max_length=45)
    tagged=models.CharField(max_length=45)
    untagged=models.CharField(max_length=45)
    
class interface(models.Model):
    interface_id=models.CharField(max_length=45)
    interface_name=models.CharField(max_length=45)
    typeinterface=models.CharField(max_length=45)
    actualmtu=models.CharField(max_length=45)
    l2mtu=models.CharField(max_length=45)
    
class ethernet(models.Model):
    ether_id=models.CharField(max_length=45)
    ether_name=models.CharField(max_length=45)
    mac_address=models.CharField(max_length=45)
    ether_default=models.CharField(max_length=45)
    
class vlan(models.Model):
    vlanid=models.CharField(max_length=45)
    vlan_name=models.CharField(max_length=45)
    vlan_id=models.CharField(max_length=45)
    vlan_interface=models.CharField(max_length=45)
    vlan_type=models.CharField(max_length=45)


class ipaddress(models.Model):
    address_id=models.CharField(max_length=45)
    address=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    interface=models.CharField(max_length=45)
    dynamic=models.CharField(max_length=45)
    
class dhcpclient(models.Model):
    dhcp_id=models.CharField(max_length=45)
    interface=models.CharField(max_length=45)
    status=models.CharField(max_length=45)
    address=models.CharField(max_length=45)
    dns=models.CharField(max_length=45)
    ntp=models.CharField(max_length=45)
    route=models.CharField(max_length=45)

class dhcpclienttype(models.Model):
    name=models.CharField(max_length=45)

class dhcpserver(models.Model):
    dhcp_id=models.CharField(max_length=45)
    name=models.CharField(max_length=45)
    interface=models.CharField(max_length=45)
    address_pool=models.CharField(max_length=45)
    
class dhcpnetwork(models.Model):
    dhcp_id=models.CharField(max_length=45)
    address=models.CharField(max_length=45)
    gateway=models.CharField(max_length=45)
    dns=models.CharField(max_length=45)

class dhcplease(models.Model):
    dhcp_id=models.CharField(max_length=45)
    address=models.CharField(max_length=45)
    mac_address=models.CharField(max_length=45)
    client=models.CharField(max_length=45)
    status=models.CharField(max_length=45)
    dhcpserver=models.CharField(max_length=45)

class pool(models.Model):
    pool_id=models.CharField(max_length=45)
    pool_name=models.CharField(max_length=45)
    pool_address=models.CharField(max_length=45)
    
class route(models.Model):
    route_id=models.CharField(max_length=45)
    dst_address=models.CharField(max_length=45)
    gateway=models.CharField(max_length=45)
    status=models.CharField(max_length=45)
    distance=models.CharField(max_length=45)
    dynamic=models.CharField(max_length=45)
    
    
class user(models.Model):
    user_id=models.CharField(max_length=45)
    name=models.CharField(max_length=45)
    group=models.CharField(max_length=45)

class identity(models.Model):
    name_id=models.CharField(max_length=45)
    name=models.CharField(max_length=45)
    
    
class dns(models.Model):
    server=models.CharField(max_length=45)
    dynamic=models.CharField(max_length=45)
    allow=models.CharField(max_length=45)
    
    
class connection(models.Model):
    con_id=models.CharField(max_length=45)
    protocal=models.CharField(max_length=45)
    src=models.CharField(max_length=45)
    dst=models.CharField(max_length=45)
    reply_src=models.CharField(max_length=60)
    reply_dst=models.CharField(max_length=60)
    repl_byte=models.CharField(max_length=60)
    repl_packet=models.CharField(max_length=60)
    orig_packet=models.CharField(max_length=60)
    orig_byte=models.CharField(max_length=60)  
    
    
    
    
class server(models.Model):
    server_id = models.CharField(max_length=45)
    server_name = models.CharField(max_length=45)
    server_interface = models.CharField(max_length=45)
    server_pool = models.CharField(max_length=45)
    server_profile = models.CharField(max_length=45)

class serverprofile(models.Model):
    ser_id = models.CharField(max_length=45)
    ser_name = models.CharField(max_length=45)
    ser_address = models.CharField(max_length=45)
    ser_dns = models.CharField(max_length=45)

class users(models.Model):
    user_id = models.CharField(max_length=45)
    user_ser = models.CharField(max_length=45)
    user_name = models.CharField(max_length=45)
    user_pass = models.CharField(max_length=45)
    user_pro = models.CharField(max_length=45)
    
class userprofile(models.Model):
    userpro_id = models.CharField(max_length=45)
    userpro_name = models.CharField(max_length=45)
    userpro_address = models.CharField(max_length=45)
    userpro_share = models.CharField(max_length=45)
    userpro_rate = models.CharField(max_length=45)
    
class host(models.Model):
    host_mac_address = models.CharField(max_length=45)
    host_address = models.CharField(max_length=45)
    host_server = models.CharField(max_length=45)

class binding(models.Model):
    binding_id = models.CharField(max_length=45)
    binding_mac = models.CharField(max_length=45)
    binding_ser = models.CharField(max_length=45)
    binding_type = models.CharField(max_length=45)
    binding_address=models.CharField(max_length=45)
   
class device(models.Model):
    name = models.CharField(max_length=45)
    host = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
