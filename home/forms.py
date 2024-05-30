from django import forms
from django.core.exceptions import ValidationError


def validate_excel_file(value):
    if not value.name.endswith('.xlsx') and not value.name.endswith('.xls'):
        raise ValidationError('Only Excel files (XLSX or XLS) are allowed.')


class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[validate_excel_file])

