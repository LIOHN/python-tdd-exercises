import pytest
from collections import Counter

def reverse_list(data_list):
    """
    Reverses order of elements in list l.
    """
    return data_list[::-1]

def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

# ------------------------------------------------------------------------------

def reverse_string(string):
    """
    Reverses order of characters in string s.
    """
    return string[::-1]


def test_reverse_string():
    assert reverse_string("foobar") == "raboof"

# ------------------------------------------------------------------------------

def is_english_vowel(letter):
    """
    Returns True if "letter" is an english vowel
    and False otherwise.
    """
    vowel_list = ['a','e','i','o','u','A','E','I','O','U','y','Y']
    return letter in vowel_list


def test_is_english_vowel():
    assert is_english_vowel('a')
    assert is_english_vowel('e')
    assert is_english_vowel('i')
    assert is_english_vowel('o')
    assert is_english_vowel('u')
    assert is_english_vowel('y')
    assert is_english_vowel('A')
    assert is_english_vowel('E')
    assert is_english_vowel('I')
    assert is_english_vowel('O')
    assert is_english_vowel('U')
    assert is_english_vowel('Y')
    assert not is_english_vowel('k')
    assert not is_english_vowel('z')
    assert not is_english_vowel('?')

# ------------------------------------------------------------------------------

def count_num_vowels(s):
    """
    Returns the number of vowels in a string s.
    """
    vowel_count = 0
    vowel_list = ['a','e','i','o','u','A','E','I','O','U','y','Y']
    for i, v in enumerate(s):
        vowel_count += 1 if v in vowel_list else 0
    return vowel_count

def test_count_num_vowels():
    sentence = "hey ho let's go"
    assert count_num_vowels(sentence) == 5
    sentence = "HEY ho let's GO"
    assert count_num_vowels(sentence) == 5
    paragraph = """She told me her name was Billie Jean,
                   as she caused a scene
                   Then every head turned with eyes
                   that dreamed of being the one
                   Who will dance on the floor in the round"""
    assert count_num_vowels(paragraph) == 54

# ------------------------------------------------------------------------------

def histogram(data_list):
    """
    Converts a list of integers into a simple string histogram.
    """
    s = ''
    for i, number in enumerate(data_list):
        s += number * '#'
        if i < len(data_list) - 1:
            s += '\n'
    return s

def test_histogram():
    assert histogram([1, 4]) == '#\n####'
    assert histogram([2, 5, 1]) == '##\n#####\n#'


# ------------------------------------------------------------------------------

def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    return list(map(len, s.split()))


def test_get_word_lengths():
    text = "Hello World"
    assert get_word_lengths(text) == [5, 5]
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]

# ------------------------------------------------------------------------------

def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    return max(s.split(), key=len)


def test_find_longest_word():
    text = "Three tomatoes are walking down the street"
    assert find_longest_word(text) == "tomatoes"
    text = "foo foo1 foo2 foo3"
    assert find_longest_word(text) == "foo1"
    text = """Django is a Python based free and open-source web 
           framework that follows the MVC architectural pattern
           """
    assert find_longest_word(text) == "architectural"


# ------------------------------------------------------------------------------

def validate_dna(s):
    """
    Return True if the DNA string only contains characters
    a, c, t, or g (lower or uppercase). False otherwise.
    """
    valid_nucleotides = 'actgACTG'
    return all(i in valid_nucleotides for i in s)


def test_validate_dna():
    assert validate_dna('AGAGTGGCAT')
    assert validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag')
    assert not validate_dna('definitely not a DNA sequence')
    assert not validate_dna('CCGxTAGGAcaag')
    assert not validate_dna('CCxGGAAGAGCTTACTTAGccggaagagcttacttag')


# ------------------------------------------------------------------------------

def base_pair(c):
    """
    Return the corresponding character (lowercase)
    of the base pair. If the base is not recognized,
    return 'unknown'.
    """
    switch = {
        'a': 't',
        't': 'a',
        'c': 'g',
        'g': 'c',
        'A': 't',
        'T': 'a',
        'C': 'g',
        'G': 'c'
    }
    pair = switch.get(c, 'unknown')
    return pair

def test_base_pair():
    assert base_pair('a') == 't'
    assert base_pair('t') == 'a'
    assert base_pair('c') == 'g'
    assert base_pair('g') == 'c'
    assert base_pair('A') == 't'
    assert base_pair('T') == 'a'
    assert base_pair('C') == 'g'
    assert base_pair('G') == 'c'
    assert base_pair('x') == 'unknown'
    assert base_pair('foo') == 'unknown'

# ------------------------------------------------------------------------------

def transcribe_dna_to_rna(s):
    """
    Return string s with each letter T replaced by U.
    Result is always uppercase.
    """
    rna = (s.replace('t', 'u')).replace('T','U')
    return rna.upper()


def test_transcribe_dna_to_rna():
    dna = 'CCGGAAGAGCTTACTTAGccggaagagcttacttag'
    assert transcribe_dna_to_rna(dna) == 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG'

# ------------------------------------------------------------------------------

def remove_substring(substring, string):
    """
    Returns string with all occurrences of substring removed.
    """
    return string.replace(substring, '')


def test_remove_substring():
    assert remove_substring('GAA', 'CCGGAAGAGCTTACTTAG') == 'CCGGAGCTTACTTAG'
    assert remove_substring('CCG', 'CCGGAAGAGCTTACTTAG') == 'GAAGAGCTTACTTAG'
    assert remove_substring('TAG', 'CCGGAAGAGCTTACTTAG') == 'CCGGAAGAGCTTACT'
    assert remove_substring('GAA', 'GAAGAAGAA') == ''


# ------------------------------------------------------------------------------

def get_position_indices(triplet, dna):
    """
    Returns list of position indices for a specific triplet (3-mer)
    in a DNA sequence. We start counting from 0
    and jump by 3 characters from one position to the next.
    """
    locations = []
    for i in range(0, len(dna), 3):
        if triplet == dna[i:i + 3]:
            locations.append(i / 3)
    return locations


def test_get_position_indices():
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAG') == [1]
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAGGAAGAA') == [1, 6, 7]



# ------------------------------------------------------------------------------

def get_3mer_usage_chart(s):
    """
    This routine implements a 'sliding window'
    and extracts all possible consecutive 3-mers.
    It counts how often they appear and returns
    a list of tuples with (name, occurrence).
    The list is alphabetically sorted by the name
    of the 3-mer.
    """
    list_of_3mers = []
    for i in range(len(s) - 2):                      # looking for triplets, so list comprehension ends 2 early
        list_of_3mers.append(s[i:i + 3])             # create list of 3mers
    chart = sorted(Counter(list_of_3mers).items())   # collections.Counter counts occurances from list.
    return chart                                     # dot items makes it a list and sorted orders it alphabetically

def test_get_3mer_usage_chart():
    s = 'CCGGAAGAGCTTACTTAGGAAGAA'
    result = [('AAG', 2), ('ACT', 1), ('AGA', 2), ('AGC', 1), ('AGG', 1), ('CCG', 1), ('CGG', 1), ('CTT', 2),
              ('GAA', 3), ('GAG', 1), ('GCT', 1), ('GGA', 2), ('TAC', 1), ('TAG', 1), ('TTA', 2)]
    assert get_3mer_usage_chart(s) == result

# ------------------------------------------------------------------------------


def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    return [float(i.split('  ')[column_number - 1]) for i in open(file_name).readlines()]

def test_read_column():

    import tempfile
    import os

    text = """1   0.1  0.001\n2   0.2  0.002\n3   0.3  0.003\n4   0.4  0.004\n5   0.5  0.005\n6   0.6  0.006"""


    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will read the column
    assert read_column(file_name, 2) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

    # we remove the temporary file
    # os.unlink(file_name)


# ------------------------------------------------------------------------------


def character_statistics(file_name):
    """
    Reads text from file file_name, then
    lowercases the text, and then returns
    a tuple (x, y), where x is the most abundant
    and y is the least abundant but present character found.
    Use the isalpha() method to figure out
    whether the character is in the alphabet.
    """
    def take_second(elem):
        return elem[1]
    '''
    file is opened, letters are extracted from text and counted by Counter, returning
    a dict of letters and corresponding occurences. That dict is turned into a list 
    with .items() then ordered by occurences (key=take_second), in descending order
    (most occurences first, reverse=true). Return the first two.
    '''
    with open(file_name) as f:
        letterCount = sorted(Counter(letter for line in f
                                    for letter in line.lower()
                                    if letter.isalpha()).items(),
                             key=take_second,
                             reverse=True)
    return letterCount[0][0], letterCount[23][0]

def test_character_statistics():

    import tempfile
    import os

    text = """
To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscover'd country from whose bourn
No traveller returns, puzzzles the will
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all;
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry,
And lose the name of action.--Soft you now!
The fair Ophelia! Nymph, in thy orisons
Be all my sins remember'd."""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will get the stats
    (most_abundant, least_abundant) = character_statistics(file_name)
    assert (most_abundant, least_abundant) == ('e', 'q')

    # we remove the temporary file
    # os.unlink(file_name)

