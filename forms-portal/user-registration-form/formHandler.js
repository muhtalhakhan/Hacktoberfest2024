document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector('.user-registration-form');

    // Handle form submission
    form.addEventListener('submit', (e) => {
        e.preventDefault();

        // Collect form data
        const fullName = form.querySelector('input[placeholder="Full Name"]').value.trim();
        const phoneNumber = form.querySelector('input[placeholder="Phone Number"]').value.trim();
        const emailId = form.querySelector('input[placeholder="Email ID"]').value.trim();
        const comments = form.querySelector('textarea[placeholder="Comments"]').value.trim();

        // Client-side validation
        if (!fullName || !phoneNumber || !emailId || !comments) {
            alert('Please fill out all required fields.');
            return; // Stop the submission if validation fails
        }

        // Log the form data in the console
        const formData = {
            fullName,
            phoneNumber,
            emailId,
            comments,
        };
        console.log(formData); // Log collected data

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
