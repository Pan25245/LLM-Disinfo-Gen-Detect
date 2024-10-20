# Weak-to-Strong Generalisation in Large Language Models for Detecting and Generating Social Media Disinformation Campaigns

## Abstract

Social media platforms have become powerful channels for disinformation campaigns that manipulate public opinion and spread misinformation. This thesis investigates the dual role of large language models (LLMs) in both generating and detecting such disinformation on social media. We explore a technique called weak-to-strong generalisation, where we fine-tune a more advanced model (GPT-4o- mini) using outputs from a less advanced model (GPT-3.5-turbo-instruct) through iterative prompting, enhancing its ability to generate convincing disinformation. Concurrently, we assess the performance of various LLMs—including GPT-4o- mini, Llama-3-70b, Gemini-1.5-flash, and BLOOM-560m—in generating and detecting diverse types of misleading tweets, such as emotional, adversarial, and conspiratorial messages. To improve detection accuracy, we employ advanced methods like Siamese Neural Networks (SNNs) combined with Long Short-Term Memory (LSTM) using GPT-2 or BERT embeddings. Emphasising the principles of Green AI, we prioritise energy-efficient, open-source models like BLOOM to reduce computational costs without sacrificing performance. Our findings demonstrate that the weak-to-strong generalisation approach significantly enhances disinformation generation capabilities. Furthermore, we show that LLMs, when responsibly applied, can effectively detect and counteract misinformation on social media, contributing to efforts in mitigating the impact of disinformation campaigns.

## Usage
The notebooks require API keys for models like GPT, Llama, and Gemini, which are not included in this repository. To replicate the results:
1. Obtain API keys for GPT, Llama, and Gemini models.
2. Replace the placeholders in the notebooks where API calls are made with your own API keys.

### Pre-trained Models
I have already trained the models for:
1. SNN + GPT-2
2. SNN + BERT
3. Fine-tuned BLOOM on arson data
   
The trained models and the training data are provided under the folder siamGPTDetect/models/. The exact process used for training these models is documented in the respective notebooks. You can train it again with different parameters as you wish. 

### Running the Experiments
To run the experiments, use the two primary notebooks provided:

1. Weak-to-Strong Generalisation: This notebook demonstrates the weak-to-strong generalisation approach used in the project.
2. Benchmarking LLMs: This notebook benchmarks the performance of different LLMs on generating and detecting disinformation.



## Acknowledgement 

Special thanks to my supervisor, Dr. Mehwish Nasim and my co-supervisor, Professor Christian Grimme for their support.

This report is submitted as partial fulfilment of the requirements for the Honours Programme of the Department of Computer Science and Software Engineering, The University of Western Australia,2024
