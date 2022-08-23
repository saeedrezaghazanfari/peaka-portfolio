from django.shortcuts import render
from .forms import ContactForm
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


def home_page(request):
    contact_form = ContactForm(request.POST or None)

    if request.POST:
        pass

    return render(request, 'portfolio/home.html', {
        'info': InfoModel.objects.last(),
        'links': LinksModel.objects.last(),
        'skills1': SkillModel.objects.all()[0:SkillModel.objects.count()/2],
        'skills2': SkillModel.objects.all()[SkillModel.objects.count()/2:],
        'exps': ExperienceModel.objects.all(),
        'edus': EducationModel.objects.all(),
        # 'degrees': DegreeModel.objects.all(),
        'ports': PortfolioModel.objects.all(),
        # 'refs': ReferenceModel.objects.all(),
        # 'form': contact_form,
    })
