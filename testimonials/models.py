from django.db import models


class Testimonial(models.Model):
    """
    Testimonials Model Setup
    """

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
