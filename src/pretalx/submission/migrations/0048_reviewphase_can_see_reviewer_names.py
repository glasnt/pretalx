# Generated by Django 3.0.5 on 2020-07-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0047_track_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="reviewphase",
            name="can_see_reviewer_names",
            field=models.BooleanField(default=True),
        ),
    ]