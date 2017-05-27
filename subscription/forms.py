from django.forms import ModelForm, DateField


from .models import Subscription


class SubscriptionForm(ModelForm):
    # birthday = DateField(required=False, input_formats=['%Y-%m-%d',  # '2017-10-26'
    #                                                     '%Y-%m-%d',  # '2017/10/26'
    #                                                     '%y-%m-%d',  # '17-10-26'
    #                                                     '%y/%m/%d']  # '17/10/26'
    # )

    class Meta:
        model = Subscription
        fields = ['first_name', 'last_name', 'birthday', 'education', 'postal_code', 'phone_number', 'mobile_number',
                  'email', 'address', 'subscription_type']
