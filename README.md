<div align="center">
  <img src="https://github.com/user-attachments/assets/638ba60d-606b-4b5d-a549-abd411f9886e" width="300"/>
</div>



----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MED-LLM-BR-OpenVINO: Medical Large Language Models for Brazilian Portuguese for OpenVINO
MED-LLM-BR-OpenVINO is a **model converted** of the [MED-LLM-BR](https://github.com/HAILab-PUCPR/MED-LLM-BR) collaborative project between [HAILab](https://github.com/HAILab-PUCPR) and [Comsentimento](https://www.comsentimento.com.br/), which aims to develop multiple medical LLMs for Portuguese language, including base models and task-specific models, with different sizes. 

## Contributions:

### Developing Resource-Efficient Clinical LLMs for Brazilian Portuguese
This project leverages LLama and Mistral as base models, adapting them through fine-tuning techniques to enhance their performance in clinical text generation tasks.

To optimize resource utilization during the fine-tuning process, we employed Low-Rank Adaptation (LoRA). This approach enables effective model adaptation with significantly reduced computational and memory requirements, making the fine-tuning process more efficient without compromising the quality of the generated clinical text.

#### Model Description
LLama: LLama is a state-of-the-art language model known for its scalability and efficiency in handling diverse natural language processing tasks. In this project, LLama serves as one of the base models for fine-tuning, aimed at adapting it to the specific requirements of clinical text generation in Portuguese.

#### How to use the models with HuggingFace

Link model FP16 : [Clinical-BR-LlaMA-2-7B-fp16-ov](https://huggingface.co/cabelo/Clinical-BR-LlaMA-2-7B-fp16-ov)

Link model Int8  : [Clinical-BR-LlaMA-2-7B-int8-ov](https://huggingface.co/cabelo/Clinical-BR-LlaMA-2-7B-int8-ov) 

1. Install the required packages:
```bash
pip install -r requirements.txt
```
2 . Run example.
```bash
python inference-MD-LLM-BR.py
LLM model: cabelo/Clinical-BR-LlaMA-2-7B-fp16-ov, FP16
Compiling the model to CPU ...
Question: Paciente admitido com angina instável, progredindo para infarto agudo do miocárdio
(IAM) inferior no primeiro dia de internação; encaminhado para unidade de hemodinâmica, onde
foi feita angioplastia com implante de stent na ponte de safena 

Paciente submeteu-se a uma cirurgia cardíaca em 2014, sendo que o procedimento teve sucesso
e sem complicações graves ou leves. Em julho deste ano apresentou-se ao nosso centro de
emergencia com sintomatologia clínicamente similar à da última crise de IAM, porém com
menor gravidade e evoluência bem melhorada quando comparada as anteriores. Foi realizada
novamente angiografia coronária que mostrou lesões restritivas em ambas artérias
circunflexa e marginal esquerda (figura). Realizado exame eletricofisiológico com
resultados normais. Apresentando-se como paciente com quadro de dor torácica,
auscultação normal e laboratórios normais, foi iniciada terapia farmacologica de classe B.
Após 3 dias de uso, o cuidado médico optou pelo retorno aos medicamentos de classe C,
já que os primeiros não foram capazes de controlar a dor torácica e a frequencia
cardiométrica.

```
