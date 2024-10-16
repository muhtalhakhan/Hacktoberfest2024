// formHandler.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector('.user-registration-form');

    // Add an event listener to handle form submission
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevents the form from submitting and refreshing the page

        // Get the values from the form fields
        const fullName = form.querySelector('input[placeholder="Full Name"]').value;
        const phoneNumber = form.querySelector('input[placeholder="Phone Number"]').value;
        const emailID = form.querySelector('input[placeholder="Email ID"]').value;
        const comments = form.querySelector('textarea[placeholder="Comments"]').value;

        // Log the data to the console
        console.log(`Full Name: ${fullName}`);
        console.log(`Phone Number: ${phoneNumber}`);
        console.log(`Email ID: ${emailID}`);
        console.log(`Comments: ${comments}`);

        // Optionally, you can show a confirmation message or reset the form
        alert('Form submitted successfully!');
        form.reset(); // Reset the form fields after submission
    });
});
