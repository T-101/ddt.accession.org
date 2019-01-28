from django.db.models import Sum
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from ddt.forms import RegistrationForm, WallForm
from ddt.models import Registration, Wall, SiteSettings


class IndexView(TemplateView):
    template_name = 'ddt/index.html'


class FuneralView(FormView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = SiteSettings.objects.first()

    template_name = 'ddt/funeral.html'
    form_class = RegistrationForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['registrations'] = Registration.objects.all()
        ctx['settings'] = self.settings
        ctx['count'] = Registration.objects.aggregate(Sum('amount')).get('amount__sum', -1)
        return ctx

    def get_success_url(self):
        return reverse('funeral')

    def form_valid(self, form):
        if self.settings.registration_open:
            form.save()
        return super().form_valid(form)


class WallView(FormView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = SiteSettings.objects.first()

    template_name = 'ddt/wall.html'
    form_class = WallForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['settings'] = self.settings
        ctx['writings'] = Wall.objects.all()
        return ctx

    def get_success_url(self):
        return reverse('wall')

    def form_valid(self, form):
        if self.settings.registration_open:
            form.save()
        return super().form_valid(form)
