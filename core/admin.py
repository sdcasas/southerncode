from django.contrib import admin

from core.models import Property, PricingRule, Booking


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(PricingRule)
class PricingRuleAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass