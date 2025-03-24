<h1>⌨️TypeFlow - Сайт для обучения скоропечатанию</h1>
<p>
    <strong>TypeFlow</strong> — это веб-приложение, созданное для улучшения навыков скоропечатания. 
    Оно включает в себя функционал для обучения, тестирования скорости печати и анализа результатов. 
    Вы можете проходить тесты с уже загруженными текстами или использовать собственные. 
    После каждого теста результаты сохраняются, что позволяет отслеживать ваш прогресс.
</p>
<p>
    Сайт разработан на <strong>Django</strong> с использованием гибкого интерфейса, удобного для пользователей.
</p>
<p>Основные возможности сайта:</p>
<ul>
    <li>Обучение навыкам скоропечатания.📚</li>
    <li>Тестирование скорости печати с подсчетом символов в минуту (зн/мин).🚀</li>
    <li>Загрузка пользовательских текстов для индивидуального тестирования.💡</li>
    <li>Регистрация и управление профилем.⚙️</li>
    <li>Хранение результатов тестирования.📝</li>
</ul>

<h1>⭐Запуск проекта⭐</h1>
<ul>
	<li>
	1. Клонируйте репозиторий:  
	```bash
	git clone https://github.com/sserebrinka/typing-trainer
	cd typing_trainer
	```
	</li>
	<li>
	2. Установите все зависимости:
	```bash
	docker-compose up --build
	```
	Это создаст и запустит все необходимые контейнеры для проекта.
	Запуск контейнеров в фоновом режиме:
	```bash
	docker-compose up -d
	```
	После того как контейнеры будут построены и запущены, проект будет доступен по адресу http://localhost:8000
	</li>
	<li>
	3. Остановить все контейнеры:
	```bash
	docker-compose down
	```
	</li>
</ul>
<ul>
    <li>
        <h1>⭐1. Страница обучения⭐</h1>
        <img src="https://github.com/user-attachments/assets/30386a1a-c51a-40a1-91ca-0e81f7bb4c89" alt="Страница обучения">
    </li>
    <li>
        <h1>⭐2. Страница тестирования с возможностью обновлять текст⭐</h1>
        <p>Тексты можно загружать при помощи Django админки.</p>
        <img src="https://github.com/user-attachments/assets/f2de76a5-7861-4494-a600-822ba29b8a3e" alt="Страница тестирования">
        <p>Отсчет времени начинается с момента написания пользователем текста.</p>
        <img src="https://github.com/user-attachments/assets/0c5134b3-1504-4127-8aae-fb106841184a" alt="Тестирование">
        <p>Скорость печати вычисляется в символах в минуту (зн/мин). Формула: <strong>длина текста / затраченное время в минутах</strong>.</p>
    </li>
    <li>
        <h1>⭐3. Страница с возможностью напечатать свой текст и провести тестирование на нем⭐</h1>
        <img src="https://github.com/user-attachments/assets/46e3e191-6a53-47b0-b98c-d491647231fe" alt="Свой текст">
		<img src="https://github.com/user-attachments/assets/e0ecff2d-1ff4-4cfc-b272-74f05e9093a3" alt="Свой текст в тестировании">
    </li>
    <li>
        <h1>⭐4. Регистрация⭐</h1>
        <img src="https://github.com/user-attachments/assets/0c18e9da-035f-491f-b331-fdd8dd5d9c68" alt="Регистрация">
        <p>После успешной регистрации пользователя перекидывает на страницу входа.</p>
        <img src="https://github.com/user-attachments/assets/8db7e1ed-840f-40fe-919f-22a7d500c2ef" alt="Страница входа">
    </li>
    <li>
        <h1>⭐5. Профиль⭐</h1>
        <img src="https://github.com/user-attachments/assets/53218ba8-760c-42ce-afc6-37081cbaa2fc" alt="Профиль">
    </li>
    <li>
        <h1>⭐6. Результаты тестирования⭐</h1>
        <p>Результаты каждого тестирования заносятся в таблицу "Мои результаты тестирования".</p>
        <p>В профиле указано:</p>
        <ul>
            <li>Количество пройденных тестов.</li>
            <li>Общее время, затраченное на тесты.</li>
            <li>Рекорд по скорости печати.</li>
        </ul>
        <p>Пример результата на странице тестирования:</p>
        <img src="https://github.com/user-attachments/assets/e69616cd-40da-4f94-9861-a5dd51585a04" alt="Результат тестирования">
        <p>Результат тестирования на странице профиля:</p>
        <img src="https://github.com/user-attachments/assets/f6cd3225-e887-4d79-b5e5-dd4fac1ca2a5" alt="Результат на странице профиля">
        <p>Скроллбар появляется, когда результатов тестирования становится больше 3.</p>
        <img src="https://github.com/user-attachments/assets/c151fb3a-1471-4711-ae68-5df9281617d2" alt="Скроллбар">
    </li>
</ul>


