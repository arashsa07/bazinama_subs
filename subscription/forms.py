from django.forms import ModelForm

from .models import Subscription


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ['first_name', 'last_name', 'age', 'education', 'postal_code', 'phone_number', 'mobile_number',
                  'email', 'address', 'subscription_type']
