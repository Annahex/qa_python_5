# Проект автоматизации тестирования Stellar Burgers
1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v. 

### Локаторы в тестах

1. `.//main//form//input` - инпуты на странице регистрации или логина
2. `.//main//form//input[@name='name']` - инпуты на странице регистрации или логина для email и имени (почему то с одинаковым name)
3. `.//main//form//input[@name='Пароль']` - инпут на странице регистрации или логина для пароля
4. `.//main//form/button` - кнопка "Зарегистрироваться" или "Войти"
5. `.//fieldset//p[text()='Некорректный пароль']` - текстовый элемент с ошибкой о неверном пароле
6. `.//main/section//button[text()='Войти в аккаунт']` - кнопка "Войти в аккаунт" на главной
7. `.//nav//p[text()='Личный Кабинет']/parent::a` - кнопка "Личный кабинет" в навбаре
8. `.//main/div/div/p/a` - кнопка "Войти" на странице регистрации
9. `.//main/div/div/p/a` - кнопка "Войти" на странице восстановления пароля
10. `.//nav//p[text()='Конструктор']/parent::a` - кнопка "Конструктур" в навбаре
11. `.//nav//div/a[@href='/']` - лого в навбаре
12. `.//main/div/nav/ul/li/button[text()='Выход']` - кнопка выхода в личном кабинете
13. `.//main/section/div/div/span[text()='Булки']/parent::div` - кнопка "Булки" на главной
14. `.//main/section/div/div/span[text()='Соусы']/parent::div` - кнопка "Соусы" на главной
15. `.//main/section/div/div/span[text()='Начинки']/parent::div` - кнопка "Начинки" на главной
16. `.//main/section/div/h2[text()='Булки']` - заголовок "Булки" на главной
17. `.//main/section/div/h2[text()='Соусы']` - заголовок "Соусы" на главной 
18. `.//main/section/div/h2[text()='Начинки']` - заголовок "Начинки" на главной