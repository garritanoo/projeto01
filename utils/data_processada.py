from sklearn.tree import DecisionTreeClassifier
import pickle
import numpy as np

def limpa_dados(df):
    df = df.copy()

    # Selecionar somente as colunas que contem erros
    colunas = ['year', 'month', 'flights_booked', 'flights_with_companions', 'total_flights',
                        'distance', 'points_accumulated', 'salary', 'clv', 'loyalty_card']

    df_colunas_numericas = df.loc[:, colunas]

    # Remover linhas que contem dados faltante
    df_limpo = df_colunas_numericas.dropna()
    
    return df_limpo

def modelo_machine_learning(df):
    X_train = df.drop(columns='loyalty_card')
    y_train = df.loc[:, 'loyalty_card']

    # Definição do algortimo
    modelo = DecisionTreeClassifier(max_depth=5)

    # Treinamento do algoritmo
    modelo_treinado = modelo.fit(X_train, y_train)
    
    return modelo_treinado

def predict(*args):
    
    modelo_treinado = pickle.load(open('/datasets/modelo/modelo_treinando.pkl', 'rb'))
    
    X = np.array([args]).reshape(1,-1)
    y_pred = modelo_treinado.predict_proba(X)

    return {"Aurora": y_pred[0][0], "Nova": y_pred[0][1], "Start": y_pred[0][2]}