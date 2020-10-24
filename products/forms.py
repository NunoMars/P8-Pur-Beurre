from django import forms

class GetProductChoiceForm(forms.Form):
    chosed_product = forms.CharField(label='produit recherché', max_length=100)