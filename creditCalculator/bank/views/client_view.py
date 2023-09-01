from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from bank.forms import ClientForm
from bank.models import Client


@login_required
def get_clients(request):
    clients = Client.objects.all()
    return render(request, "client/clients.html", {"clients": clients})


@login_required
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank:get_clients')
    else:
        form = ClientForm()
    return render(request, "client/post_client.html", {"form": form})


@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client, client_id=client_id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('bank:get_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, "client/post_client.html", {"form": form})


@login_required
def delete_client(request, client_id):
    try:
        client = Client.objects.get(client_id=client_id)
        client.delete()
        return redirect('bank:get_clients')
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
