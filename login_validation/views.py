from django.shortcuts import render

def login_validation_view(request):

    context = {}

    return render(request, "login.html", context)
