from django.views.generic import TemplateView
from django.shortcuts import render

# class EmployeeProfileView(TemplateView):
#     template_name = 'profile.html'

# class SettingsView(TemplateView):
#     template_name = 'settings.html'

def employee_profile_view(request):

    context = {}

    return render(request, "profile.html", context)

def settings_view(request):

    context = {}

    return render(request, "settings.html", context)