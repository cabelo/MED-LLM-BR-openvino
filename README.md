<div align="center">
  <img src="https://github.com/user-attachments/assets/638ba60d-606b-4b5d-a549-abd411f9886e" width="300"/>
</div>



----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MED-LLM-BR-OpenVINO: Medical Large Language Models for Brazilian Portuguese for OpenVINO
MED-LLM-BR-OpenVINO is a **model converted** of the collaborative project between [HAILab](https://github.com/HAILab-PUCPR) and [Comsentimento](https://www.comsentimento.com.br/), which aims to develop multiple medical LLMs for Portuguese language, including base models and task-specific models, with different sizes. 

## Contributions:

### Developing Resource-Efficient Clinical LLMs for Brazilian Portuguese
This project leverages LLama and Mistral as base models, adapting them through fine-tuning techniques to enhance their performance in clinical text generation tasks.

To optimize resource utilization during the fine-tuning process, we employed Low-Rank Adaptation (LoRA). This approach enables effective model adaptation with significantly reduced computational and memory requirements, making the fine-tuning process more efficient without compromising the quality of the generated clinical text.

#### Model Description
LLama: LLama is a state-of-the-art language model known for its scalability and efficiency in handling diverse natural language processing tasks. In this project, LLama serves as one of the base models for fine-tuning, aimed at adapting it to the specific requirements of clinical text generation in Portuguese.

#### How to use the models with HuggingFace

Link model FP16 : [Clinical-BR-LlaMA-2-7B-int16-ov](https://huggingface.co/cabelo/Clinical-BR-LlaMA-2-7B-int16-ov)

Link model FP8  : [Clinical-BR-LlaMA-2-7B-int8-ov]() comming...

Link model FP4  : [Clinical-BR-LlaMA-2-7B-int4-ov]() comming...


