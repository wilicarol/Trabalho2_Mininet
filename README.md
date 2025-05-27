# Trabalho Final - Mininet

Este repositório contém a solução para o trabalho final da disciplina de C115 utilizando Mininet. O projeto é dividido em duas partes principais: uma topologia em árvore criada via linha de comando e uma topologia customizada desenvolvida em Python que está disponível no arquivo `tree.py`.

---

## Tecnologias e Ferramentas

- Mininet VM
- PuTTY
- Xming
- Python 3 instalado

---

## Questão 1: Topologia em Árvore
Objetivo: Criar uma topologia em árvore com profundidade 4 e ramificação 3, utilizando linha de comando.

a) Criar topologia:  `sudo mn --topo tree,depth=4,fanout=3 --mac --link tc,bw=35`
![alt text](/images/image.png)
![alt text](/images/image-1.png)



b) Inspeção de interfaces: 
- `nodes`: lista de hosts e switches 

![alt text](/images/image-2.png)

- `dump`: Estados dos nós

![alt text](/images/image-3.png)

- `h1 ifconfig`: para ver IP e MAC

![alt text](/images/image-4.png)

c) ![alt text](</images/diagrama mininet.png>)


d) ![alt text](/images/image-5.png)

e) Teste com 5:

![alt text](/images/image-6.png)

Inspecionando h1: ![alt text](/images/image-7.png)

Inspecionando h2: ![alt text](/images/image-8.png)

Especificando porta h1: ![alt text](/images/image-9.png)

Declarando h1 como servidor e h2 como cliente + emitindo relatório: ![alt text](/images/image-10.png)

Teste com 10:
![alt text](/images/image29.png)


Declarando h1 como servidor e h2 como cliente + emitindo relatório:
![alt text](/images/image30.png)


Teste com 25:

![alt text](/images/image32.png)


Declarando h1 como servidor e h2 como cliente + emitindo relatório:
![alt text](/images/image31.png)

Teste com 35:

![alt text](/images/image.png)

Declarando h1 como servidor e h2 como cliente + emitindo relatório:
![alt text](/images/image-1.png)


## Questão 2: 

 a) Verificando a importação do arquivo `tree.py`: ![alt text](/images/image-16.png)


b) Lista todos os hosts e switches

![alt text](/images/image-13.png)


Inspecionando h1

![alt text](/images/image-14.png)

Inspecionando portas de switches

![alt text](/images/image-15.png)


c) Diagrama

![alt text](/images/image23.png)

d) Teste de ping fail

![alt text](/images/image-17.png)

e) Apagando regras anteriores no s2

![alt text](/images/image-18.png)

f) Validando regras via ping


h2 → h5 - FUNCIONA
![alt text](/images/image-19.png)


h2 → h1 - FALHA
![alt text](/images/image-20.png)

Apenas o h2 e h5 conseguem se comunicar através de s2, o restante deve estar bloqueado.
![alt text](/images/image-21.png)






