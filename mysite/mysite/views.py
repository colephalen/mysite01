from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import Http404
# from mysite.models import View

def all_view(request):
    # context = {'alls': View.objects.all()}
    return render(request, 'base.html')
