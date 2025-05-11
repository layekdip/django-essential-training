from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime

from flask_login import login_required


# Create your views here.
def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'home/welcome.html', {'today': datetime.today()})


@login_required
def authorized(request):
    return render(request, 'home/authorized.html', {})
