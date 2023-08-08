from django import forms

from bank.models import Bank, Client, Credit, CreditOffer


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = '__all__'


class CreditOfferForm(forms.ModelForm):
    class Meta:
        model = CreditOffer
        fields = '__all__'