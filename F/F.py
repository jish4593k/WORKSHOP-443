import os
import concurrent.futures
from flask import Flask, send_file, request, jsonify
from flask_cors import CORS
from pdfminer.high_level import extract_text
import seaborn as sns
import torch



def health_check():
    return f"Processes: {os.cpu_count()}", 200

def extract_text_async(caminho_arquivo_entrada):
    texto_extraido = extract_text(camin_entrada)
    with open('./a 'w') as a_saida:
        arquivo_saida.write(texto_extraido)


def extract():
    try:
        file = request.files['entrada.PDF']
        caminho_arquivo_entrada = f'./upame}'
        file.save(caminho_arquivo_entrada)
        
        with concurrent.futures.ProcessPoolExecutor() as executor:
            future = executor.submit(extract_text_async, caminho_arquivo_entrada)
            concurrent.futures.wait([future], timeout=None, return_when=concurrent.futures.ALL_COMPLETED)

        return send_file('./t', download_name="marcacoes.txt")
    except Exception as e:
        return str(e)


def generate_torch_tensor():
    torch_tensor = torch.randn(100)
    return jsonify({'torch_tensor': torch_tensor.tolist()})


def display_seaborn_plot():
    # Dummy Seaborn plot (replace with your specific use case)
    sns.lineplot(x=range(10), y=range(10))
    plt.savefig('./seaborn_plot.png')
    return send_file('./seaborn_plot.png', download_name="seaborn_plot.png")

if __name__ == "__main__":
    os.makedirs('./uploads', exist_ok=True)
    app.run(debug=True)
