from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render

from vacancies.models import Specialty, Company, Vacancy


def main_view(request):
    # TODO Хорошая работа!
    # TODO Попробуйте только убрать all(), так как вроде и без этого должно работать
    specialties = Specialty.objects.annotate(num_vacancy=Count('vacancies')).all()
    companies = Company.objects.annotate(num_vacancy=Count('vacancies')).all()

    return render(request, 'index.html', {
        'specialties': specialties,
        'companies': companies
    })


def jobs_views(request, specialty_code=None):
    if specialty_code:
        # TODO Вы правильно делаете, что обрабатываете исключения,
        # TODO но также Вы можете воспользоваться следующей функцией для сокращения кода

        # TODO from django.shortcuts import get_object_or_404
        # TODO specialty = get_object_or_404(Specialty, code=specialty_code)

        # TODO по факту данная функция делает то же самое, что и код ниже, просто она уменьшает кол-во кода
        try:
            specialty = Specialty.objects.get(code=specialty_code)
        except:
            raise Http404()
        vacancies = Vacancy.objects.filter(specialty__code=specialty_code).all()
    else:
        specialty = None
        vacancies = Vacancy.objects.all()

    return render(request, 'vacancies.html', {
        'vacancies': vacancies,
        'specialty_code': specialty_code,
        'specialty': specialty,
    })


def company_view(request, company_id):
    # TODO можно воспользоваться get_object_or_404
    try:
        company = Company.objects.get(id=company_id)
    except:
        raise Http404()
    vacancies = Vacancy.objects.filter(company__id=company_id).all()

    return render(request, 'company.html', {
        'company': company,
        'vacancies': vacancies,
    })


def vacancy_view(request, job_id):
    # TODO можно воспользоваться get_object_or_404
    try:
        vacancy = Vacancy.objects.get(id=job_id)
    except:
        raise Http404()

    return render(request, 'vacancy.html', {
        'vacancy': vacancy,
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound('<br/><h1>Ошибка 404</h1><h2>Запрашиваемый ресурс не найден</h2>')


def custom_handler500(request):
    return HttpResponseServerError('<br/><h1>Ошибка 500</h1><h2>Ошибка запроса. Отказано в обработке</h2>')


