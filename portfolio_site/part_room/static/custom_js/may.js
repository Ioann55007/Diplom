//const {form} = document.forms;
//
//function retrieveFormValue(event){
//    event.preventDefault();
//
//    const formData = new FormData(form)
//    const values = Object.fromEntries(formData.entries());
//
//    console.log(">>", values)
//
//}
//
//form.addEventListener('submit', retrieveFormValue);


 $(document).ready(function () {
          // отслеживаем событие отправки формы
          $('#contactForm').submit(function () {
              // создаем AJAX-вызов
              $.ajax({
                  data: $(this).serialize(), // получаем данные формы
                  type: $(this).attr('method'), // GET или POST
                  url: "{% url 'contact_form' %}",
                  // если успешно, то
                  success: function (response) {
                      alert("Спасибо, что обратились к нам " + response.name);
                  },
                  // если ошибка, то
                  error: function (response) {
                      // предупредим об ошибке
                      alert(response.responseJSON.errors);
                      console.log(response.responseJSON.errors)
                  }
              });
              return false;
          });
      })