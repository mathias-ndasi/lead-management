from django import forms

from leads.models import Lead


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent",
        )
