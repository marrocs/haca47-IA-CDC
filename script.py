import torch, json
from transformers import pipeline

file = open('perguntas_sem_resposta.json', 'r')

data = json.loads(file)

model_id = "meta-llama/Llama-3.2-1B"

pipe = pipeline("text-generation", model=model_id, torch_dtype=torch.bfloat16, device_map="auto")

#for 

print(data)

#pipe(f"Responda a questão: {questao}")