# Generated by Django 3.2.9 on 2021-12-08 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20211208_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.profile'),
        ),
        migrations.AlterField(
            model_name='followsystem',
            name='follower',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_follower', to='gallery.profile'),
        ),
        migrations.AlterField(
            model_name='followsystem',
            name='following',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_following', to='gallery.profile'),
        ),
    ]
