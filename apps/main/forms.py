from django import forms

class FileRequestEmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)