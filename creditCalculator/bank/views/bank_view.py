from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from bank.forms import BankForm
from bank.models import Bank


class BankView:

    def get_banks(request):
        banks = Bank.objects.all()
        return render(request, "bank/banks.html", {"banks": banks})

    def create_bank(request):
        if request.method == 'POST':
            form = BankForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('get_banks')
        else:
            form = BankForm()
        return render(request, "bank/post_bank.html", {"form": form})

    def edit_bank(request, bank_id):
        bank = get_object_or_404(Bank, bank_id=bank_id)
        if request.method == "POST":
            form = BankForm(request.POST, instance=bank)
            if form.is_valid():
                form.save()
                return redirect('get_banks')
        else:
            form = BankForm(instance=bank)
        return render(request, "bank/post_bank.html", {"form": form})

    def delete_bank(request, bank_id):
        try:
            bank = Bank.objects.get(bank_id=bank_id)
            bank.delete()
            return redirect('get_banks')
        except Bank.DoesNotExist:
            return HttpResponseNotFound("<h2>Bank not found</h2>")