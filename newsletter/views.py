from django.shortcuts import render


def subscribe_view(request):
    """
    A view to render the newsletter subscription page
    """
    subscribed = False

    if request.method == "POST":
        subscribed = True

    return render(request, "newsletter/subscription.html", {"subscribed": subscribed})
