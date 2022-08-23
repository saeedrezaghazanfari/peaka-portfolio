from django.contrib import admin
from .models import (
    InfoModel,
    SkillModel,
    ExperienceModel,
    EducationModel,
    DegreeModel,
    PortfolioModel,
    ReferenceModel,
    LinksModel,
    ContactModel,
)


class InfoModel_admin(admin.ModelAdmin):
    list_display = ['__str__']
    ordering = ['-id']

class SkillModel_admin(admin.ModelAdmin):
    list_display = ['skill', 'percent', 'title']
    ordering = ['-id']

class ExperienceModel_admin(admin.ModelAdmin):
    list_display = ['title', 'place']
    ordering = ['-id']

class EducationModel_admin(admin.ModelAdmin):
    list_display = ['title', 'place']
    ordering = ['-id']

class DegreeModel_admin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['-id']

class PortfolioModel_admin(admin.ModelAdmin):
    list_display = ['title', 'created']
    ordering = ['-id']

class ReferenceModel_admin(admin.ModelAdmin):
    list_display = ['full_name', 'created']
    ordering = ['-id']

class LinksModel_admin(admin.ModelAdmin):
    list_display = ['__str__']
    ordering = ['-id']

class ContactModel_admin(admin.ModelAdmin):
    list_display = ['name', 'created', 'is_read']
    ordering = ['-id']

admin.site.register(InfoModel, InfoModel_admin)
admin.site.register(SkillModel, SkillModel_admin)
admin.site.register(ExperienceModel, ExperienceModel_admin)
admin.site.register(EducationModel, EducationModel_admin)
admin.site.register(DegreeModel, DegreeModel_admin)
admin.site.register(PortfolioModel, PortfolioModel_admin)
admin.site.register(ReferenceModel, ReferenceModel_admin)
admin.site.register(LinksModel, LinksModel_admin)
admin.site.register(ContactModel, ContactModel_admin)