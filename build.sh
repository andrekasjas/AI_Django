#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python -m spacy download es_core_news_md