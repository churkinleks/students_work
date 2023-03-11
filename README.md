# Проверка

Добрый день), у Вас получился действительно хороший и полноценный проект, и ниже я приведу список общих рекомендаций, 
которые помогут улучшить проект. Также в самом коде я вставлю **TODO** для объяснения локальных улучшений по коду.

1. Вы правильно написали все эндпоинты, но их следует перенсти в приложение [vacancies](vacancies). Т.е. в 
   приложении [vacancies](vacancies) нужно создать модуль **urls.py** и туда перенести большую часть эндпоинтов, как 
   это было рассказано на лекции (тут я ссылку оставлю на лекцию из SkyPro).
2. Для зарплат и цен в моделях лучше использовать такой тип данных как 
   [Decimal](https://docs.python.org/3/library/decimal.html#module-decimal), так как он гарантирует точность и 
   нивелирует недостатки Float (Float проигрывает из-за погрешности). Если Вы перейдете по ссылке, то в первых же 
   пунктах сможете найти объяснение тому, в чем разница между Float и Decimal.

# Строгая проверка
Тут будут мои замечания, которые в оригинале не будут присутствовать в проверке для начинающих специалистов,
но для опытных я бы их учел

1. Вы назвали папку с конфигурацией проекта как [junior_developers](junior_developers), это не является ошибкой, но 
   другим разработчикам будет сложно понять за что отвечает эта папка в большом проекте, поэтому я рекомендую 
   назвать эту папку иначе, например **core**.
2. Вы хорошо справились с шаблонами, но нужно немного поменять архитектуру, чтобы не было коллизий имен. Т.е нужно 
   сделать следующую иерархию _templates/{имя приложения}/{сам HTML файл}_
3. В папке static следует создать папки **images**, **css** и **js**, после чего все изображения перенести в папку 
   images.
4. Подумайте о том, почему поле code стоит сделать уникальным в модели Specialty
5. Постарайтесь добавить больше аннотации типов для улучшения надежности кода
