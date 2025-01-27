import torch, json
from transformers import pipeline, AutoTokenizer
from huggingface_hub import login as huglog


huglog(token = "")
file = open('./perguntas/perguntas_sem_resposta.json', 'r')
saida = open('respostas_modelo','w')

data = json.load(file)

model_id = "meta-llama/Llama-3.2-1B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
pipe = pipeline("text-generation", model=model_id, torch_dtype=torch.bfloat16, device_map="auto")


#print(data)

for quest in data["questions"]:

    resposta = pipe(quest['question'],  
                    max_length=100, 
                    min_length=50, 
                    do_sample=True, 
                    temperature=0.5,
                    top_k=50,
                    top_p=0.9)

    resposta_texto = resposta[0]["generated_text"]

    if resposta_texto.startswith(quest["question"]):
        resposta_texto = resposta_texto[len(quest["question"]):].strip()

    saida.write(f"Pergunta: {quest['question']}\n")
    saida.write(f"Resposta: {resposta_texto}\n\n")
