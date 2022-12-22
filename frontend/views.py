from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response



# @login_required(login_url='login')
def list(request):
    return render(request, 'frontend/index.html')
