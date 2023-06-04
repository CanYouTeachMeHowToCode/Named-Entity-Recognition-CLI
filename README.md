[![Continuous Integration](https://github.com/CanYouTeachMeHowToCode/Named-Entity-Recognition-CLI/actions/workflows/cicd.yml/badge.svg)](https://github.com/CanYouTeachMeHowToCode/Named-Entity-Recognition-CLI/actions/workflows/cicd.yml)
## A Named-Entity-Recognition Command-Line Interface

**Individual Project One: Setup Continuous Integration with Github Actions and Github Codespaces for CLI Prediction Tool**

In this project, I implemented a [click](https://github.com/pallets/click) Command-Line Interface (CLI) prediction tool that uses a [HuggingFace](https://huggingface.co) pre-trained model to perform the named entity recognition task of the input text. 

### Setup (Manually)
- Create a new virtual environment with python version `3.10.11`
- Activate the virtual environment and run command 
```
make all
```
, which will perform the entire building process including installing necessary packages/modules, linting, testing, formatting, and deployment.

### Usage

- Run command 
```
python ner.py --text [text]
```
, where `text` is the input text in string format; for instance, the output recognized named entity of input text `"New York is better than San Francisco."` will be `['New York', 'San Francisco']`.

### CI/CD
Github Actions configured in .github/workflows

### References
- [HuggingFace](https://huggingface.co)
- [click](https://github.com/pallets/click)





