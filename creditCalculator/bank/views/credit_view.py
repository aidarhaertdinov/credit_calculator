from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from bank.forms import CreditForm
from bank.models import Credit


class CreditView:

    def get_credits(request):
        credits = Credit.objects.all()
        return render(request, "credit/credits.html", {"credits": credits})

    def create_credit(request):
        if request.method == 'POST':
            form = CreditForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('get_credits')
        else:
            form = CreditForm()
        return render(request, "credit/post_credit.html", {"form": form})

    def edit_credit(request, credit_id):
        credit = get_object_or_404(Credit, credit_id=credit_id)
        if request.method == "POST":
            form = CreditForm(request.POST, instance=credit)
            if form.is_valid():
                form.save()
                return redirect('get_credits')
        else:
            form = CreditForm(instance=credit)
        return render(request, "credit/post_credit.html", {"form": form})

    def delete_credit(request, credit_id):
        try:
            credit = Credit.objects.get(credit_id=credit_id)
            credit.delete()
            return redirect('get_credits')
        except Credit.DoesNotExist:
            return HttpResponseNotFound("<h2>Credit not found</h2>")