from django.shortcuts import render

# Create your views here.
def jinja_a1(request):
    d={'name':'sasank','age':23}
    return render(request,'jinja_a1.html',d)
    