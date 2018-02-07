from django import forms


class ZipForm(forms.Form):
    zipfile = forms.FileField(max_length=256, allow_empty_file=False, label='Zip File')
    email = forms.EmailField()
    pattern = forms.CharField(max_length=128, required=False)
