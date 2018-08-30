from django.views.generic import TemplateView
from authenticate import requirements
from django.contrib.auth.mixins import UserPassesTestMixin

class DashboardView(TemplateView,UserPassesTestMixin):
    template_name = "dashboard/dashboard.html"
    login_url = '/account/new_person/'
    def get_test_func(self):
        return self.check

    def check(self):
        return hasattr(self.request.user, 'person')