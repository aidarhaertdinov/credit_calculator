from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from bank.forms import BankForm
from bank.models import Bank, CreditOffer


@login_required
def get_banks(request):
    banks = Bank.objects.all()
    return render(request, "bank/banks.html", {"banks": banks})


@login_required
def create_bank(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank:get_banks')
    else:
        form = BankForm()
    return render(request, "bank/post_bank.html", {"form": form})


@login_required
def edit_bank(request, bank_id):
    bank = get_object_or_404(Bank, bank_id=bank_id)
    if request.method == "POST":
        form = BankForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            return redirect('bank:get_banks')
    else:
        form = BankForm(instance=bank)
    return render(request, "bank/post_bank.html", {"form": form})


@login_required
def delete_bank(request, bank_id):
    try:
        bank = Bank.objects.get(bank_id=bank_id)
        bank.delete()
        return redirect('bank:get_banks')
    except Bank.DoesNotExist:
        return HttpResponseNotFound("<h2>Bank not found</h2>")


@login_required
def get_all_banks_clients(request, bank_id):
    credit_offers = CreditOffer.objects.filter(bank_id=bank_id).distinct("client")

    if credit_offers:
        return render(request, "bank/all_banks_clients.html", {"credit_offers": credit_offers})
    else:
        return HttpResponseNotFound("<h2>У данного банка нет клиентов</h2>")



