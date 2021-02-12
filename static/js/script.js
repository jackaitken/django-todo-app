// function to mark list item as completed.
document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('#completed')
    checkboxes.forEach(checkbox => {
        checkbox.onclick = function() {
            console.log('click')
        }
    });
  });