from django.db import models
from Extentions.utils import user_image_path, portfolio_image_path, degree_image_path


class InfoModel(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='Full Name')
    subtitle = models.CharField(max_length=255, verbose_name='Sub Title')
    profile = models.ImageField(upload_to=user_image_path, verbose_name='Profile')
    age = models.PositiveIntegerField(verbose_name='Age')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    skype = models.CharField(max_length=255, verbose_name='Skype')
    phone = models.PositiveBigIntegerField(verbose_name='Phone')
    address = models.TextField(verbose_name='Address')
    aboutme = models.TextField(verbose_name='About Me')
    x = models.FloatField(verbose_name='X')
    y = models.FloatField(verbose_name='Y')

    def __str__(self):
        return 'This is Information :)'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Information'
        verbose_name_plural = 'Informations'


class SkillModel(models.Model):
    TITLE_SKILL = (('beginner', 'BEGINNER'), ('expert', 'EXPERT'), ('master', 'MASTER'), ('advance', 'ADVANCE'))
    skill = models.CharField(max_length=255, verbose_name='Skill')
    percent = models.PositiveIntegerField(verbose_name='Percent')
    title = models.CharField(max_length=255, choices=TITLE_SKILL, verbose_name='Title')

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class LanguageModel(models.Model):
    language = models.CharField(max_length=255, verbose_name='Language')
    listening = models.PositiveIntegerField(verbose_name='Listening')
    speaking = models.PositiveIntegerField(verbose_name='Speaking')
    reading = models.PositiveIntegerField(verbose_name='Reading')
    writing = models.PositiveIntegerField(verbose_name='Writing')

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class ExperienceModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    place = models.CharField(max_length=255, verbose_name='Place')
    from_date = models.DateField(verbose_name='From')
    to_date = models.DateField(verbose_name='To', blank=True, null=True)
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'


class EducationModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    place = models.CharField(max_length=255, verbose_name='Place')
    from_date = models.DateField(verbose_name='From')
    to_date = models.DateField(verbose_name='To', blank=True, null=True)
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'


class DegreeModel(models.Model):
    image = models.ImageField(upload_to=degree_image_path, verbose_name='Image')
    title = models.CharField(max_length=255, verbose_name='Title')
    created = models.DateField(verbose_name='Created')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Degree'
        verbose_name_plural = 'Degrees'


class PortfolioModel(models.Model):
    image = models.ImageField(upload_to=portfolio_image_path, verbose_name='Image')
    title = models.CharField(max_length=255, verbose_name='Full Name')
    techs = models.CharField(max_length=255, verbose_name='Technologies')
    description = models.TextField(verbose_name='Description')
    created = models.DateField(verbose_name='Created')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'


class ReferenceModel(models.Model):
    profile = models.ImageField(upload_to=user_image_path, verbose_name='Profile')
    full_name = models.CharField(max_length=255, verbose_name='Full Name')
    ref_title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    created = models.DateField(verbose_name='Created')

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Reference'
        verbose_name_plural = 'References'


class LinksModel(models.Model):
    github = models.CharField(max_length=255, verbose_name='GitHub')
    instagram = models.CharField(max_length=255, verbose_name='Instagram')
    linkedin = models.CharField(max_length=255, verbose_name='LinkedIn')
    telegram = models.CharField(max_length=255, verbose_name='Telegram')

    def __str__(self):
        return 'this is Links :)'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Link'
        verbose_name_plural = 'Links'


class ContactModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    email_address = models.EmailField(max_length=255, verbose_name='E-mail')
    message = models.TextField(verbose_name='Message')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    is_read = models.BooleanField(default=False, verbose_name='Is Read?')
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

