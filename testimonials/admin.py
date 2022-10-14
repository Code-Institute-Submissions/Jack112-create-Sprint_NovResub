from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    """
    Register custom Testimonial Admin with custom meta fields.
    """

    # Admin users can only read and delete testimonials.
    readonly_fields = ('name', 'description')


admin.site.register(Testimonial, TestimonialAdmin)
