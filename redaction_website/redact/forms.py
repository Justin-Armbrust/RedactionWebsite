from django import forms

class InputForm(forms.Form):
    input_text = forms.CharField(label='Input Text', max_length=2000,widget=forms.Textarea(attrs={'class':'form-control','rows':'5'}))