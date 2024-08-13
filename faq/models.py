from django.db import models


class FAQ(models.Model):
    """
    Model representing a frequently asked question.
    """

    question = models.CharField(max_length=255)  # The question field
    answer = models.TextField()  # The answer field

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["id"]  # Orders FAQs by ID

    def __str__(self):
        return self.question  # Returns the question as the string representation
