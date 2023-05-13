# ViteApp_APITest
API автотесты сайта http://34.141.58.52:8080/#/:
- получения уникального токена пользователя по указанным email и password;
- получения ID своего профиля;
- создание питомца;
- добавления фото питомца (из папки tests>photos);
- получение информации о питомце (имя, гендер, возраст, id владельца);
- удаление питомца;
- изменение питомца (имя, гендер, возраст, вид);
- оставить комментарий питомцу;
- поставить лайк питомцу;
- удаление всех питомцев.

Тесты расположены в файле test_pet.py.

Функции, на которые ссылаются тесты, расположены в файле api.py

В файле settings.py находятся данные для авторизации.

В файле requirement.ini находятся необходимые для работы автотестов пакеты, которые следует установить в настройках.
