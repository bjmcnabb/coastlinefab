# Generated by Django 4.2 on 2023-08-02 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0004_alter_album_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="albumimage",
            name="album",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="gallery.album"
            ),
        ),
    ]
