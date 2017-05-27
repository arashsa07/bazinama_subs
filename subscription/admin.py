from django.contrib import admin

from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birthday', 'education', 'postal_code', 'phone_number', 'mobile_number',
                    'email', 'address', 'subscription_type', 'is_paid', 'paid_time']
    readonly_fields = ['created_time', 'first_name', 'last_name', 'birthday', 'education', 'postal_code', 'phone_number',
                       'mobile_number', 'email', 'address', 'subscription_type', 'subscription_type', 'payment',
                       'is_paid', 'paid_time']
    list_filter = ('is_paid', 'subscription_type', )
    search_fields = ('first_name', 'last_name', 'phone_number', 'mobile_number', 'email')
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Subscription, SubscriptionAdmin)
