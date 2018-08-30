from django.views.generic import TemplateView
# from authenticate import requirements
from assets.checks.user_check_mixins import ProfileCheckMixin

class DashboardView(ProfileCheckMixin, TemplateView):
    template_name = "dashboard/dashboard.html"
