from django.views.generic import TemplateView


class LoginValidationView(TemplateView):
    template_name = 'login.html'
