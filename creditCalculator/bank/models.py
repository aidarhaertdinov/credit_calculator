from django.db import models


class Client(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    passport_series_number = models.CharField(max_length=10)


class Bank(models.Model):
    name = models.CharField(max_length=100)


class CreditOffer(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    credit_limit = models.DecimalField(max_digits=11, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)  # Процентная ставка


class Credit(models.Model):
    credit_offer = models.OneToOneField(CreditOffer, on_delete=models.CASCADE, primary_key=True)

    amount_credit = models.DecimalField(max_digits=11, decimal_places=2)  # сумма кредита
    payment_schedule = models.DateField()  # график платежей
    payment_date = models.DateField()  # дата платежа
    payment_amount = models.DecimalField(max_digits=11, decimal_places=2)  # сумма платежа
    repayment_amount_body = models.DecimalField(max_digits=11, decimal_places=2)  # Сумма гашения тела кредита
    repayment_amount_interest = models.DecimalField(max_digits=11, decimal_places=2)  # Сумма гашения процентов
