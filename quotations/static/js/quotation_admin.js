// document.addEventListener('DOMContentLoaded', function() {
//   const courseQtyWeeksField = document.querySelector('select[name="course_qty_weeks"]');
  
//   if (courseQtyWeeksField) {
//       courseQtyWeeksField.addEventListener('change', function() {
//           const form = courseQtyWeeksField.closest('form');
          
//           if (form) {
//               const formData = new FormData(form);

//               fetch(form.action, {
//                   method: 'POST',
//                   body: formData,
//                   headers: {
//                       'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
//                   }
//               })
//               .then(response => response.text())
//               .then(() => {
//                   // Reload the page
//                   window.location.reload();
//               })
//               .catch(error => {
//                   console.error('Error:', error);
//               });
//           }
//       });
//   }
// });


