# %%
from sentences import get_determiner, get_noun, get_preposition, get_verb, get_preposition, get_prepositional_phrase
import pytest

def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # Test the singular nouns.
    singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_noun(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_nouns

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural nouns.
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns

def test_get_verb():
    # Test the past tense verbs.
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_verb(1, "past")

        # Verify that the word returned from get_verb is
        # one of the words in the past_verbs list.
        assert word in past_verbs

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the present singular verbs.
    present_sigular_verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_sigular_verbs list.
        assert word in present_sigular_verbs

    # Test the present plural verbs.
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(2, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_plural_verbs list.
        assert word in present_plural_verbs

    # Test the future verbs.
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(4):
        word = get_verb(1, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future_verbs list.
        assert word in future_verbs

def test_get_prepostition():
    # Test the preposition.
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_preposition()

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in prepositions

def test_get_prepostition_phrase():
    # Test the preposition.
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    determiners = ["the", "one"]
    nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        prep = get_preposition()
        determiner = get_determiner(1)
        noun = get_noun(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert (prep in prepositions) and (determiner in determiners) and (noun in nouns)

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])
# %%
