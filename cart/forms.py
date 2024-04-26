from django import forms


class AddToCartProductForm(forms.Form):
    QUANTITY_CHOICES = [('1', '1')]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
