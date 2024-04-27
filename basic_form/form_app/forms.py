from django import forms
from django.core import validators



class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again: ')
    text = forms.CharField(widget=forms.Textarea)
    # botCatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


    # def clean_botCatcher(self):
    #     botCatcher = self.cleaned_data['botCatcher']
    #     if len(botCatcher):
    #         raise forms.ValidationError("GOTCHA BOT!")

    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        vmail = all_cleaned_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match")


    def __str__(self):
        return self.name