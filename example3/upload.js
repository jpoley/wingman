// Assuming you have an HTML form with an input field of type "file" for image upload
const fileInput = document.querySelector('input[type="file"]');

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    const formData = new FormData();

    formData.append('image', file);

    // Send the image data to the server using AJAX
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        console.log(data);
    })
    .catch(error => {
        // Handle any errors
        console.error(error);
    });
});
