from django import forms


class TemplateForm(forms.Form):
    name = forms.CharField()
    select = forms.ChoiceField(choices=(
        ("General Health", "General Health"),
        ("Cardiology", "Cardiology"),
        ("Dental", "Dental"),
        ("Medical Research", "Medical Research"),
    ))
    message = forms.CharField(widget=forms.Textarea, max_length=100)
    email = forms.EmailField()
    data = forms.DateField()
    phone = forms.CharField(max_length=12)