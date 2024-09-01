form optimum.intel.openvino import OVModelForCausalLM
from transformers import AutoTokenizer, AutoConfig
from transformers.generation.streamers import TextStreamer

model_id = 'cabelo/Clinical-BR-LlaMA-2-7B-int16-ov'
model_vendor, model_name = model_id.split('/')

model_precision = 'FP16'

print(f'LLM model: {model_id}, {model_precision}')

tokenizer = AutoTokenizer.from_pretrained(model_id)
ov_model = OVModelForCausalLM.from_pretrained(
    model_id = f'{model_name}/{model_precision}',
    device='CPU',
    ov_config={"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""},
    config=AutoConfig.from_pretrained(model_name)
)

# Generation with a prompt message
question = 'Paciente admitido com angina instável, progredindo para infarto agudo do miocárdio (IAM) inferior no primeiro dia de internação; encaminhado para unidade de hemodinâmica, onde foi feita angioplastia com implante de stent na ponte de'

prompt_text_tinyllama = f"""\
<|system|>
Você é um assistente prestativo Médico PHD.</s>
<|user|>
{question}</s>
<|assistant|>
"""

print('Question:', question)
input_tokens = tokenizer(prompt_text_tinyllama, return_tensors='pt', add_special_tokens=False)
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
response = ov_model.generate(**input_tokens, max_new_tokens=300, num_return_sequences=1, temperature=1.0, do_sample=True, top_k=5, top_p=0.85, repetition_penalty=1.2, streamer=streamer)
