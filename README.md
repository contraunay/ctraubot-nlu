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
pipenv run install_spacy_model
```

# Train NLU

```bash
pipenv run python -m ctraubot_nlu.main -c train_nlu
```

# Run as HTTP server and Test
Starting the Rasa NLU as a HTTP server

```bash
pipenv run python -m rasa_nlu.server --path models
```

Sending a HTTP request

```bash
curl -X POST localhost:5000/parse -d '{"q": "Hi", "project": "ctraubot", "model": "nlu"}' | python -m json.tool
```



