from django import forms

class GetProductForm(forms.Form):
    cherched_product = forms.CharField(label='produit recherché', max_length=100)