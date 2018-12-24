# Generated by Django 2.1.4 on 2018-12-24 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='At',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=8)),
                ('belongs_id', models.IntegerField()),
                ('ater', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='ater', to=settings.AUTH_USER_MODEL)),
                ('vic_at', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vic_at', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Base_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Focus_Rela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('focuser', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='focuser', to=settings.AUTH_USER_MODEL)),
                ('vic_focus', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vic_focus', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('time', models.TimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liker', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('base_post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='demo.Base_Post')),
            ],
            bases=('demo.base_post',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('base_post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='demo.Base_Post')),
                ('hits', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
            ],
            bases=('demo.base_post',),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('base_post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='demo.Base_Post')),
                ('belongs', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demo.Comment')),
                ('replyer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='replyer', to=settings.AUTH_USER_MODEL)),
                ('vic_reply', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vic_reply', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('demo.base_post',),
        ),
        migrations.AddField(
            model_name='base_post',
            name='poster',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='vic_like',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demo.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='belongs',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demo.Post'),
        ),
    ]