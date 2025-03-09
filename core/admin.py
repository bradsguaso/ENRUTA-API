from django.contrib import admin

from core.models import Charge


class ChargeAdmin:
    list_display = ("name", "description")


admin.site.register(Charge)
