from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from bank.forms import CreditForm
from bank.models import Credit


@login_required
def get_credits(request):
    credits = Credit.objects.all()
    return render(request, "credit/credits.html", {"credits": credits})


@login_required
def create_credit(request):
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank:get_credits')
    else:
        form = CreditForm()
    return render(request, "credit/post_credit.html", {"form": form})


@login_required
def edit_credit(request, credit_id):
    credit = get_object_or_404(Credit, credit_id=credit_id)
    if request.method == "POST":
        form = CreditForm(request.POST, instance=credit)
        if form.is_valid():
            form.save()
            return redirect('bank:get_credits')
    else:
        form = CreditForm(instance=credit)
    return render(request, "credit/post_credit.html", {"form": form})


@login_required
def delete_credit(request, credit_id):
    try:
        credit = Credit.objects.get(credit_id=credit_id)
        credit.delete()
        return redirect('bank:get_credits')
    except Credit.DoesNotExist:
        return HttpResponseNotFound("<h2>Credit not found</h2>")