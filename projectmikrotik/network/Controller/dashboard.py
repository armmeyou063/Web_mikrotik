from django.shortcuts import render, redirect
from network.models import  identity as identity_model 


def Dashboard(request):
     identity=identity_model.objects.all()
     return render(request, 'dashboard/dashboard.html',{'identity':identity})
