# Generated by Django 4.0.4 on 2022-08-26 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('audis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500, null=True)),
                ('question_response', models.CharField(choices=[('Core', 'Core'), ('Tech', 'Tech'), ('Both Core and Tech', 'Both Core and Tech')], max_length=100)),
                ('question_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]