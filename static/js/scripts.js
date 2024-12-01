// Открытие модального окна
document.getElementById("registerBtn").onclick = function() {
    document.getElementById("registerModal").style.display = "block";
}

// Закрытие модального окна
document.getElementById("closeModal").onclick = function() {
    document.getElementById("registerModal").style.display = "none";
}

// Закрытие окна, если пользователь кликает за его пределами
window.onclick = function(event) {
    if (event.target === document.getElementById("registerModal")) {
        document.getElementById("registerModal").style.display = "none";
    }
}

document.getElementById("registerForm").addEventListener("submit", function(e) {
    e.preventDefault(); // Отменить обычную отправку формы

    const formData = new FormData(this);

    fetch("{% url 'users:register' %}", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Закрыть модальное окно и показать сообщение об успехе
            document.getElementById("registerModal").style.display = "none";
            alert("Регистрация успешна!");
        } else {
            // Обработать ошибки формы, если они есть
            alert("Пожалуйста, исправьте ошибки в форме.");
        }
    })
    .catch(error => console.error('Ошибка:', error));
});
