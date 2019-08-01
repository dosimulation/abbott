from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect

# main page
def index(request):
    return render(request, 'index.html')
