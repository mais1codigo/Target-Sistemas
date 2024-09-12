INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print("Valor final de SOMA:", SOMA)

# a) 1, 3, 5, 7,
a = [1, 3, 5, 7]
a.append(a[-1] + 2)
print("a) Próximo elemento:", a[-1])

# b) 2, 4, 8, 16, 32, 64,
b = [2, 4, 8, 16, 32, 64]
b.append(b[-1] * 2) 
print("b) Próximo elemento:", b[-1])

# c) 0, 1, 4, 9, 16, 25, 36,
c = [0, 1, 4, 9, 16, 25, 36]
c.append((len(c))**2) 
print("c) Próximo elemento:", c[-1])

# d) 4, 16, 36, 64,
d = [4, 16, 36, 64]
d.append((len(d) * 2)**2)  
print("d) Próximo elemento:", d[-1])

# e) 1, 1, 2, 3, 5, 8,
e = [1, 1, 2, 3, 5, 8]
e.append(e[-1] + e[-2]) 
print("e) Próximo elemento:", e[-1])

# f) 2, 10, 12, 16, 17, 18, 19,
f = [2, 10, 12, 16, 17, 18, 19]
f.append(f[-1] + 1) 
print("f) Próximo elemento:", f[-1])
