# Generated by Django 2.2.6 on 2019-12-11 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0003_auto_20191211_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='video_link',
        ),
        migrations.AddField(
            model_name='video',
            name='playlist_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='playlist.Playlist'),
            preserve_default=False,
        ),
    ]
