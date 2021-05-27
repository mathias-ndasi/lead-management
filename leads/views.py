from django.core.mail import send_mail
from django.urls import reverse
from django.views import generic

from leads.forms import LeadModelForm, CustomUserCreationForm
from leads.models import Lead


class SignupPageView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse(viewname="login")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(generic.ListView):
    template_name = "leads/list.html"
    context_object_name = "leads"
    queryset = Lead.objects.all()


class LeadDetailView(generic.DetailView):
    template_name = "leads/detail.html"
    context_object_name = "lead"
    queryset = Lead.objects.all()


class LeadCreateView(generic.CreateView):
    template_name = "leads/create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse(viewname="leads:lead_list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see your new lead.",
            from_email="example@example.com",
            recipient_list=["test@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse(viewname="leads:lead_detail", kwargs={"pk": self.object.id})


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse(viewname="leads:lead_list")
