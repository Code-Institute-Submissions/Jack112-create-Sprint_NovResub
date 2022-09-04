
/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

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
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');


// Handle validation errors on the card element

card.addEventListener('change', function(e) {
    var errorDiv = document.getElementById('card-errors');
    if (e.error) {
        var html = `
        <span class="card-error">
            <i class="fas fa-times"></i>
        </span>
        <span>${e.error.message}</span>
        `

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
    $('.spinner-container').fadeIn();
    $('.spinner-container').css('display', 'flex');
    $('.spinner-container').css('justify-content', 'center');
    $('.spinner-container').css('align-items', 'center');
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            $('.spinner-container').fadeOut();
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
        } else {
            $('.spinner-container').fadeOut();
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});

console.log(form)