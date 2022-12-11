# Generated by Django 3.1.14 on 2022-12-11 18:25

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0006_add_slugs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True)),
                ('icon', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=False, quality=75, scale=None, size=[50, 50], upload_to='categories', verbose_name='Icon')),
            ],
        ),
        migrations.AddField(
            model_name='usersubscription',
            name='recurring_payin_registration_id',
            field=models.CharField(blank=True, editable=False, max_length=128),
        ),
        migrations.AlterField(
            model_name='plancost',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, help_text='the cost per recurrence of the plan', max_digits=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='plan_description',
            field=models.TextField(blank=True, default='', help_text='a description of the subscription plan'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersubscription',
            name='active',
            field=models.BooleanField(default=False, help_text='whether this subscription is active or not'),
        ),
        migrations.AddField(
            model_name='usersubscription',
            name='categories',
            field=models.ManyToManyField(blank=True, to='subscriptions.Category'),
        ),
    ]
