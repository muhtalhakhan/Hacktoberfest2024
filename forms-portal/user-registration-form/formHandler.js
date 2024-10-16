// formHandler.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector('.user-registration-form');

    // Add an event listener to handle form submission
    form.addEventListener('submit', function (event) {
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

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.user-registration-form');

    // Handle form submission
    form.addEventListener('submit', (e) => {
        e.preventDefault();

        // Collect form data
        const formData = {
            fullName: form.querySelector('input[placeholder="Full Name"]').value,
            phoneNumber: form.querySelector('input[placeholder="Phone Number"]').value,
            emailId: form.querySelector('input[placeholder="Email ID"]').value,
            comments: form.querySelector('textarea[placeholder="Comments"]').value,
        };

        console.log(formData); // Log the form data in the console

        // Export options
        const exportType = prompt("Type 'CSV' for CSV export or 'EXCEL' for Excel export:");

        if (exportType.toLowerCase() === 'csv') {
            exportToCSV(formData);
        } else if (exportType.toLowerCase() === 'excel') {
            exportToExcel(formData);
        } else {
            alert("Invalid option selected.");
        }

        // Reset form
        form.reset();
    });

    // Function to export data to CSV
    function exportToCSV(data) {
        const csvContent = `Full Name,Phone Number,Email ID,Comments\n${data.fullName},${data.phoneNumber},${data.emailId},${data.comments}`;
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement('a');
        const url = URL.createObjectURL(blob);
        link.setAttribute('href', url);
        link.setAttribute('download', 'form_data.csv');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }

    // Function to export data to Excel
    function exportToExcel(data) {
        const workbook = XLSX.utils.book_new();
        const worksheetData = [['Full Name', 'Phone Number', 'Email ID', 'Comments'],
        [data.fullName, data.phoneNumber, data.emailId, data.comments]];

        const worksheet = XLSX.utils.aoa_to_sheet(worksheetData);
        XLSX.utils.book_append_sheet(workbook, worksheet, 'Form Responses');

        XLSX.writeFile(workbook, 'form_data.xlsx');
    }
});
