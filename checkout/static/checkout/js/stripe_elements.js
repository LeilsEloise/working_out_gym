/* ChatGPT Code */
$(document).ready(function() {
    $('#loading-overlay').hide();
});

/* Code Institute Code */
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"PT Serif", serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle Realtime Validation Errors on Card Element */
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';        
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').hide(); // ChatGPT Code
    $('#loading-overlay').fadeIn(200); //ChatGPT Code

    var saveInfo = $('#id-save-info').is(':checked');// ChatGPT Code
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';
// ChatGPT Code
$.post(url, postData).done(function () {
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            }
        },
        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },
    }).then(function(result) {

        if (result.error) {
            $('#card-errors').text(result.error.message);
            $('#loading-overlay').fadeOut(200);
            $('#payment-form').show();
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);

        } else {
            // ✅ THIS IS WHAT YOU WERE MISSING
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }

    });

}).fail(function () {
    location.reload();
});

});