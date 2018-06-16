#!/bin/bash -e

# Use space model 'en'
# Here we can use `en_core_web_lg` which is ~900MB

spacy_en_installed=$(pipenv run python -m pip show en-core-web-md)

if test -z "$spacy_en_installed"
then
    python -m spacy download en_core_web_md
fi

python -m spacy link en_core_web_md en
