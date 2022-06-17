# Generated by Django 4.0.5 on 2022-06-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_polls_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='polls',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='polls',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, to='polls.ipmodel'),
        ),
    ]