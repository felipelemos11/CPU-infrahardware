Aqui vai um README organizado, bonito e com uma cara mais profissional, mas ainda bem humano como tu costuma pedir:

---

# 🕹️ CPU-infrahardware

Simulação de uma CPU simples em Python, desenvolvida para demonstrar, na prática, como funciona a execução de instruções dentro de um processador.

---

## 💡 Sobre o projeto

O projeto implementa uma CPU chamada **MiniCPU**, com o objetivo de facilitar o entendimento dos conceitos básicos de arquitetura de computadores.

A CPU possui:

* Memória com 256 posições
* 4 registradores de uso geral
* Contador de programa (**PC**)
* Flag de comparação (**ZF**)

A execução acontece em ciclos, simulando o funcionamento real de um processador.

---

## ⚙️ Como funciona

A cada ciclo, a CPU executa três etapas principais:

1. **Fetch (Busca)**
   A instrução é buscada na memória com base no valor do PC

2. **Execute (Execução)**
   A instrução é interpretada e executada

3. **Trace (Exibição)**
   O estado atual da CPU é mostrado (registradores, PC, etc.)

Esse processo continua até encontrar a instrução **HALT**, que encerra a execução.

---

## 🧠 Instruções suportadas

A MiniCPU suporta operações básicas, como:

* Carregar valores da memória
* Armazenar valores
* Operações aritméticas (soma e subtração)
* Movimentação de dados
* Comparações entre registradores
* Desvios condicionais e incondicionais

---

## 📦 Organização do programa

O programa é montado diretamente na memória, incluindo:

* Instruções
* Dados de entrada (lista de valores)
* Um valor de referência (**limiar**)

---

## 📊 Funcionalidade implementada

Após a execução da CPU, o programa realiza uma verificação:

* Percorre os valores armazenados na memória
* Conta quantos são maiores que o limiar definido
* Armazena e exibe o resultado final

---

## ▶️ Como executar

1. Certifique-se de ter o Python instalado
2. Salve o arquivo como `cpu.py`
3. Abra o terminal na pasta do projeto

Execute com:

```bash
python cpu.py
```

Caso não funcione:

```bash
py cpu.py
```

---

## 🖥️ Saída do programa

Durante a execução, serão exibidos:

* Ciclos da CPU
* Estado dos registradores
* Valor do PC e da ZF

Ao final:

* Limiar utilizado
* Lista de valores
* Resultado da contagem

---

## 👥 Equipe 9 (Grupo 6) — Contagem Condicional

* Danilo Santos — [dsc4@cesar.school](mailto:dsc4@cesar.school)
* Diego Gomes — [dgsx@cesar.school](mailto:dgsx@cesar.school)
* Felipe Lemos — [fal@cesar.school](mailto:fal@cesar.school)
* Felipe Menezes — [fem@cesar.school](mailto:fem@cesar.school)
* Gustavo Soares — [grsf@cesar.school](mailto:grsf@cesar.school)
* João Falcão — [jffn@cesar.school](mailto:jffn@cesar.school)
* Natan Luis — [nlps@cesar.school](mailto:nlps@cesar.school)


Se quiser, eu deixo ele ainda mais “nível GitHub top” (com badges, gifzinho de execução, ou até print da saída simulada), fica bem chamativo pra professor 👍
