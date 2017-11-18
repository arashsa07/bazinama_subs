from django.shortcuts import render, redirect

from .forms import SubscriptionForm
from .models import Subscription
from payments.models import Payment, Gateway


# Subscription Apply ==================================================================================================
def subscription_apply(request):

    sub_types = [('1', "شش شماره + پست سفارشی = 45000 تومان"),
                 ('2', "شش شماره + DVD + پست سفارشی = 54000 تومان"),
                 ('3', "دوازده شماره + پست سفارشی = 90000 تومان"),
                 ('4', "دوازده شماره + DVD + پست سفارشی = 108000 تومان")]

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            amount = Subscription.SUBSCRIPTION_TYPES[form.cleaned_data['subscription_type']-1][1]
            new_sub = form.save(commit=False)
            gateway = Gateway.objects.first()
            gateway_id = {'id': gateway.id}
            payment = Payment.objects.create(amount=amount, gateway=gateway, response_type=2)
            new_sub.payment = payment
            new_sub.save()

            return redirect(payment.get_url(request=request, gateway=gateway_id))

        else:
            return render(request, 'subscription/apply.html', {'form': form, 'sub_types': sub_types})

    return render(request, 'subscription/apply.html', {'sub_types': sub_types})


# Subscription Result =================================================================================================
def subscription_result(request):

    try:
        payment = Payment.objects.get(invoice_number=request.GET['id'])
    except Payment.DoesNotExist:
        context = {
            'status': False,
        }

    else:
        context = {
            'status': payment.paid_status,
            'invoice_number': payment.invoice_number
        }

    return render(request, 'subscription/result.html', context)
