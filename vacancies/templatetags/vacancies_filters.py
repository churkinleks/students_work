from django import template

register = template.Library()


@register.filter
def vacancy_declension(num):
    # TODO чтобы взять последнее число, воспользуйтесь след. выражением num % 10
    # TODO (тут должна быть ссылка на лекцию SkyPro на тему // и %)
    unit = int(str(num)[-1])
    # TODO здесь можно воспользоваться новым оператором % для оптимизации кода
    tens = int(str(num // 10)[-1])
    if unit == 1 and tens != 1:
        return f'{num} вакансия'
    elif 1 < unit < 5 and tens != 1:
        return f'{num} вакансии'
    else:
        return f'{num} вакансий'


@register.filter
def people_declension(num):
    # TODO тут тоже на забудьте оптимизировать код :)
    unit = int(str(num)[-1])
    tens = int(str(num // 10)[-1])
    if 1 < unit < 5 and tens != 1:
        return f'{num} человека'
    else:
        return f'{num} человек'


@register.filter
def convert_to_list(s):
    return s.split(', ')
