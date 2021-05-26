from django.shortcuts import render, redirect
from django.urls import reverse

from leads.forms import LeadModelForm
from leads.models import Lead


def lead_list(request):
    leads = Lead.objects.all()

    context = {
        "leads": leads
    }
    return render(request=request, template_name="leads/list.html", context=context)


def lead_create(request):
    form = LeadModelForm()

    if request.method == "POST":
        form = LeadModelForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse(viewname="leads:lead_list"))

    context = {
        "form": form
    }
    return render(request=request, template_name="leads/create.html", context=context)


def lead_detail(request, pk: int):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request=request, template_name="leads/detail.html", context=context)


def lead_update(request, pk: int):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)

    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)

        if form.is_valid():
            lead.first_name = form.cleaned_data.get("first_name")
            lead.last_name = form.cleaned_data.get("last_name")
            lead.age = form.cleaned_data.get("age")
            lead.save()

            return redirect(reverse(viewname="leads:lead_detail", kwargs={"pk": lead.id}))

    context = {
        "form": form
    }
    return render(request=request, template_name="leads/update.html", context=context)


def lead_delete(request, pk: int):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect(reverse("leads:lead_list"))
