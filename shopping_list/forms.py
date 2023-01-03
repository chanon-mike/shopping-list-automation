from django import forms


class RecipeSearchForm(forms.Form):
    query = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter a food in the search bar below to find a recipe:',
            }
        ),
    )
