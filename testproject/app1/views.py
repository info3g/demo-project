from django.shortcuts import render
from django.shortcuts import HttpResponse,render,redirect
from app1.models import data2,data1,more

# Create your views here.
def home(request):
    if request.method == "POST":

        execcuter=request.POST["exe"]
        print(execcuter)
        if execcuter=="1":
            d1 = data1.objects.all()
            return render(request, "index.html", {"d1": d1})
        if execcuter=="0":
            d2 = data2.objects.all()
            return render(request, "index.html", {"d2": d2})
        if execcuter == 'moron':
            m = more.objects.all()
            return render(request, "index.html", {"m1": m})

    return render(request,"index.html",)