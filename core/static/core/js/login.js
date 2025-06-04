// Registro ↓
document.getElementById('registroForm').addEventListener('submit', function(event) {
    event.preventDefault();
    try {
        var usuario = document.getElementById('Rut').value;
        var contrasena = document.getElementById('Password').value;
        var email = document.getElementById('Email').value;

        if(validarRut(usuario)){
            if (usuario !== '' && contrasena !== '' && email !== '') {
                window.location.href = 'diseno/';
            } else {
                throw new Error('Por favor, complete todos los campos (Usuario, Contraseña, Email) antes de continuar.');
            }
        }else{
            throw new Error('Por favor, ingresa un Rut válido en el formato XXXXXXXX-Y, donde X son dígitos del 1-9 e Y es un dígito 1-9 o la letra k minúscula.');
        }
    } catch (error) {
        alert(error.message);
    }
});

//Verificar forma del rut
function validarRut(rut) {
    var rutRegex = /^[0-9]{7,8}-[0-9kK]$/;

    if (!rutRegex.test(rut)) {
        return false;
    }

    // Separar todoooooo
    var partes = rut.split('-');
    var rutSinGuion = partes[0];
    var digitoVerificador = partes[1];

    var dvCalculado = calcularDigitoVerificador(rutSinGuion);
    return dvCalculado === digitoVerificador.toUpperCase();
}

function calcularDigitoVerificador(rutSinGuion) {
    var M = 0;
    var S = 1;

    for (; rutSinGuion; rutSinGuion = Math.floor(rutSinGuion / 10)) {
        S = (S + rutSinGuion % 10 * (9 - M++ % 6)) % 11;
    }

    return S ? String(S - 1) : 'K';
}

// Login ↓
document.getElementById('log').addEventListener('submit', function(event) {
    event.preventDefault();
    try {
        var usuarioL = document.getElementById('rutlog').value;
        var contrasenaL = document.getElementById('pswdlog').value;

        // Validar el formato del Rut antes de realizar otras validaciones
        if (validarRut(usuarioL)) {
            // Rut válido, puedes continuar con otras validaciones o redirigir
            if (usuarioL !== '' && contrasenaL !== '') {
                window.location.href = 'diseno/';
            } else {
                throw new Error('Por favor, complete todos los campos (Rut y Contraseña) antes de continuar.');
            }
        } else {
            // Rut no válido
            throw new Error('Por favor, ingresa un Rut válido en el formato XXXXXXXX-Y, donde X son dígitos del 1-9 e Y es un dígito 1-9 o la letra k minúscula.');
        }
    } catch (error) {
        alert(error.message);
    }
});

