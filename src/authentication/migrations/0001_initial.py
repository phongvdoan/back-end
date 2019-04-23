# Generated by Django 2.2 on 2019-04-22 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=256, null=True, unique=True
                    ),
                ),
                ("zip", models.CharField(blank=True, max_length=256, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("encrypted_password", models.CharField(max_length=256)),
                (
                    "reset_password_token",
                    models.CharField(
                        blank=True, max_length=256, null=True, unique=True
                    ),
                ),
                ("reset_password_sent_at", models.DateTimeField(blank=True, null=True)),
                ("remember_created_at", models.DateTimeField(blank=True, null=True)),
                ("sign_in_count", models.IntegerField()),
                ("current_sign_in_at", models.DateTimeField(blank=True, null=True)),
                ("last_sign_in_at", models.DateTimeField(blank=True, null=True)),
                (
                    "current_sign_in_ip",
                    models.GenericIPAddressField(blank=True, null=True),
                ),
                (
                    "last_sign_in_ip",
                    models.GenericIPAddressField(blank=True, null=True),
                ),
                ("mentor", models.BooleanField(blank=True, null=True)),
                ("first_name", models.CharField(blank=True, max_length=256, null=True)),
                ("last_name", models.CharField(blank=True, max_length=256, null=True)),
                ("timezone", models.CharField(blank=True, max_length=256, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
                ("verified", models.BooleanField()),
                ("state", models.CharField(blank=True, max_length=256, null=True)),
                ("address_1", models.CharField(blank=True, max_length=256, null=True)),
                ("address_2", models.CharField(blank=True, max_length=256, null=True)),
                ("city", models.CharField(blank=True, max_length=256, null=True)),
                ("username", models.CharField(blank=True, max_length=256, null=True)),
                ("volunteer", models.BooleanField(blank=True, null=True)),
                (
                    "branch_of_service",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("years_of_service", models.FloatField(blank=True, null=True)),
                ("pay_grade", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "military_occupational_specialty",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("github", models.CharField(blank=True, max_length=256, null=True)),
                ("twitter", models.CharField(blank=True, max_length=256, null=True)),
                ("linkedin", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "employment_status",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("education", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "company_role",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "education_level",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("interests", models.CharField(blank=True, max_length=256, null=True)),
                ("scholarship_info", models.BooleanField(blank=True, null=True)),
                ("role_id", models.IntegerField(blank=True, null=True)),
                (
                    "military_status",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
            ],
            options={"db_table": "users", "managed": False},
        ),
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("zip", models.CharField(blank=True, max_length=256, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("remember_created_at", models.DateTimeField(blank=True, null=True)),
                ("sign_in_count", models.IntegerField(blank=True, null=True)),
                ("mentor", models.BooleanField(blank=True, default=False, null=True)),
                ("timezone", models.CharField(blank=True, max_length=256, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
                ("verified", models.BooleanField(default=False)),
                ("state", models.CharField(blank=True, max_length=256, null=True)),
                ("address_1", models.CharField(blank=True, max_length=256, null=True)),
                ("address_2", models.CharField(blank=True, max_length=256, null=True)),
                ("city", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "volunteer",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                (
                    "branch_of_service",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("years_of_service", models.FloatField(blank=True, null=True)),
                ("pay_grade", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "military_occupational_specialty",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("github", models.CharField(blank=True, max_length=256, null=True)),
                ("twitter", models.CharField(blank=True, max_length=256, null=True)),
                ("linkedin", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "employment_status",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("education", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "company_role",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "education_level",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("interests", models.CharField(blank=True, max_length=256, null=True)),
                ("scholarship_info", models.BooleanField(blank=True, null=True)),
                ("role_id", models.IntegerField(blank=True, null=True)),
                (
                    "military_status",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("slack_id", models.CharField(max_length=16)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
