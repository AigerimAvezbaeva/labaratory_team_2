from django.db import models

class CV(models.Model):
    job_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название искомой вакансии')
    expected_salary = models.FloatField(null=False, blank=False, verbose_name='Ожидаемая ЗП')
    job_category = models.ForeignKey('JobCategory', on_delete=models.CASCADE, verbose_name='Job Category*')
    education = models.ManyToManyField('Education', blank=True, verbose_name='Education and Qualifications')
    experience = models.ManyToManyField('Experience', blank=True, verbose_name='Work Experience')
    telegram = models.CharField(max_length=50, verbose_name='Telegram*')
    email = models.EmailField(verbose_name='Email*')
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number*', null=True, blank=True)
    languages = models.ManyToManyField('Language', blank=True, verbose_name='Languages')
    social_media = models.CharField(max_length=200, verbose_name='Social Media', null=True, blank=True)
    relocation = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')), verbose_name='Relocation', default='N')
    driving_license = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')), verbose_name='Driving License', default='N')
    is_hidden = models.BooleanField(default=False, verbose_name='Hidden')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Deleted At')



class JobCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Job Category')

    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=100, verbose_name='Education and Qualification')

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=100, verbose_name='Work Experience')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Language')

    def __str__(self):
        return self.name
