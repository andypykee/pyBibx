from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name='pybibx',
    version='4.5.3',
    license='GNU',
    author='Andrew Asante',
    author_email='andrew.asante.kwasi@gmail.com',
    url='https://github.com/andypykee/pybibx',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'bertopic',
        'bert-extractive-summarizer',
        'chardet',
        'google-generativeai',
        'gensim',
        'llmx',
        'matplotlib',
        'networkx',
        'numba',
        'numpy',
        'pandas',
        'plotly',
        'scipy',
        'scikit-learn',
        'sentencepiece',
        'sentence-transformers',
        'torch', 
        'torchvision',
        'torchaudio',
        'transformers',
        'umap-learn',
        'openai',
        'wordcloud'
    ],
    zip_safe=True,
    description='A Bibliometric and Scientometric Library Powered with Artificial Intelligence Tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
