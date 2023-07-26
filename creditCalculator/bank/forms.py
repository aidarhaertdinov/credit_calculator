from django import forms


class BankForm(forms.Form):
    name = forms.CharField(help_text="Введите название банка", label="Название")
