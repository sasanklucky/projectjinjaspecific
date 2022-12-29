from django.shortcuts import render

# Create your views here.
def jinja_a2(request):
    d={'name':'sasank','age':22}
    return render(request,'jinja_a2.html',d)