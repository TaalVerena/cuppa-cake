from django.shortcuts import render


def subscribe_view(request):
    return render(request, 'newsletter/subscription.html')
