# Generated by Django 3.2.2 on 2021-05-19 09:50

from django.db import migrations
from django.db.models.signals import post_migrate


def assing_permissions(apps, schema_editor):
    def on_migrations_complete(sender=None, **kwargs):
        Group = apps.get_model("auth", "Group")
        Permission = apps.get_model("auth", "Permission")
        handle_payments = Permission.objects.filter(
            codename="handle_payments", content_type__app_label="payment"
        ).first()
        for group in Group.objects.iterator():
            group.permissions.add(handle_payments)

    post_migrate.connect(on_migrations_complete)


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0028_drop_searchable_key"),
        ("channel", "0003_alter_channel_default_country"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payment",
            options={
                "ordering": ("pk",),
                "permissions": (("handle_payments", "Handle payments"),),
            },
        ),
        migrations.RunPython(assing_permissions, migrations.RunPython.noop),
    ]
