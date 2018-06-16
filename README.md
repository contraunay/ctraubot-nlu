# ctraubot-nlu
This is a component of a chatbot called "ctraubot". It is used for handling the Natural Language Understanding (NLU) feature

# Setting up (macOS)

**Install Python 3.6 (recommended)**

```bash
brew install python
```
**Install [pipenv](https://docs.pipenv.org/)**, so we can install dependencies and manage virtual environments.

```bash
python -m pip install pipenv
```

**Install dependencies via pipenv**

```bash
cd ctraubot
# create a shared virtualenv accross serveral project instead of a generated one
python -m venv {path_to_your_virtualenvs}/ctraubot-nlu
ln -s {path_to_your_virtualenvs}/ctraubot-nlu .venv
pipenv install
```


