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
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    # TODO Если для поля важна точность, то лучше использовать поле models.DecimalField
    # TODO Поэтому лучше использовать его для полей salary_min и salary_max
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#decimalfield
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    # TODO по условию задачи тут должно быть поле published_at
    posted = models.DateField()

# TODO здесь осталось большое кол-во пробелов, Вы не забыли проверить проект через flake8? :)




