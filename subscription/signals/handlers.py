from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from payments.models import Payment
from ..models import Subscription


@receiver(post_save, sender=Payment)
def payment_post_save(sender, instance, **kwargs):

    if not instance._b_paid_status and instance.paid_status and instance.gateway:

        subscription = Subscription.objects.get(payment=instance)

        subscription.is_paid = instance.paid_status
        subscription.paid_time = timezone.now()
        subscription.save()
