from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from model_utils import Choices

from wingtel.plans.models import Plan


class Subscription(models.Model):
    ONE_KILOBYTE_PRICE = Decimal("0.001")
    ONE_SECOND_PRICE = Decimal("0.001")

    """Represents a subscription with AT&T for a user and a single device"""
    STATUS = Choices(
        ("new", "New"),
        ("active", "Active"),
        ("suspended", "Suspended"),
        ("expired", "Expired"),
    )
    SUBSCRIPTION_TYPE = Choices(
        ("att", "Att"),
        ("sprint", "Sprint"),
    )
    type_of_subscription = models.CharField(max_length=10, choices=SUBSCRIPTION_TYPE)

    user = models.ForeignKey(User, on_delete=models.PROTECT)  # Owning user

    plan = models.ForeignKey(Plan, null=True, on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=STATUS, default=STATUS.new)

    device_id = models.CharField(max_length=20, blank=True, default="")
    phone_number = models.CharField(max_length=20, blank=True, default="")
    phone_model = models.CharField(max_length=128, blank=True, default="")
    network_type = models.CharField(max_length=5, blank=True, default="")
    sprint_id = models.CharField(max_length=16, null=True)

    effective_date = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{}; device - {}".format(self.type_of_subscription, self.device_id)
