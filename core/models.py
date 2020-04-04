from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import jsonfield


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class ProductOrder(models.Model):
    
    approved_for_delivery= models.BooleanField(default=False)
    order = jsonfield.JSONField()
    addon = jsonfield.JSONField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_package_delivered = models.BooleanField(default=False)
    reference_code = models.CharField(max_length=20, blank=True, null=True)
    package_being_delivered = models.BooleanField(default=False)
