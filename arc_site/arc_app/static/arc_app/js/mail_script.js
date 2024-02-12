// Add this JavaScript code to your script.js file or in a script block at the end of your HTML body

document.addEventListener('DOMContentLoaded', function() {
    var quickContact = document.getElementById('kleo-quick-contact');
    var quickContactLink = document.querySelector('.kleo-quick-contact-link');
    
    // Toggle the quick contact form visibility
    quickContactLink.addEventListener('click', function(e) {
        e.preventDefault();
        toggleQuickContact();
    });

    // Close the quick contact form when clicking outside of it
    document.addEventListener('click', function(e) {
        if (!quickContact.contains(e.target) && !quickContactLink.contains(e.target)) {
            quickContact.style.display = 'none';
        }
    });
});

function toggleQuickContact() {
    var quickContact = document.getElementById('kleo-quick-contact');
    quickContact.style.display = (quickContact.style.display === 'block') ? 'none' : 'block';
}
