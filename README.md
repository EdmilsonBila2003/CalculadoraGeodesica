# Calculadora Geodésica

Interface inicial de uma calculadora geodésica web, construída com Python e Streamlit.

## Requisitos
- Python 3.10 ou superior recomendado
- pip

## Instalação
Abra o terminal do VS Code na pasta do projecto e execute:

```bash
pip install -r requirements.txt
```

## Executar
```bash
streamlit run app.py
```

A aplicação deverá abrir no navegador, normalmente em http://localhost:8501.

## Estado actual
- Conversão graus/radianos: funcional.
- Cálculo convencional do fuso UTM: funcional.
- Conversões UTM/geográficas: interface criada; cálculo ainda por implementar.
- Problemas directo e inverso de Puissant e Sodano: interfaces criadas; fórmulas ainda por implementar.

As fórmulas geodésicas serão adicionadas após serem fornecidas e confirmados os parâmetros de referência.
