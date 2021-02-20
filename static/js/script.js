// function to mark list item as completed.
document.addEventListener('DOMContentLoaded', function() {
    let checkboxes = document.querySelectorAll('#completed')
    checkboxes.forEach(checkbox => {
        checkbox.onclick = function() {
            const pk = checkbox.dataset.id
            fetch(`/${pk}/item`, {
                method: 'PUT',
                body: JSON.stringify({
                    completed: (completed ? false : true)
                })
            })
        }
    });
});
