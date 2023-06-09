# Generated by Django 3.2.19 on 2023-05-30 11:49

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('progysat', '0005_footerdetail_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thematic',
            name='icon',
        ),
        migrations.AddField(
            model_name='thematic',
            name='description',
            field=wagtail.fields.RichTextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='thematic',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtaildocs.document'),
        ),
    ]
