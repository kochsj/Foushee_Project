from django.views.generic import TemplateView

class EmployeeProfileView(TemplateView):
    template_name = 'profile.html'

class SettingsView(TemplateView):
    template_name = 'settings.html'