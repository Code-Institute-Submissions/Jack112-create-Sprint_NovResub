from email.policy import default
from django.db import models
from profiles.models import User


class Product(models.Model):
    """
    Product Model Setup
    """

    PRODUCT_TYPES = (
        ('T', 'Template'),
        ('D', 'Design'),
    )

    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPES)
    category = models.ForeignKey(
        'projects.Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Review Model Setup
    """

    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    content = models.TextField()
    created_by = models.ForeignKey(
        User,
        related_name='reviews',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
