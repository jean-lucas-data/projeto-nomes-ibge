# Web App – Nomes no Brasil (IBGE)

Este projeto consiste em um web app desenvolvido em Python que consome a API pública do IBGE para exibir a frequência de nomes no Brasil ao longo das décadas.

## Fonte dos dados
- API de nomes do IBGE: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2

## Tecnologias utilizadas
- Python
- Requests
- Pandas
- Streamlit
- Poetry

## Funcionalidades
- Consulta de nomes na base do IBGE
- Visualização da frequência por década
- Exibição dos dados em tabela e gráfico
- Tratamento de erros para nomes inexistentes

## Como executar o projeto

### Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/projeto-nomes-ibge.git
cd projeto-nomes-ibge
```

### Instale as dependências
```bash
poetry install
```

### Ative o ambiente virtual
```bash
poetry shell
```

### Execute o aplicativo
```bash
streamlit run app.py
```

## Observações

A API do IBGE pode não retornar dados para nomes compostos.

O projeto possui finalidade educacional, com foco em consumo de API e visualização de dados.

