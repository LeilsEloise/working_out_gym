/* ChatGPT Code */
let countrySelect = document.getElementById('id_default_country');

function setColor() {
    if (!countrySelect.value) {
        countrySelect.style.color = '#aab7c4';
    } else {
        countrySelect.style.color = '#000';
    }
}

setColor();
countrySelect.addEventListener('change', setColor);