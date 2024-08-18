from django.shortcuts import render


def subscribe_view(request):
    subscribed = False

    if request.method == "POST":
        subscribed = True

    return render(request, "newsletter/subscription.html", {"subscribed": subscribed})
