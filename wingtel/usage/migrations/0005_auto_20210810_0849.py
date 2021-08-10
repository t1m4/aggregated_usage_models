# Generated by Django 2.2.1 on 2021-08-10 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('att_subscriptions', '0001_initial'),
        ('sprint_subscriptions', '0001_initial'),
        ('usage', '0004_bothusagerecord_type_of_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bothusagerecord',
            name='subscription_id',
        ),
        migrations.RemoveField(
            model_name='bothusagerecord',
            name='type_of_subscription',
        ),
        migrations.AddField(
            model_name='bothusagerecord',
            name='att_subscription_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='att_subscriptions.ATTSubscription'),
        ),
        migrations.AddField(
            model_name='bothusagerecord',
            name='sprint_subscription_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sprint_subscriptions.SprintSubscription'),
        ),
    ]