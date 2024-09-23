from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='aryan',
    author_email='aryan2ml2901@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2", "huggingface_hub", "transformers", "accelerate", "bitsandbytes", "langchain-community"],
    packages=find_packages()
)
