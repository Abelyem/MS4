var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#b71c1c',
        iconColor: '#b71c1c'
    }
};
var card = elements.create('card', { style: style });
card.mount('#card-payment');

// Card error message

card.addEventListener('change', function (event) {
    var paymentError = document.getElementById('payment-error');
    if (event.error) {
        var html = `
            <span class="payment-error-message">
            <i class="fas fa-exclamation-circle"></i>
            ${event.error.message}</span>
        `;
        $(paymentError).html(html);
    } else {
        paymentError.textContent = '';
    }
});

// Form submission

var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            var paymentError = document.getElementById('payment-error');
            var html = `
                <span><i class="fas fa-exclamation-circle"></i>
                ${result.error.message}</span>`;
            $(paymentError).html(html);
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
