var form_1 = document.querySelector(".form_1");
var form_2 = document.querySelector(".form_2");
var form_3 = document.querySelector(".form_3");

var form_1_btns = document.querySelector(".form_1_btns");
var form_2_btns = document.querySelector(".form_2_btns");
var form_3_btns = document.querySelector(".form_3_btns");

var form_1_next_btn = document.querySelector(".form_1_btns .btn_next");
var form_2_back_btn = document.querySelector(".form_2_btns .btn_back");
var form_2_next_btn = document.querySelector(".form_2_btns .btn_next");
var form_3_back_btn = document.querySelector(".form_3_btns .btn_back");

var form_2_progessbar = document.querySelector(".form_2_progessbar");
var form_3_progessbar = document.querySelector(".form_3_progessbar");

var btn_done = document.querySelector(".btn_done");
var modal_wrapper = document.querySelector(".modal_wrapper");
var shadow = document.querySelector(".shadow");

form_1_next_btn.addEventListener("click", function () {
	form_1.style.display = "none";
	form_2.style.display = "block";

	form_1_btns.style.display = "none";
	form_2_btns.style.display = "flex";

	form_2_progessbar.classList.add("active");
});

form_2_back_btn.addEventListener("click", function () {
	form_1.style.display = "block";
	form_2.style.display = "none";

	form_1_btns.style.display = "flex";
	form_2_btns.style.display = "none";

	form_2_progessbar.classList.remove("active");
});

form_2_next_btn.addEventListener("click", function () {
	form_2.style.display = "none";
	form_3.style.display = "block";

	form_3_btns.style.display = "flex";
	form_2_btns.style.display = "none";

	form_3_progessbar.classList.add("active");
});

form_3_back_btn.addEventListener("click", function () {
	form_2.style.display = "block";
	form_3.style.display = "none";

	form_3_btns.style.display = "none";
	form_2_btns.style.display = "flex";

	form_3_progessbar.classList.remove("active");
});

btn_done.addEventListener("click", function () {
	modal_wrapper.classList.add("active");
})

shadow.addEventListener("click", function () {
	modal_wrapper.classList.remove("active");
})


document.addEventListener('DOMContentLoaded', function () {
	// Mostrar mensajes flash con SweetAlert2
	const flashMessage = document.getElementById('flash-message');
	if (flashMessage) {
		const category = flashMessage.getAttribute('data-category');
		const message = flashMessage.getAttribute('data-message');

		let icon = 'info';
		if (category === 'success') icon = 'success';
		if (category === 'error') icon = 'error';
		if (category === 'warning') icon = 'warning';

		Swal.fire({
			title: message,
			icon: icon,
			toast: true,
			position: 'top-end',
			showConfirmButton: false,
			timer: 3000,
			timerProgressBar: true
		});
	}

	// Botón de prueba para SweetAlert
	const testAlertBtn = document.getElementById('test-alert');
	if (testAlertBtn) {
		testAlertBtn.addEventListener('click', function () {
			Swal.fire({
				title: '¡Funciona!',
				text: 'SweetAlert2 está correctamente configurado.',
				icon: 'success',
				confirmButtonText: 'Genial'
			});
		});
	}
});
