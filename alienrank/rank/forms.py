
# Django
from django import forms

# Vendor
from bootstrap3_datetime.widgets import DateTimePicker

class PostFilterForm(forms.Form):

    hide_cdn = forms.BooleanField(required=False)
    hide_reddit = forms.BooleanField(required=False)

    begin = forms.DateTimeField(required=False,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD"})
    )

    end = forms.DateTimeField(required=False)

