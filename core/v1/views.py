from rest_framework import viewsets

from core.models import Property, Booking, PricingRule
from core.v1.serializers import PropertySerializer, BookingSerializer, PricingRuleSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    model = Property
    serializer_class = PropertySerializer
    queryset = Property.objects.all()


class BookingViewSet(viewsets.ModelViewSet):
    model = Booking
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class PricingRuleViewSet(viewsets.ModelViewSet):
    model = PricingRule
    serializer_class = PricingRuleSerializer
    queryset = PricingRule.objects.all()
