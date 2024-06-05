const presentBox = document.getElementById("upload-photo");
const dialog = document.getElementById("upload-photo-dialog");

    presentBox.addEventListener('click', () => {
        dialog.showModal();
    });

    // Handle form submission with JavaScript and Django
    const form = document.getElementById("upload-photo-form");
    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);

        try {
        const response = await fetch('/upload-photo/', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
          // Handle successful response
          // (e.g., display a success message)
            alert("Данные успешно отправлены!");
            dialog.close();
        } else {
          // Handle errors
            alert("Ошибка при отправке данных!");
            console.error("Error:", response.status, response.statusText);
        }
        } catch (error) {
        // Handle network errors
        console.error("Network Error:", error);
        }
    });