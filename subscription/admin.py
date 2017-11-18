from django.contrib import admin

from .models import Subscription


class AmountListFilter(admin.SimpleListFilter):
    title = 'Amounts'
    parameter_name = 'Amounts'

    def lookups(self, request, model_admin):
        return (
            ('30000', '30000'),
            ('42000', '42000'),
            ('60000', '60000'),
            ('80000', '80000'),
            ('45000', '45000'),
            ('54000', '54000'),
            ('90000', '90000'),
            ('108000', '108000')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(payment__amount=int(self.value()))


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birthday', 'education', 'postal_code', 'phone_number', 'mobile_number',
                    'email', 'address', 'amount', 'is_paid', 'paid_time']
    readonly_fields = ['created_time', 'first_name', 'last_name', 'birthday', 'education', 'postal_code', 'phone_number',
                       'mobile_number', 'email', 'address', 'amount', 'payment', 'is_paid', 'paid_time']
    list_filter = ('is_paid', AmountListFilter, )
    search_fields = ('first_name', 'last_name', 'phone_number', 'mobile_number', 'email')
    actions = None
    list_display_links = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def amount(self, obj):
        return obj.payment.amount


admin.site.register(Subscription, SubscriptionAdmin)
