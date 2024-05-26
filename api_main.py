from bs4 import BeautifulSoup
import os
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def html_to_txt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'lxml')
    
    text = soup.get_text()
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

    with open('index.txt', 'r', encoding='utf-8') as file:
        input_text = file.read()

    return input_text



def llamamodel():
    input_text = html_to_txt(input_file='index.html', output_file='index.txt')

    llm = CTransformers(model="llama-2-7b-chat.ggmlv3.q8_0.bin",model_type="llama",
                config={'max_new_tokens':4096,'temperature':0.01,'context_length' : 4096})

    template = """
        Extract meaningful attributes from an HTML block (stored in input_text variable as .txt) of an e-commerce website. return the relevant and meaningful information from the page in JSON format.
        
        Input HTML:
        {input_text}
        
        Extracted Attributes (in JSON format):

    """
    prompt = PromptTemplate(input_variables=["input_text"], template=template)
    response=llm(prompt.format(input_text=input_text))
    return response


@app.route('/assesment', methods=['POST','GET'])
def assesment():
    response_main = llamamodel()

    return jsonify({'data': response_main})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)