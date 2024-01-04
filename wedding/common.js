// Function to initialize the cart object
document.addEventListener('DOMContentLoaded', function () {

function initializeCart() {
    // Check if cart already exists in localStorage
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // If not, create an empty cart
    if (!cart || !Array.isArray(cart)) {
        cart = [];
    }

    return cart;
}


// Function to update and save the cart in localStorage

// Example usage:
// Initialize the cart
let cart = initializeCart();

// Add an item to the cart

// Update and save the cart

// Retrieve the cart anytime during the session
let retrievedCart = initializeCart();


// Sample JavaScript to update the badge number
let badgeNumber = cart.map(e => e.quantity).reduce((partialSum, a) => partialSum + a, 0); // Replace this with your dynamic value
document.getElementById('cartBadge').innerText = badgeNumber;

// Show the badge if the number is greater than 0
if (badgeNumber > 0) {
    document.getElementById('cartBadge').style.display = 'block';
}
else {
    document.getElementById('cartBadge').style.display = 'none';
}
console.log(cart)

})

