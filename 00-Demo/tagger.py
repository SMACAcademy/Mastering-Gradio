from transformers import pipeline
import pandas as pd

ner_tagger = pipeline("ner", aggregation_strategy="simple",
                       #model="ml6team/keyphrase-extraction-kbir-inspec",
                       device=0)
text = '''Muthu is an expert in DevOps, CI/CD Pipelines, Cloud Native Architectures, Kubernetes, and Containerization (Docker). With deep expertise in Generative AI (GenAI), Argo CD, Argo Workflows, LangChain, LlamaIndex, and Model Finetuning, he specializes in building cutting-edge solutions for modern technology challenges.

An advocate for Big Data and Analytics, Muthu excels in leveraging platforms like Apache Spark to drive actionable insights. He is also proficient in Hugging Face and other advanced AI frameworks, enabling the development of state-of-the-art machine learning and AI models. As a passionate iSMAC (IoT, Social, Mobile, Analytics, Cloud) technologist, he integrates innovative strategies to create impactful solutions in diverse industries.

A forward-thinking advisor on emerging technologies and a startup incubator, Muthu is committed to delivering transformative results by embracing high-impact, next-generation technologies while ensuring the adoption of the most relevant and impactful tools in the ever-evolving tech landscape.'''

outputs = ner_tagger(text)
pd.DataFrame(outputs)
print(outputs)
