# Generated by Django 2.2.1 on 2022-12-19 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("subscriptions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="VoiceUsageRecord",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("price", models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ("usage_date", models.DateTimeField()),
                ("seconds_used", models.IntegerField()),
                (
                    "subscription_id",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.PROTECT, to="subscriptions.Subscription"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DataUsageRecord",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("price", models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ("usage_date", models.DateTimeField()),
                ("kilobytes_used", models.IntegerField()),
                (
                    "subscription_id",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.PROTECT, to="subscriptions.Subscription"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UsageRecord",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "type_of_usage",
                    models.CharField(choices=[("data", "DataUsage"), ("voice", "VoiceUsage")], max_length=100),
                ),
                ("price", models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ("usage_date", models.DateField()),
                ("used", models.IntegerField()),
                (
                    "subscription_id",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.PROTECT, to="subscriptions.Subscription"
                    ),
                ),
            ],
        ),
    ]
