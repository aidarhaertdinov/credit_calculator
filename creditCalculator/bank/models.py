from django.db import models


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    passport_series_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CreditOffer(models.Model):
    credit_offer_id = models.AutoField(primary_key=True)
    bank = models.ForeignKey(Bank, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)

    credit_term = models.IntegerField()  # срок кредита
    credit_amount = models.FloatField()  # сумма кредита
    credit_date = models.DateField(auto_now=True)
    # payment_list = models.ForeignKey(Payment, null=True, on_delete=models.SET_NULL)  #список сущностей ежемесячный платеж

    def __str__(self):
        return f'{self.bank} {self.client} {self.credit_term} {self.credit_amount} {self.credit_date}'


class Credit(models.Model):
    credit_id = models.AutoField(primary_key=True)
    credit_offer = models.OneToOneField(CreditOffer, on_delete=models.CASCADE)
    credit_name = models.CharField(max_length=50)
    credit_limit = models.FloatField()  # лимит по кредиту
    interest_rate = models.FloatField()  # Процентная ставка

    def __str__(self):
        return self.credit_name

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    date = models.DateField()

    payment_amount = models.FloatField()  # сумма платежа
    principal_amount = models.FloatField()  # Сумма гашения тела кредита
    interest_amount = models.FloatField()  # Сумма гашения процентов
    debt_balance = models.FloatField() #остаток
    credit_offer = models.ForeignKey(CreditOffer, null=True, on_delete=models.SET_NULL)
