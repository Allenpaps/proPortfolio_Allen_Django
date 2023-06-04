from django.shortcuts import render

def baseView(request):
    return render(request, 'base.html')