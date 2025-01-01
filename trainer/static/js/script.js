document.addEventListener("DOMContentLoaded", () => {
    const textToType = document.getElementById("text-to-type").textContent.trim();
    const container = document.getElementById("text-to-type");
    const userInput = document.getElementById("user-input");
    const resultsContainer = document.getElementById("results");

    // Преобразуем текст в отдельные спаны для стилизации
    container.innerHTML = '';
    for (let i = 0; i < textToType.length; i++) {
        const span = document.createElement('span');
        span.textContent = textToType[i];
        container.appendChild(span);
    }

    let startTime = null;
    let errors = 0;

    // Функция для обновления текущей буквы
    const highlightCurrentLetter = (index) => {
        for (let i = 0; i < container.children.length; i++) {
            const span = container.children[i];
            if (i === index) {
                span.classList.add("highlight"); // Текущая буква
            } else {
                span.classList.remove("highlight");
            }
        }
    };

    userInput.addEventListener("input", () => {
        if (!startTime) startTime = new Date(); // Фиксируем время первого ввода

        const typedText = userInput.value;
        const currentLength = typedText.length;

        // Сброс стилей символов и подсчёт ошибок
        errors = 0;
        let correctCount = 0;
        for (let i = 0; i < textToType.length; i++) {
            const span = container.children[i];
            if (i < currentLength) {
                if (typedText[i] === textToType[i]) {
                    span.classList.add("correct");
                    span.classList.remove("wrong", "highlight");
                    correctCount++;
                } else {
                    span.classList.add("wrong");
                    span.classList.remove("correct", "highlight");
                    errors++;
                }
            } else {
                span.classList.remove("correct", "wrong");
            }

            // Проверка на пробелы и выделение их красным
            if (typedText[i] === " " && textToType[i] !== " ") {
                span.classList.add("wrong");
                span.classList.remove("correct", "highlight");
                errors++;
            }
        }

        // Выделяем текущую букву
        if (currentLength < textToType.length) {
            highlightCurrentLetter(currentLength);
        }

        // Проверка завершения
        if (currentLength === textToType.length) {
            const endTime = new Date();
            const timeTaken = ((endTime - startTime) / 1000).toFixed(2); // Время в секундах
            const timeInMinutes = timeTaken / 60; // Время в минутах
            const symbolsPerMinute = Math.round(textToType.length / timeInMinutes); // Скорость
            const accuracy = ((correctCount / textToType.length) * 100).toFixed(2); // Точность в процентах

            // Отображаем результаты
            document.getElementById("errors-count").textContent = `Ошибки: ${errors}`;
            document.getElementById("time-taken").textContent = `Время: ${timeTaken} секунд`;
            document.getElementById("speed-count").textContent = `Скорость: ${symbolsPerMinute} зн/мин`;
            document.getElementById("accuracy").textContent = `Точность: ${accuracy}%`;

            resultsContainer.style.display = "block"; // Показываем блок с результатами

            // Отключаем ввод после завершения
            userInput.disabled = true;

            // Отправка результатов на сервер (AJAX)
            fetch('/users/update_test_results/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    'speed': symbolsPerMinute,
                    'accuracy': accuracy,
                    'time_taken': timeTaken
                })
            });            
        }
    });

    // Изначально выделяем первую букву
    highlightCurrentLetter(0);

    // Автозапуск фокуса на поле для ввода
    userInput.focus();

    function getCookie(name) {
        const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
        return cookieValue ? cookieValue.pop() : '';
    }
});
