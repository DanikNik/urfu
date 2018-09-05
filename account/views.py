from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Person
from assets.checks.user_check_mixins import ProfileCheckMixin


class PersonListView(ProfileCheckMixin, ListView):
    model = Person
    template_name = 'account/person_list.html'
    context_object_name = 'person_list'


# Create your views here.

class PersonDetailView(ProfileCheckMixin, DetailView):
    model = Person
    template_name = 'account/person_detail.html'
    context_object_name = 'person'


class PersonCreateView(CreateView):
    model = Person
    template_name = 'registration/person_create.html'
    fields = [
        'name',
        'surname',
        # 'last_name',
        'place_of_study',
        'group_number',
        'place_of_work',
        'job_position',
        'birth_date',
        'vk_link',
        'fb_link',
        'google_link',
        'tg_link',
        'phone_number',
        'type'
    ]

    def form_valid(self, form):
        person = form.save(commit=False)
        person.user = self.request.user
        return super(PersonCreateView, self).form_valid(form)


class PersonUpdateView(ProfileCheckMixin, UpdateView):
    model = Person
    fields = ['type']
    template_name = 'account/person_update.html'
    fields = [
        'name',
        'surname',
        # 'last_name',
        'place_of_study',
        'group_number',
        'place_of_work',
        'job_position',
        'birth_date',
        'vk_link',
        'fb_link',
        'google_link',
        'tg_link',
        'phone_number',
        'type'
    ]

    def get_object(self):
        return self.request.user.person
