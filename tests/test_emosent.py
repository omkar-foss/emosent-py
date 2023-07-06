"""
    Unit tests for this project.
"""

import unittest
from emosent import get_emoji_sentiment_rank, get_emoji_sentiment_rank_multiple


class TestEmosent(unittest.TestCase):

    def test_basic_ranking(self):
        print('\ntest_basic_ranking: It checks for basic ranking functionality\n')
        emoji = '❤'
        expected_result = {
            'unicode_codepoint': '0x2764',
            'occurrences': 8050,
            'position': 0.746943086,
            'negative': 355.0,
            'neutral': 1334.0,
            'positive': 6361.0,
            'unicode_name': 'HEAVY BLACK HEART',
            'unicode_block': 'Dingbats',
            'sentiment_score': 0.746
        }
        result = get_emoji_sentiment_rank(emoji)
        self.assertDictEqual(result, expected_result)

        emoji = ''
        result = get_emoji_sentiment_rank(emoji)
        self.assertIsNone(result)

        emoji = '   '
        result = get_emoji_sentiment_rank(emoji)
        self.assertIsNone(result)

    def test_emojis_text_extraction(self):
        print(
            '\ntest_emojis_text_extraction: It checks for multiple emojis in '
            'text functionality\n'
        )
        text = 'that is amazing! 😂❤'
        expected_result = [
            {
                'text_position': 17,
                'emoji_sentiment_rank': {
                    'unicode_codepoint': '0x1f602',
                    'occurrences': 14622,
                    'position': 0.805100583,
                    'negative': 3614.0,
                    'neutral': 4163.0,
                    'positive': 6845.0,
                    'unicode_name': 'FACE WITH TEARS OF JOY',
                    'unicode_block': 'Emoticons',
                    'sentiment_score': 0.221
                }
            },
            {
                'text_position': 18,
                'emoji_sentiment_rank': {
                    'unicode_codepoint': '0x2764',
                    'occurrences': 8050,
                    'position': 0.746943086,
                    'negative': 355.0,
                    'neutral': 1334.0,
                    'positive': 6361.0,
                    'unicode_name': 'HEAVY BLACK HEART',
                    'unicode_block': 'Dingbats',
                    'sentiment_score': 0.746
                }
            }
        ]
        result = get_emoji_sentiment_rank_multiple(text)
        self.assertListEqual(result, expected_result)

        text = ''
        result = get_emoji_sentiment_rank_multiple(text)
        self.assertListEqual(result, [])

        text = '   '
        result = get_emoji_sentiment_rank_multiple(text)
        self.assertListEqual(result, [])


if __name__ == '__main__':
    unittest.main()
