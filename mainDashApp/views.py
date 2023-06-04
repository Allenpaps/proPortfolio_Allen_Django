from django.shortcuts import render

def baseView(request):
    return render(request, 'base.html')

def aboutView(request):
    return render(request, 'aboutMe.html')

def contactView(request):
    return render(request, 'contacts.html')

def historyView(request):
    return render(request, 'history.html')