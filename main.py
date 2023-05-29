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
    print(text)
    ner = pipeline(task="ner", model="dhtocks/Named-Entity-Recognition")
    result = ner(text)
    print(result)
    click.echo("Recognition complete!")
    click.echo("-" * 50)
    click.echo(result)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    named_entity_recognition()
