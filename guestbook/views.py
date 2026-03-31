from django.shortcuts import render, redirect
from .forms import GuestEntryForm
from .models import GuestEntry


# Create your views here.

def home(request):
    if request.method == "POST":
        form = GuestEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("entry_list")
    else:
        form = GuestEntryForm()

    return render(request, "guestbook/home.html", {"form": form})

def entry_list(request):
    entries = GuestEntry.objects.order_by("-created_at")
    return render(request, "guestbook/entry_list.html", {"entries": entries})