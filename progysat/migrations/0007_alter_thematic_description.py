# Generated by Django 3.2.19 on 2023-05-31 09:45

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('progysat', '0006_auto_20230530_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thematic',
            name='description',
            field=wagtail.fields.RichTextField(blank=True, default='', max_length=500, null=True),
        ),
    ]