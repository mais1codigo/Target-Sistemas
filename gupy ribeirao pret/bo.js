function pertenceFibonacci(numero) {
    function fibonacciSeq(limite) {
        let seq = [0, 1];
        while (seq[seq.length - 1] < limite) {
            seq.push(seq[seq.length - 1] + seq[seq.length - 2]);
        }
        return seq;
    }

    let fibonacci = fibonacciSeq(numero);

    if (fibonacci.includes(numero)) {
        return `O número ${numero} pertence à sequência de Fibonacci.`;
    } else {
        return `O número ${numero} NÃO pertence à sequência de Fibonacci.`;
    }
}

let numeroInformado = parseInt(prompt("Informe um número:"));
let resultado = pertenceFibonacci(numeroInformado);
alert(resultado);
