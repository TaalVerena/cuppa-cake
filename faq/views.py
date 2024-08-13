from django.shortcuts import render
from .models import FAQ


def faq_list(request):
    """
    View to display a list of frequently asked questions.
    """
    faqs = FAQ.objects.all()  # Retrieve all FAQ entries
    return render(
        request, "faq/faq_list.html", {"faqs": faqs}
    )  # Render the FAQs to the template
