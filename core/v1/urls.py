from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.v1.views import PropertyViewSet, PricingRuleViewSet, BookingViewSet


router = DefaultRouter()
router.register('property', PropertyViewSet, basename='property_list')
router.register('pricingrule', PricingRuleViewSet, basename='pricingrule_list')
router.register('booking', BookingViewSet, basename='booking_list')


urlpatterns = [
    path('', include(router.urls)),
]