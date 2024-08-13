from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for collecting contact information and message.
    """

    class Meta:
        model = Contact
        fields = ["name", "email", "message"]  # Fields to include in the form
