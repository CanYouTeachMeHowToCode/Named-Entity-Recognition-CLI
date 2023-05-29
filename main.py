"""
Main cli or app entry point
"""

# from mylib.calculator import add
import click
import re

# import pandas as pd
from transformers import pipeline


@click.command()
@click.option("--text")
def translate_sentence(sentence):
    pipe = pipeline(model="larryvrh/mt5-translation-ja_zh")
    return pipe(f"<-ja2zh-> {sentence}")[0]["translation_text"]


def translate_paragraph(paragraph):
    sentences = []
    cursor = 0
    for i, c in enumerate(paragraph):
        if c == "。":
            sentences.append(paragraph[cursor : i + 1])
            cursor = i + 1
    if paragraph[-1] != "。":
        sentences.append(paragraph[cursor:])
    return "".join(translate_sentence(s) for s in sentences)


def translate_text(text):
    paragraphs = re.split(r"([\r\n]+)", text)
    for i, p in enumerate(paragraphs):
        if len(p.strip()) == 0:
            continue
        paragraphs[i] = translate_paragraph(p)
    result = "".join(paragraphs)
    click.echo("Translation complete!")
    click.echo("-" * 50)
    click.echo(result)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    translate_text()
