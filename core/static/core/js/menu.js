const fileInput = document.getElementById('imagen');
const uploadedImage = document.getElementById('uploaded-image');
const generateButton = document.getElementById('generate-button');
const codigoInput = document.getElementById('codigo');
const cursoSelect = document.getElementById('curso');
const alumnoSelect = document.getElementById('alumno');
const beneficioInput = document.getElementById('beneficio');
const motivoTextarea = document.getElementById('motivo');

// Función para mostrar la imagen seleccionada
fileInput.addEventListener('change', function () {
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            uploadedImage.src = e.target.result;
        };

        reader.readAsDataURL(file);
    }
});

// Función para generar el código único en el patrón XXX - XXX - XXX
generateButton.addEventListener('click', () => {
    const randomNumber = generateRandomNumber();
    document.getElementById('hint-text').textContent = randomNumber;
    // Actualiza tanto el hint-text como el valor del campo de entrada
    codigoInput.value = randomNumber.replace(/-/g, '');
});
// Función para generar números aleatorios irrepetibles
function generateRandomNumber() {
    let numbers = Array.from({ length: 9 }, (_, i) => i + 1);
    let randomNumbers = [];

    for (let i = 0; i < 9; i++) {
        const randomIndex = Math.floor(Math.random() * numbers.length);
        const digit = numbers.splice(randomIndex, 1)[0];
        randomNumbers.push(digit);

    }
    console.log('Numeros creados:', randomNumbers);

    return `${randomNumbers.slice(0, 3).join('')} - ${randomNumbers.slice(3, 6).join('')} - ${randomNumbers.slice(6).join('')}`;

}


// Función para seleccionar el beneficio
function seleccionarBeneficio(button, beneficioId) {
    // Lógica para resaltar el beneficio seleccionado si es necesario
    const beneficioCard = button.closest('.card');
    beneficioCard.classList.toggle('seleccionado');

    // Actualiza el campo oculto con el ID del beneficio seleccionado
    document.getElementById('beneficio').value = beneficioCard.classList.contains('seleccionado') ? beneficioId : '';

    // Agrega un console.log para verificar si la función se está ejecutando
    console.log('Beneficio seleccionado:', beneficioId);
}
function mostrarMensajeTotem() {
    alert('Su tótem ha sido guardado exitosamente');
}

// Document ready
document.addEventListener('DOMContentLoaded', function () {
    // Ocultar el campo de código al cargar la página
    document.getElementById('codigo').hidden = true;
    const form = document.querySelector('form');
    form.addEventListener('submit', submitFormulario);
});
function submitFormulario(event) {
    event.preventDefault(); // Evitar la presentación por defecto del formulario
    // Log para verificar si la función se está ejecutando
    console.log('Submit del formulario iniciado');
    // Validar que se haya seleccionado al menos un beneficio
    if (!beneficioInput.value) {
        alert('Por favor, selecciona al menos un beneficio.');
        return;
    }

    // Obtener los valores seleccionados del curso y del alumno
    const selectedCurso = cursoSelect.value;
    const selectedAlumno = alumnoSelect.value;

    // Validar que se hayan seleccionado curso y alumno
    if (selectedCurso === '.....' || selectedAlumno === '.....') {
        alert('Por favor, selecciona curso y alumno.');
        return;
    }

    // Actualizar los campos ocultos con los valores seleccionados
    document.getElementsByName('curso')[0].value = selectedCurso;
    document.getElementsByName('alumno')[0].value = selectedAlumno;


    mostrarMensajeTotem();
}


