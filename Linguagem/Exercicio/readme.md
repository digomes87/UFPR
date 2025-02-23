# Aluno: Diego Gomes

# Projeto de Análise e Predição de Preços de Carros

Este projeto realiza uma análise exploratória, visualização de dados e modelagem preditiva para estimar o preço médio dos carros no Brasil com base na Tabela FIPE.

## Requisitos
Antes de rodar o projeto, certifique-se de ter instalado o Python 3. O projeto requer as seguintes dependências:

- pandas
- matplotlib
- seaborn
- scikit-learn
- xgboost
- libomp (necessário para macOS)

## Instalação

1. Clone este repositório:
   ```bash
   gh repo clone digomes87/UFPR
   cd UFPR/Linguagem/Exercicio
   ```

2. Crie um ambiente virtual (opcional, recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. No macOS, instale `libomp` caso necessário:
   ```bash
   brew install libomp
   ```

## Executando o Projeto
Para rodar a análise e treinamento do modelo, basta executar:
```bash
python main.py
```
Isso irá carregar os dados, gerar visualizações e treinar os modelos de Machine Learning.

## Saída do Projeto
iPara dúvidas ou sugestões, entddre em contato via email ou GitHub Issues.
![Descrição](resultado-terminal.png)

# No diretório irá encontrar:
- Gráficos salvos como arquivos `.png`.
- Avaliação dos modelos impressa no terminal.
- Melhor modelo selecionado com base em métricas como MAE, MSE e R².


