"""
Main cli or app entry point
"""

# from mylib.calculator import add
import click
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
# import pandas as pd

from transformers import pipeline


@click.command()
@click.option("--text")
def named_entity_recognition(text):
    ner = pipeline(
        task="ner", model="NYTK/named-entity-recognition-nerkor-hubert-hungarian"
    )
    ner_res = ner(text, aggregation_strategy="simple")
    final_res = list(map(lambda res: res["word"], ner_res))
    click.echo("Recognition complete!")
    click.echo("-------------------------------")
    click.echo(final_res)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    named_entity_recognition()
