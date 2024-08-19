from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    """
    A view for handling the contact form.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact_thank_you")
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})


def contact_thank_you_view(request):
    """
    A view for displaying a thank you message after contact form submission.
    """
    return render(request, "contact/thank_you.html")
