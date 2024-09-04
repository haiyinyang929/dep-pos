# POS Tagging and Dependency Visualizer

This project is a small practice project using the `spaCy` package for Natural Language Processing (NLP). The user can input a sentence, and the program will output the Part-of-Speech (POS) tagging for each token in the sentence. Additionally, the project generates an HTML file that visualizes the dependency structure of the sentence as a graph.

## Features

- POS tagging of input sentences.
- Generation of an HTML file with a dependency graph visualization.
- Simple and intuitive interface for users.

## Installation

1. Clone this repository to your local machine

2. Create a virtual environment (optional but recommended)

3. Activate the virtual environment
  
4. Install the required packages
  
5. Download the necessary spaCy language model:

    ```bash
    python -m spacy download en_core_web_sm
    ```

## Dependency Graph
After processing the sentence, an HTML file (sentence.html) will be generated that shows the dependency graph. Open this file in a web browser to view the visual representation of the sentence's syntactic structure.

