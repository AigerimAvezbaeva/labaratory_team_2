from django.db import models


class JobSeeker(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский')
    )
    first_name = models.CharField(max_length=30, null=False, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, null=False, blank=True, verbose_name='Фамилия')
    birth_date = models.DateField(null=False, blank=True, verbose_name='Дата рождения')
    location = models.TextField(verbose_name='Местонахождение', null=True, blank=True)
    gender = models.CharField(max_length=1, null=False, choices=GENDER_CHOICES, default='M', verbose_name='Пол')
    citizenship = models.CharField(max_length=50, verbose_name='Гражданство', null=True, blank=True)
    cv = models.ForeignKey('webapp.CV', on_delete=models.SET_NULL, null=True, verbose_name='Резюме')
    about_me = models.TextField(verbose_name='О себе', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата и время удаления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'
