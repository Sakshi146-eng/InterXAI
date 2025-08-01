# Generated by Django 5.2.3 on 2025-07-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0013_alter_interviewsession_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='customquestion',
            name='type',
            field=models.CharField(choices=[('resume', 'resume'), ('interview', 'interview')], default='technical', max_length=20),
        ),
        migrations.AlterField(
            model_name='interviewsession',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('cheated', 'cheated'), ('ongoing', 'Ongoing')], default='scheduled', max_length=20),
        ),
    ]
