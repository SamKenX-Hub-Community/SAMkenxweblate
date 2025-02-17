# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.7 on 2020-07-29 12:00

from django.db import migrations

import weblate.utils.fields
import weblate.utils.validators


class Migration(migrations.Migration):
    dependencies = [
        ("weblate_auth", "0011_unique_case_insensitive"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=weblate.utils.fields.EmailField(
                max_length=190,
                null=True,
                unique=True,
                validators=[weblate.utils.validators.validate_email],
                verbose_name="E-mail",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=weblate.utils.fields.UsernameField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Username may only contain letters, numbers or the following characters: @ . + - _",
                max_length=150,
                unique=True,
                validators=[weblate.utils.validators.validate_username],
                verbose_name="Username",
            ),
        ),
    ]
