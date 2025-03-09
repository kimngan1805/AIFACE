from transformers import BertTokenizer, BertModel
import torch

model_name = 'bert-base-cased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

def get_bert_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)

    return outputs.last_hidden_state[:, 0, :].squeeze().numpy()

user_input = "Hãy tạo một bối cảnh chạy đua giữa rùa và thỏ."

vector = get_bert_embeddings(user_input)
print(vector)


