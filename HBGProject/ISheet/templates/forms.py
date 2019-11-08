from django.forms import ModelForm
from detailapp.models import Is_details
from django import forms


class Is_Form(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Bla bla','style': 'background: cyan;font-size: 17px'}))
    class Meta:
        model = UserDetails
        fields = ['title', 'gender', 'notes']

        def clean(self):
            cc_myself = self.cleaned_data("title")
            subject = self.cleaned_data("gender")
            print(cc_myself)
            if cc_myself and subject:
                # Only do something if both fields are valid so far.
                if "help" not in subject:
                    raise forms.ValidationError(
                        "Did not send for 'help' in the subject despite "
                        "CC'ing yourself."
                    )
            return cleaned_data