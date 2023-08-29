from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from bank.forms import ClientForm
from bank.models import Client


class ClientView:

    def get_clients(request):
        clients = Client.objects.all()
        return render(request, "client/clients.html", {"clients": clients})

    def create_client(request):
        if request.method == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('get_clients')
        else:
            form = ClientForm()
        return render(request, "client/post_client.html", {"form": form})

    def edit_client(request, client_id):
        client = get_object_or_404(Client, client_id=client_id)
        if request.method == "POST":
            form = ClientForm(request.POST, instance=client)
            if form.is_valid():
                form.save()
                return redirect('get_clients')
        else:
            form = ClientForm(instance=client)
        return render(request, "client/post_client.html", {"form": form})

    def delete_client(request, client_id):
        try:
            client = Client.objects.get(client_id=client_id)
            client.delete()
            return redirect('get_clients')
        except Client.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
