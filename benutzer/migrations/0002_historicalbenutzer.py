# Generated by Django 3.2.6 on 2021-11-30 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('benutzer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalBenutzer',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.IntegerField(blank=True, db_column='bnz_id', db_index=True, verbose_name='ID')),
                ('username', models.CharField(blank=True, db_column='bnz_bname', db_index=True, max_length=64, null=True, verbose_name='Benutzername')),
                ('email', models.EmailField(blank=True, db_column='bnz_email', default='', max_length=128, verbose_name='e. Postadresse')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Benutzer',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]