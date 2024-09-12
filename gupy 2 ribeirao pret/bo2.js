function verificaLetraA(texto) {
    let textoMinusculo = texto.toLowerCase();
    let contador = 0;

    for (let i = 0; i < textoMinusculo.length; i++) {
        if (textoMinusculo[i] === 'a') {
            contador++;
        }
    }

    if (contador > 0) {
        return `A letra 'a' aparece ${contador} vezes na string.`;
    } else {
        return "A letra 'a' não foi encontrada na string.";
    }
}
let textoInformado = prompt("Informe uma string:");
let resultado = verificaLetraA(textoInformado);
alert(resultado);
