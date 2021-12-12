# Generated by Django 4.0 on 2021-12-11 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('nombre', models.CharField(max_length=15, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=15, verbose_name='Apellido')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('tipo_documento', models.CharField(max_length=15, verbose_name='Tipo Documento')),
                ('celular', models.BigIntegerField(verbose_name='Celular')),
                ('cedula', models.BigIntegerField(verbose_name='Cedula')),
                ('direccion', models.CharField(max_length=256, verbose_name='Direccion')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('rol', models.CharField(max_length=15, verbose_name='Rol')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]