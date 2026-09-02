from django.db import models


class Contact(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("read", "Read"),
        ("replied", "Replied"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"



class GalleryImage(models.Model):

    CATEGORY_CHOICES = [
        ('sainik', 'Sainik School Jhansi'),
        ('navodaya', 'Navodaya Vidyalaya'),
        ('glimpses', 'Other Glimpses'),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name="Image Title"
    )

    image = models.ImageField(
        upload_to='gallery/',
        verbose_name="Image"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='glimpses',
        verbose_name="Category"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Show on Gallery"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Display Order"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title




''' visitor '''
'''
class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_date = models.DateField(auto_now_add=True)
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.visit_date}"

    class Meta:
        ordering = ["-visit_time"]
'''



class Visitor(models.Model):
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.visited_at.strftime("%d-%m-%Y %H:%M:%S")
