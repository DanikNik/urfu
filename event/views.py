from django.template import loader
from django.http import HttpResponse
from .models import Event, Membership
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic import FormView
from django.forms import Form
#TODO: перевести все views на class-based

class EventRegisterForm(Form):
    pass

class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = "event_list"

class EventDetailView(FormView, DetailView):
    success_url = "events/"
    context_object_name = "event"
    model = Event
    template_name = "event/event_detail.html"
    form_class = EventRegisterForm

    def form_valid(self, form):
        Membership.add_member(self.request.user.person, Event.objects.get(id=int(self.pk_url_kwarg)))
        return super(EventDetailView, self).form_valid(form)

#
#
# @login_required
# def index(request):
#     event_list = Event.objects.all()
#     template = loader.get_template('event/index.html')
#     context = {
#         'event_list': event_list
#     }
#     return HttpResponse(template.render(context, request))
#
#
# @login_required
# def event(request, event_id):
#     event = Event.objects.get(id=event_id)
#     user_list = event.members.all()
#     template = loader.get_template('event/event.html')
#     context = {
#         'event_title': Event.objects.get(id=event_id),
#         'user_list': user_list
#     }
#     return HttpResponse(template.render(context, request))
