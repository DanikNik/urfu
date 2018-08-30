from django.views.generic import TemplateView
# from authenticate import requirements
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin

class DashboardView(UserPassesTestMixin, TemplateView):
    template_name = "dashboard/dashboard.html"
    redirect_field_name = 'next'
    raise_exception = False

    def get_login_url(self):
        return reverse('person_create')

    def test_func(self):
        return hasattr(self.request.user, 'person')