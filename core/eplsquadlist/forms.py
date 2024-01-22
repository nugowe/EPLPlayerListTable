from eplsquadlist.models import EPL
from django import forms

class EPLFormFilter(forms.Form):
    EplTeams_query = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        choices = EPL.EPLTeams.choices
    )


