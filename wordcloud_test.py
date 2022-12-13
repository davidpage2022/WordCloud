"""Test word cloud tools."""
from wordcloud import WordCloud

FILENAME = "text.txt"
TEXT = """I am i, listen to me roar! The ROAR of a thousand lions, and lion's playthings.
We are the lolly pop guild and we are here to collect the rent."""


# EXCLUDED_WORDS = ["the", "a", "i", "to"]


def test_word_cloud():
    # text = TEXT
    text = WordCloud.load_text_from_file(FILENAME)

    word_cloud = WordCloud(text, min_length=4, max_words=15)
    print(word_cloud.word_to_count)
    for word in word_cloud.words:
        print(word)

    word_cloud.render_to_image(filename="world-cloud.png", open_after=True)


if __name__ == '__main__':
    test_word_cloud()
