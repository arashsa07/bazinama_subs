from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators


class Subscription(models.Model):
    SUB_30000 = 1
    SUB_42000 = 2
    SUB_60000 = 3
    SUB_80000 = 4
    SUBSCRIPTION_TYPES = (
        (SUB_30000, 30000),  # "شش شماره + پست سفارشی = 30000 تومان"),
        (SUB_42000, 42000),  # "شش شماره + DVD + پست سفارشی = 42000 تومان"),
        (SUB_60000, 60000),  # "دوازده شماره + پست سفارشی = 60000 تومان"),
        (SUB_80000, 80000),  # "دوازده شماره + DVD + پست سفارشی = 80000 تومان")
    )

    created_time = models.DateTimeField(_('Time'), auto_now_add=True)
    first_name = models.CharField(_('First Name'), max_length=255, blank=True)
    last_name = models.CharField(_('First Name'), max_length=255, blank=True)
    birthday = models.CharField(_('Birthday'), max_length=100, blank=True, null=True)
    education = models.CharField(_('First Name'), max_length=255, blank=True)
    postal_code = models.CharField(_('Postal Code'), max_length=20, blank=True)
    phone_number = models.CharField(_('Phone Number'), max_length=20, blank=True)
    mobile_number = models.CharField(_('Mobile Number'), max_length=20, validators=[
        validators.RegexValidator(r'^989[0-3,9]\d{8}$',
                                  _('Phone number must be a VALID 12 digits like 989xxxxxxxxx'), 'invalid')])
    email = models.EmailField(_('Email'))
    address = models.TextField(_('Address'), blank=True)
    subscription_type = models.PositiveSmallIntegerField(_('Type'), choices=SUBSCRIPTION_TYPES)
    payment = models.OneToOneField('payments.Payment', verbose_name=_('payment'), null=True, editable=False)
    is_paid = models.BooleanField(_('Is Paid'), default=False)
    paid_time = models.DateTimeField(_('Paid Time'), blank=True, null=True)

    class Meta:
        db_table = 'subscriptions'
