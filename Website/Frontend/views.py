from django.shortcuts import render

def app_view(request):
    return render(request, 'Frontend/app.html')