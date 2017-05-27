from django.conf.urls import url

from .views import subscription_apply, subscription_result


urlpatterns = [

    url(r'^$', subscription_apply, name='subscription-apply'),
    url(r'^result/$', subscription_result, name='payment-result-address'),

]
