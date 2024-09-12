<script>
    
document.addEventListener('DOMContentLoaded', function() {
    var schoolSelect = document.getElementById('id_school');
    var courseSelect = document.getElementById('id_course');

    schoolSelect.addEventListener('change', function() {
        var schoolId = schoolSelect.value;

        if (schoolId) {
            fetch('/admin/get_courses_by_school/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
                params: {
                    'school_id': schoolId
                }
            })
            .then(response => response.json())
            .then(data => {
                // Clear existing options
                courseSelect.innerHTML = '';

                // Add new options
                data.forEach(function(course) {
                    var option = document.createElement('option');
                    option.value = course.id;
                    option.textContent = course.name;
                    courseSelect.appendChild(option);
                });
            })
            .catch(error => {
                console.error('Error fetching courses:', error);
            });
        } else {
            // Clear options if no school selected
            courseSelect.innerHTML = '';
        }
    });
});

</script>