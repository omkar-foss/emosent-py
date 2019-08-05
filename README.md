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

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, 
see the 
[tags on this repository](https://github.com/FintelLabs/emosent-py/tags). 

## License

This project is licensed under the MIT License - see the 
[LICENSE.txt](LICENSE.txt) file for more details.