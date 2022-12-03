from django.shortcuts import render
import http

# Create your views here.
def landing(req):
    return render(req, "demo/landing_page.html")