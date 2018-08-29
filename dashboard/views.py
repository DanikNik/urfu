from django.views.generic import TemplateView
from account.models import Person


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"
