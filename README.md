The developed API successfully extracted meaningful attributes from the HTML blocks and returned the information in JSON format. However, due to the constraints of using a low-end PC, the API throws an error when processing large HTML files like index.html due to the exceeding number of tokens. This issue can be addressed by preprocessing the HTML file using NLP libraries to tokenize and feed the model in chunks.

## Sample Output

The sample folder contains a small part of the index.html and its corresponding output. Due to the limitations of my low-end PC, it was not possible to process the entire index.html file within the expected time. The sample folder demonstrates the extraction process and the format of the output.

                                                              `sample.ipynb`

<img width="610" alt="11" src="https://github.com/AryanKapri88/LLM-ecommerce-parser/assets/110614822/e717a03b-7ec8-4584-aefb-07a9a7c1ae84">

                                                              `api_main.py`

<img width="593" alt="Capture" src="https://github.com/AryanKapri88/LLM-ecommerce-parser/assets/110614822/f5c348f4-f57a-48b4-9a08-a21d66d5d28b">


`Note:` The Llama 2 model was run locally on my machine, allowing for efficient processing despite hardware constraints. The model can be accessed from [Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML).
