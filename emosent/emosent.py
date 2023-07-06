"""
    Module to convert Unicode Emojis to corresponding Sentiment Rankings.

    Based on the research by Kralj Novak P, Smailović J, Sluban B, Mozetič I
    (2015) on Sentiment of Emojis.

    Journal Link:
    https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144296

    CSV Data acquired from CLARIN repository,
    Repository Link: http://hdl.handle.net/11356/1048
"""

import csv
import logging
from os import path
import re

logging.basicConfig(
    level=logging.INFO,
    format='%(process)d | %(levelname)s | %(message)s'
)


# pylint: disable=too-many-locals
def _build_dict_from_csv(csv_path):
    """ Builds the Emoji to Sentiment dictionary from the CSV file. """

    emoji_sentiment_rankings = {}

    # Explicit use of UTF-8 encoding is required while reading Emojis from CSV
    # to avoid errors in systems where UTF-8 is not the default encoding (e.g. Windows).
    # Credits to MrMindy for this fix.
    with open(csv_path, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        _header_row = next(csv_reader)
        for row in csv_reader:
            emoji = row[0]
            unicode_codepoint = row[1]
            occurrences = int(row[2])
            position = float(row[3])
            negative = float(row[4])
            neutral = float(row[5])
            positive = float(row[6])
            unicode_name = row[7]
            unicode_block = row[8]
            sentiment_score = float(
                '{:.3f}'.format((positive - negative) / occurrences)
            )

            emoji_sentiment_rankings[emoji] = {
                'unicode_codepoint': unicode_codepoint,
                'occurrences': occurrences,
                'position': position,
                'negative': negative,
                'neutral': neutral,
                'positive': positive,
                'unicode_name': unicode_name,
                'unicode_block': unicode_block,
                'sentiment_score': sentiment_score
            }

    return emoji_sentiment_rankings


def get_emoji_sentiment_rank(char):
    """ Returns the emoji sentiment rank mapped to the specified character. """

    return EMOJI_SENTIMENT_DICT.get(char.strip())


def get_emoji_sentiment_rank_multiple(text):
    """
        Parses the input text character by character and extracts emoji 
        sentiment ranks and their respective positions in the text.
    """

    emoji_results = []

    for index, char in enumerate(text.strip()):
        if char.isalnum():
            continue

        sentiment_rank = EMOJI_SENTIMENT_DICT.get(char)
        if sentiment_rank:
            emoji_results.append({
                'text_position': index,
                'emoji_sentiment_rank': sentiment_rank
            })

    return emoji_results


EMOJI_SENTIMENT_DICT = _build_dict_from_csv(
    path.join(
        path.abspath(path.dirname(__file__)),
        'data/Emoji_Sentiment_Data_v1.0.csv'
    )
)
