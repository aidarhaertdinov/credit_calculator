from django import forms


class BankForm(forms.Form):
    name = forms.CharField(help_text="Введите название банка", label="Название")


class ClientForm(forms.Form):
    last_name = forms.CharField(help_text="Введите фамилию", label="Фамилия")
    first_name = forms.CharField(help_text="Введите имя", label="Имя")
    patronymic = forms.CharField(help_text="Введите отчество", label="Отчество")
    phone_number = forms.CharField(help_text="Введите номер телефона", label="Номер телефона")
    email = forms.EmailField(help_text="Введите почту", label="Почта")
    passport_series_number = forms.CharField(help_text="Введите номер и серию паспорта без пробела",
                                             label="Номер и серия паспорта")


class CreditForm(forms.Form):
    credit_limit = forms.FloatField(help_text="Введите лимит по кредиту", label="Лимит по кредиту")
    interest_rate = forms.FloatField(help_text="Введите процентную ставку", label="Процентная ставка")


class CreditOfferForm(forms.Form):
    credit_term = forms.IntegerField(help_text="Введите срок по кредитному предложению",
                                     label="Срок кредитного предложения")
    credit_amount = forms.FloatField(help_text="Введите сумму по кредитному предложению",
                                     label="Сумма кредитного предложения")
    credit_date = forms.DateField(help_text="Введите дату по кредитному предложению",
                                  label="Лимит кредитного предложения")