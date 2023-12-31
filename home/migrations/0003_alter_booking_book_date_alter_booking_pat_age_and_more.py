# Generated by Django 4.1.2 on 2023-06-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_booking_pat_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="book_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="pat_age",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="pat_email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="pat_phone",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
