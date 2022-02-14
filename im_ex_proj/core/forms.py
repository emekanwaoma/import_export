from django import forms

class NewForm(forms.Form):
    options = (
        ('csv', 'csv'),
        ('xls', 'xls'),
        ('json', 'json'),
        ('pdf', 'pdf'),
    )
    
    category = forms.CharField(widget=forms.Select(choices=options), label='Export To:')