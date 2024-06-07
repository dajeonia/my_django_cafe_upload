from django.shortcuts import render
from django.http import HttpResponse

import os
import time

# Create your views here.

def index(request):
    time.sleep(3)
    os.system('python manage.py crontab remove')
    time.sleep(3)
    os.system('python manage.py crontab add')
    time.sleep(3)
    return HttpResponse({"success":True})
