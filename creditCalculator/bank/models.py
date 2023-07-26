
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
    bank = models.ForeignKey(Bank, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)

    credit_term = models.IntegerField() # срок кредита
    credit_amount = models.FloatField() # сумма кредита
    credit_date = models.DateField(auto_now=True)
    # payment_list = models.ForeignKey(Payment, null=True, on_delete=models.SET_NULL)  #список сущностей ежемесячный платеж


class Credit(models.Model):
    credit_offer = models.OneToOneField(CreditOffer, on_delete=models.CASCADE, primary_key=True)

    credit_limit = models.FloatField() # лимит по кредиту
    interest_rate = models.FloatField()  # Процентная ставка


class Payment(models.Model):
    date = models.DateField()
    # payment_date = models.IntegerField()
    # дата платежа
    payment_amount = models.FloatField()  # сумма платежа
    principal_amount = models.FloatField()  # Сумма гашения тела кредита
    interest_amount = models.FloatField()  # Сумма гашения процентов
    credit_offer = models.ForeignKey(CreditOffer, null=True, on_delete=models.SET_NULL)
