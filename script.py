import torch, json
from transformers import pipeline

file = open('perguntas_sem_resposta.json', 'r')

data = json.loads(file)

model_id = "meta-llama/Llama-3.2-1B"

pipe = pipeline("text-generation", model=model_id, torch_dtype=torch.bfloat16, device_map="auto")

with open(output, "w", encoding="utf-8") as output:
    for i, item in enumerate(data["questions"], start=1):
        # Obtendo a pergunta
        question = item.get("question", "")

        # Gerando a resposta para a pergunta
        prompt = f"Responda a questão: {question}"
        generated = pipe(prompt, max_length=100, num_return_sequences=1)
        response = generated[0]["generated_text"].strip()

        # Escrevendo os dados no arquivo de saída
        output.write(f"Item {i}:\n")
        output.write(f"Pergunta: {question}\n")
        output.write(f"Resposta: {response}\n")
        output.write("-" * 50 + "\n")
        
        # Opcional: também imprimir no console
        print(f"Processado Item {i}")
    
