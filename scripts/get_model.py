from transformers import AutoTokenizer, AutoModel

model = AutoModel.from_pretrained("intfloat/multilingual-e5-base")
tokenizer = AutoTokenizer.from_pretrained("intfloat/multilingual-e5-base")
model.save_pretrained("../models/multilingual-e5-base")
tokenizer.save_pretrained("../models/multilingual-e5-base")
