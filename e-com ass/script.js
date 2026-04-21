const checkoutForm = document.getElementById("checkoutForm");

if (checkoutForm) {
    checkoutForm.addEventListener("submit", function(event) {
        event.preventDefault(); 

        let name = document.getElementById("fullName").value;
        let email = document.getElementById("email").value;
        let phone = document.getElementById("phone").value;
        let pin = document.getElementById("pin").value;
        let terms = document.getElementById("terms").checked;

        if (name === "" || !/^[A-Za-z ]+$/.test(name)) {
            alert("Enter a valid name (letters and spaces only).");
            return false;
        }

        if (email === "" || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            alert("Enter a valid email address.");
            return false;
        }

        if (!/^[0-9]{10}$/.test(phone)) {
            alert("Enter a valid 10-digit phone number.");
            return false;
        }

        if (!/^[0-9]{6}$/.test(pin)) {
            alert("Enter a valid 6-digit PIN Code.");
            return false;
        }

        
        if (!terms) {
            alert("You must agree to the Terms & Conditions.");
            return false;
        }
        alert("Order Placed Successfully! Thank you for shopping with Ebay.");
        checkoutForm.reset(); 
        return true;
    });
}