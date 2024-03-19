document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', document.querySelector('input[type=file]').files[0]);
    const response = await fetch('/', {
        method: 'POST',
        body: formData
    });
    const data = await response.text();
    document.getElementById('output').innerHTML = data;
});