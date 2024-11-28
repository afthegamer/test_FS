from django import forms

class CSVUploadForm(forms.Form):
    file = forms.FileField(label='Sélectionnez un fichier CSV')
