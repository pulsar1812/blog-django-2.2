"""
Dummy docstring
"""
from django import forms


class ContactForm(forms.Form):
    """Dummy docstring"""

    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):
        """Dummy docstring"""
        email = self.cleaned_data.get("email")
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError(
                "This is not a valid email. Please do not use .edu"
            )
        return email
