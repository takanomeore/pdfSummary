#!/usr/bin/env python

import sys
#sys.path.append('/lib/python3/dist-packages')
import openai

args = sys.argv

openai.api_key = ("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")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role":"user", "content":args[2]},
        ],
    )

    print(response['choices'][0]["message"]["content"])
except Exception as e:
    print(e)