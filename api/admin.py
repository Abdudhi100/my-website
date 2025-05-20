
from django.contrib import admin
from .models import Project, Education, Certificate, Experience, Skill, Contact
# Register your models here
# filepath: c:\Users\owner\OneDrive\Desktop\DHIKRULLAH ABDULLAH ADEMOLA\DhikrullahAbdullah\DhikrullahAbdullah\portfolio\api\admin.py


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'base_url', 'image')
    



@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'year')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')