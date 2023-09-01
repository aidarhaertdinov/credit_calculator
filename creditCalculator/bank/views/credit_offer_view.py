from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from bank.forms import CreditOfferForm
from bank.models import CreditOffer


@login_required
def get_credit_offers(request):
    credit_offers = CreditOffer.objects.all()
    return render(request, "credit_offer/credit_offers.html",
                  {"credit_offers": credit_offers})


@login_required
def create_credit_offer(request):
    if request.method == 'POST':
        form = CreditOfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank:get_credit_offer')
    else:
        form = CreditOfferForm()
    return render(request, "credit_offer/post_credit_offer.html", {"form": form})


@login_required
def edit_credit_offer(request, credit_offer_id):
    credit_offer = get_object_or_404(CreditOffer, credit_offer_id=credit_offer_id)
    if request.method == "POST":
        form = CreditOfferForm(request.POST, instance=credit_offer)
        if form.is_valid():
            form.save()
            return redirect('bank:get_credit_offer')
    else:
        form = CreditOfferForm(instance=credit_offer)
    return render(request, "credit_offer/post_credit_offer.html", {"form": form})


@login_required
def delete_credit_offer(request, credit_offer_id):
    try:
        credit_offer = CreditOffer.objects.get(credit_offer_id=credit_offer_id)
        credit_offer.delete()
        return redirect('bank:get_credit_offer')
    except CreditOffer.DoesNotExist:
        return HttpResponseNotFound("<h2>CreditOffer not found</h2>")
