# Пульт охраны банка

Сайт, показывающий посетителей хранилища банка. На главной странице указаны обладатели активных карт доступа. Также по ссылке сверху можно перейти на страницу, показывающую текущих посетителей хранилища. Кроме того, с главной страници можно перейти на страницу обладателя карты доступа, в которой указаны все его посещения хранилища.

Сайт подключен к удаленной базе данных, содержащей пропуска и визиты сотрудников банка.

## Запуск

* Скачать код
* Установить требуемые библиотеки командой
```
python -m pip install -r requirements.txt
```
* Заполнить `.env` файл по нижеуказанному шаблону и сохранить рядом с файлом `setitings.py`:
	* `ENGINE` - адаптер базы данных
	* `HOST` - адрес базы данных
	* `PORT` - номер порта
	* `NAME` - имя поста охраны в базе данных
	* `LOGIN` - логин
	* `PASSWORD` - пароль
	* `DEBUG` - для включения режима отладки поставить `True`. Для выключения - `False`
* Сайт запускается командой:
```
python manage.py runserver 0.0.0.0:8000
```
* Сайт открывается по адресу http://127.0.0.1:8000

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
