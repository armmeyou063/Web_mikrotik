import json
from django.shortcuts import render, redirect
import paramiko
from librouteros import connect
from network.models import  connection as firewall_model,identity as identity_model

def firewall_list(request):
    if 'host' in request.session :
        host = request.session['host']
        username = request.session['username']
        password = request.session['password']
        api = connect(username=username, password=password,host=host)
        connection_info = api(cmd="/ip/firewall/connection/print")
        firewall_del=firewall_model.objects.all()
        firewall_del.delete()
        for con in connection_info:
            #print(json.dumps(con, indent=4))
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
        firewall=firewall_model.objects.all()
        identity=identity_model.objects.all()
        return render(request,'firewall/firewall_list.html',{'firewall':firewall,'identity':identity})
    else:
        return redirect('login-form')
    