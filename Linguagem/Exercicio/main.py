import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import sys
import platform

# Verificar se tem o XGBoost instalado no pc
try:
    from xgboost import XGBRegressor
except ImportError:
    print("XGBoost não está instalado corretamente.")
    sistema = platform.system()
    instrucoes = {
        "Darwin": "Execute: brew install libomp",
        "Windows": "Execute: pip install xgboost",
        "Linux": "Execute: sudo apt install libomp-dev (Debian/Ubuntu) ou sudo dnf install libomp (Fedora)"
    }
    print(instrucoes.get(sistema, "Sistema não reconhecido, instale o XGBoost manualmente."))
    sys.exit(1)

class DataLoader:
    @staticmethod
    def carregar_dados(file_path):
        print("Carregando os dados...")
        return pd.read_csv(file_path)

class DataAnalysis:
    @staticmethod
    def executar(df):
        print("\nAnalisando os dados...")
        print("Valores faltantes:\n", df.isnull().sum())
        print("\nValores duplicados:", df.duplicated().sum())
        print("\nEstatísticas das variáveis numéricas:\n", df.describe())
        print("\nContagem de marcas:\n", df['brand'].value_counts())

class DataVisualization:
    @staticmethod
    def gerar_grafico(df, coluna, titulo, nome_arquivo):
        plt.figure(figsize=(12, 6))
        df[coluna].value_counts().plot(kind='bar')
        plt.title(titulo)
        plt.xticks(rotation=45)
        plt.savefig(nome_arquivo)
        plt.close()

    @staticmethod
    def executar(df):
        print("\nGerando gráficos...")
        DataVisualization.gerar_grafico(df, 'brand', "Distribuição da Quantidade de Carros por Marca", "grafico_marcas.png")
        DataVisualization.gerar_grafico(df, 'gear', "Distribuição da Quantidade de Carros por Tipo de Engrenagem", "grafico_gear.png")

        df['month_of_reference'] = pd.Categorical(df['month_of_reference'], 
            categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
        avg_price_by_month = df.groupby('month_of_reference')['avg_price_brl'].mean()
        
        plt.figure(figsize=(12, 6))
        avg_price_by_month.plot(marker='o', linestyle='-', color='blue')
        plt.title("Evolução da Média de Preço dos Carros")
        plt.savefig("grafico_preco_meses.png")
        plt.close()

class ModelTraining:
    @staticmethod
    def executar(df):
        print("\nTreinando modelos...")
        
        categorical_features = ['brand', 'model', 'fuel', 'gear', 'engine_size', 'month_of_reference']
        df_encoded = df.copy()
        for col in categorical_features:
            df_encoded[col] = LabelEncoder().fit_transform(df_encoded[col].astype(str))
        
        X = df_encoded.drop(columns=['avg_price_brl', 'fipe_code', 'authentication'])
        y = df_encoded['avg_price_brl'].fillna(df_encoded['avg_price_brl'].median())
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
        
        modelos = {
            "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
            "XGBoost": XGBRegressor(n_estimators=100, random_state=42)
        }
        
        resultados = {}
        for nome, modelo in modelos.items():
            modelo.fit(X_train.fillna(0), y_train)
            predicoes = modelo.predict(X_test.fillna(0))
            resultados[nome] = {
                "MAE": mean_absolute_error(y_test, predicoes),
                "MSE": mean_squared_error(y_test, predicoes),
                "R²": r2_score(y_test, predicoes)
            }
        
        print("\nResultados da Avaliação dos Modelos:")
        for nome, metricas in resultados.items():
            print(f"{nome} - MAE: {metricas['MAE']}, MSE: {metricas['MSE']}, R²: {metricas['R²']}")
        
        melhor_modelo = max(resultados, key=lambda k: resultados[k]['R²'])
        print(f"\nMelhor modelo: {melhor_modelo}")

if __name__ == "__main__":
    df = DataLoader.carregar_dados("precos_carros_brasil.csv")
    DataAnalysis.executar(df)
    DataVisualization.executar(df)
    ModelTraining.executar(df)


