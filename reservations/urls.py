from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Southern Code"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Callenger for Southern Code"

urlpatterns = [
    path('backoffice/', admin.site.urls),
    path('api/v1/', include(("core.v1.urls", "core"), namespace="core")),
]
