from django.shortcuts import render, redirect

from .forms import SubscriptionForm
from payments.models import Payment, Gateway


# Subscription Apply ==================================================================================================
def subscription_apply(request):

    sub_amounts = {'1': 3103431,
                   '2': 200,
                   '3': 60000,
                   '4': 80000}

    sub_types = [('1', "شش شماره + پست سفارشی = 30000 تومان"),
                 ('2', "شش شماره + DVD + پست سفارشی = 42000 تومان"),
                 ('3', "دوازده شماره + پست سفارشی = 60000 تومان"),
                 ('4', "دوازده شماره + DVD + پست سفارشی = 80000 تومان")]

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            amount = sub_amounts[str(form.cleaned_data['subscription_type'])]
            new_sub = form.save(commit=False)
            gateway = Gateway.objects.first()
            gateway_id = {'id': gateway.id}
            payment = Payment.objects.create(amount=amount, gateway=gateway, response_type=2)
            new_sub.amount = amount
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
