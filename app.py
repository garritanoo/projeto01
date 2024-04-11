import pandas as pd
import numpy as np
import gradio as gr
import pickle

import utils as ut

# Coletando os dados
original_url = 'https://drive.google.com/file/d/1n3Zt2V4M4O6C1ASBUuZlVZdpKLZOEpSi/view?usp=sharing'
file_id = original_url.split('/')[-2]
download_url = 'https://drive.google.com/uc?id=' + file_id 
df_completo = pd.read_pickle(download_url)

# carregando o dataset limpo para o treinamento do algoritmo
df_treinamento = ut.limpa_dados(df_completo)

modelo_treinado = ut.modelo_machine_learning(df_treinamento)

def predict(*args):

    X = np.array([args]).reshape(1,-1)
    y_pred = modelo_treinado.predict_proba(X)

    return {"Aurora": y_pred[0][0], "Nova": y_pred[0][1], "Start": y_pred[0][2]}

with gr.Blocks() as demo:

    # Titulo do painel
    gr.Markdown( """# Propensão de Compra""")

    with gr.Row():
        # Coluna 1
        with gr.Column():
            gr.Markdown(""" # Atributos do Cliente """)
            year 		            = gr.Slider(label="year", minimum=2017, maximum=2018,step=1, randomize=True)
            month                   = gr.Slider(label="month", minimum=1, maximum=12,step=1, randomize=True)
            flights_booked          = gr.Slider(label="flights_booked",minimum=0, maximum=21, step=1, randomize=True)
            flights_with_companions = gr.Slider(label="flights_with_companions", minimum=0,maximum=11, step=1, randomize=True)
            total_flights           = gr.Slider(label="total_flights", minimum=0, maximum=32,step=1, randomize=True)
            distance                = gr.Slider(label="distance", minimum=0, maximum=6293, step=1, randomize=True)
            points_accumulated      = gr.Slider(label="points_accumulated", minimum=0.00, maximum=676.50, step=0.1, randomize=True)
            salary                  = gr.Slider(label="salary", minimum=58486.00, maximum=407228.00, step=0.1, randomize=True)
            clv                     = gr.Slider(label="clv", minimum=2119.89, maximum=83325.38, step=0.1, randomize=True)

            with gr.Row():
                predict_btn = gr.Button(value="Previsão")

        # Coluna 2
        with gr.Column():
            gr.Markdown("""# Propensão de Compra do Cliente""")
            label = gr.Label()

        # Botao de Predict
        predict_btn.click(
                fn=predict,
                inputs=[
                year,
                month,
                flights_booked,
                flights_with_companions,
                total_flights,
                distance,
                points_accumulated,
                salary,
                clv
                ],
                outputs=[label] )

demo.launch(debug=True, share=False)