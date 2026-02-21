# QR Code Generator

Às vezes tudo que você precisa são 30 minutos livres e uma pequena frustração para nascer um projeto útil.

Esse gerador de QR Code surgiu exatamente assim. Depois de ficar na mão com QR Codes criados em sites duvidosos, decidi construir minha própria solução: simples, rápida e confiável.

O projeto foi desenvolvido com Python no backend, utilizando Flask para conectar a aplicação ao frontend construído com HTML e CSS. Para a geração do QR Code, foi utilizada a biblioteca `qrcode` do Python, junto com outras bibliotecas auxiliares para estruturar a lógica de geração e exibição da imagem.

A proposta é direta: transformar qualquer link em um QR Code funcional, de forma instantânea, sem depender de serviços externos.

---

## Tecnologias utilizadas

- Python  
- Flask  
- HTML  
- CSS  
- Biblioteca `qrcode`  

---

## 💡 Como funciona

O usuário insere um link na interface.  
O Flask recebe esse dado, gera o QR Code em memória utilizando a biblioteca `qrcode`, converte a imagem para Base64 e retorna para o frontend, onde ela é renderizada diretamente na página — sem necessidade de salvar arquivos no servidor.

O QR Code é exibido apenas após a geração e desaparece ao atualizar a página, garantindo que sempre apareça apenas o mais recente.

---

## Como executar o projeto

Clone o repositório ou baixe os arquivos para sua máquina.

Certifique-se de ter o Python instalado. É recomendado utilizar um ambiente virtual.

### Criando e ativando o ambiente virtual

**No Windows**

```bash
python -m venv venv
venv\Scripts\activate
```
---
### Instalando as dependências

```bash
pip install flask qrcode pillow
```
---
### Executando a aplicação

```bash
python app.py
```
---

##  Objetivo do projeto

Criar uma ferramenta simples, confiável e independente para geração de QR Codes, eliminando a necessidade de depender de serviços externos e garantindo que os códigos sempre funcionem quando você precisar.

Projeto simples, rápido de desenvolver e extremamente útil no dia a dia.
