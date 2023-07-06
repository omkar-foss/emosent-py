# emosent-py

emosent-py is a Python utility package to get Sentiment Rankings for Unicode Emojis. 

Based on the research by Kralj Novak P, Smailović J, Sluban B, Mozetič I
(2015) on _Sentiment of Emojis_.

Journal Link:
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144296

CSV Data acquired from CLARIN repository,
Repository Link: http://hdl.handle.net/11356/1048

This project is inspired by [emoji-sentiment](https://github.com/dematerializer/emoji-sentiment), a similar utility written in JavaScript.

## Emoji Support

The complete listed of Emojis to Sentiment Ranking supported by this project 
can be found at 
[Emoji Sentiment Ranking v1.0](http://kt.ijs.si/data/Emoji_sentiment_ranking/).

## Installation

You can install emosent-py from using `pip`:
```bash
pip install emosent-py
```

## Usage

#### Example 1

```python
from emosent import get_emoji_sentiment_rank
get_emoji_sentiment_rank('❤')
```
Output:
```python 
{'unicode_codepoint': '0x2764',
 'occurrences': 8050,
 'position': 0.746943086,
 'negative': 355.0,
 'neutral': 1334.0,
 'positive': 6361.0,
 'unicode_name': 'HEAVY BLACK HEART',
 'unicode_block': 'Dingbats',
 'sentiment_score': 0.746}
```

#### Example 2

```python
from emosent import get_emoji_sentiment_rank

# This function returns the emoji sentiment rank 
# mapped to the specified character.
get_emoji_sentiment_rank('😂')
```
Output:
```python 
{'unicode_codepoint': '0x1f602',
 'occurrences': 14622,
 'position': 0.805100583,
 'negative': 3614.0,
 'neutral': 4163.0,
 'positive': 6845.0,
 'unicode_name': 'FACE WITH TEARS OF JOY',
 'unicode_block': 'Emoticons',
 'sentiment_score': 0.221}
```

#### Example 3

```python
from emosent import get_emoji_sentiment_rank_multiple

# Parses the input text character by character and 
# extracts emoji sentiment ranks and their respective positions in the text.
get_emoji_sentiment_rank_multiple('well done buddy! 😁👏')
```
Output:
```python 
# Here, the emojis are found at positions 17 and 18 in the specified text.
[{'text_position': 17,
  'emoji_sentiment_rank': {'unicode_codepoint': '0x1f601',
   'occurrences': 2189,
   'position': 0.796151187,
   'negative': 278.0,
   'neutral': 648.0,
   'positive': 1263.0,
   'unicode_name': 'GRINNING FACE WITH SMILING EYES',
   'unicode_block': 'Emoticons',
   'sentiment_score': 0.45}},
 {'text_position': 18,
  'emoji_sentiment_rank': {'unicode_codepoint': '0x1f44f',
   'occurrences': 2336,
   'position': 0.787130164,
   'negative': 243.0,
   'neutral': 634.0,
   'positive': 1459.0,
   'unicode_name': 'CLAPPING HANDS SIGN',
   'unicode_block': 'Miscellaneous Symbols and Pictographs',
   'sentiment_score': 0.521}}]

```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, 
see the 
[tags on this repository](https://github.com/FintelLabs/emosent-py/tags). 

## License

This project is licensed under the MIT License - see the 
[LICENSE.txt](LICENSE.txt) file for more details.
