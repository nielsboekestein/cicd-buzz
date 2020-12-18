from buzz import generator


def test_sample_single_word():
    een = ('foo', 'bar', 'foobar')
    word = generator.sample(een)
    assert word in een


def test_sample_multiple_words():
    een = ('foo', 'bar', 'foobar')
    words = generator.sample(een, 2)
    assert len(words) == 2
    assert words[0] in een
    assert words[1] in een
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
