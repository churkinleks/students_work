from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Company(models.Model):
    # TODO поле id в данном случае не следует создавать вручную, так как оно само будет создано автоматически
    id = models.IntegerField(primary_key=True)
    # TODO по условия задачи тут должно быть поле name
    title = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    # TODO поле id в данном случае не следует создавать вручную, так как оно само будет создано автоматически
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    # TODO Старайтесь придерживаться одного стиля строк,т.е. либо двойные кавычки во всем проекте, либо одинарные
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    # TODO В зарплате также могут присутствовать копейки, поэтому потребуется использовать тип Float или Decimal.
    # TODO 2-ой пункт в README.md объясняет, почему лучше использовать Decimal, а не Float
    # TODO В Django поле Decimal создается следующим образом -> models.DecimalField
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#decimalfield
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    # TODO по условию задачи тут должно быть поле published_at
    posted = models.DateField()

# TODO здесь осталось большое кол-во пробелов, Вы не забыли проверить проект через flake8? :)




