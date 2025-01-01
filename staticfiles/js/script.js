document.addEventListener("DOMContentLoaded", () => {
    const textToType = document.getElementById("text-to-type").textContent.trim();
    const container = document.getElementById("text-to-type");
    const userInput = document.getElementById("user-input");
    const resultsContainer = document.getElementById("results");

    container.innerHTML = '';
    for (let i = 0; i < textToType.length; i++) {
        const span = document.createElement('span');
        span.textContent = textToType[i];
        container.appendChild(span);
    }

    let startTime = null;
    let errors = 0;

    const highlightCurrentLetter = (index) => {
        for (let i = 0; i < container.children.length; i++) {
            const span = container.children[i];
            if (i === index) {
                span.classList.add("highlight"); 
            } else {
                span.classList.remove("highlight");
            }
        }
    };

    userInput.addEventListener("input", () => {
        if (!startTime) startTime = new Date(); 

        const typedText = userInput.value;
        const currentLength = typedText.length;

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

            if (typedText[i] === " " && textToType[i] !== " ") {
                span.classList.add("wrong");
                span.classList.remove("correct", "highlight");
                errors++;
            }
        }

        if (currentLength < textToType.length) {
            highlightCurrentLetter(currentLength);
        }

        if (currentLength === textToType.length) {
            const endTime = new Date();
            const timeTaken = ((endTime - startTime) / 1000).toFixed(2); 
            const timeInMinutes = timeTaken / 60; 
            const symbolsPerMinute = Math.round(textToType.length / timeInMinutes); 
            const accuracy = ((correctCount / textToType.length) * 100).toFixed(2);

            document.getElementById("errors-count").textContent = `Ошибки: ${errors}`;
            document.getElementById("time-taken").textContent = `Время: ${timeTaken} секунд`;
            document.getElementById("speed-count").textContent = `Скорость: ${symbolsPerMinute} зн/мин`;
            document.getElementById("accuracy").textContent = `Точность: ${accuracy}%`;

            resultsContainer.style.display = "block"; 

            userInput.disabled = true;

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

    highlightCurrentLetter(0);

    userInput.focus();

    function getCookie(name) {
        const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
        return cookieValue ? cookieValue.pop() : '';
    }
});
