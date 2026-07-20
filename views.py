from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse("<u>welcome Coder's to django world!</u>")

def bio(request):
    return HttpResponse("""
    <h1>Name: <h2>Shubham Sirse</h2></h1>
    <h1>Age: <h2>19</h2></h1>
    <h1>Position: <h2>Coder</h2></h1>
    """)

def Home_page(request):
    return render(request, "Home_page_.html")

def Login(request):
    return render(request, "Login.html")       