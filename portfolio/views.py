from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactForm
from .models import (
    InfoModel,
    SkillModel,
    LanguageModel,
    ExperienceModel,
    EducationModel,
    DegreeModel,
    PortfolioModel,
    ReferenceModel,
    LinksModel
)


# url: /
def home_page(request):
    contact_form = ContactForm(request.POST or None)

    if request.POST:
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank You for Submission!')
            return redirect('/')

    return render(request, 'portfolio/home.html', {
        'info': InfoModel.objects.last(),
        'links': LinksModel.objects.last(),
        'skills1': SkillModel.objects.all()[0:SkillModel.objects.count()/2],
        'skills2': SkillModel.objects.all()[SkillModel.objects.count()/2:],
        'langs': LanguageModel.objects.all(),
        'exps': ExperienceModel.objects.all(),
        'edus': EducationModel.objects.all(),
        'degrees': DegreeModel.objects.all(),
        'ports': PortfolioModel.objects.all(),
        'refs': ReferenceModel.objects.all()[:2],
        'form': contact_form,
    })
