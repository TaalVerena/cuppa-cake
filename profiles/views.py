from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile and handle profile updates.
    """
    profile = get_object_or_404(UserProfile, user=request.user)  # Get user profile

    if request.method == "POST":
        # Handle profile form submission
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        form = UserProfileForm(
            instance=profile
        )  # Populate form with current profile data

    orders = (
        profile.orders.all()
    )  # Retrieve all orders associated with the user profile

    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "on_profile_page": True,  # Indicate the user is on the profile page
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Display past order details for a given order number.
    """
    order = get_object_or_404(
        Order, order_number=order_number
    )  # Retrieve order by order number

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,  # Indicate that the view is accessed from the profile page
    }

    return render(request, template, context)
