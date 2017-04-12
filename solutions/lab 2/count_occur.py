import collections


text = """
The Heart of a Woman (1981) is the fourth of seven autobiographies by American writer Maya Angelou (pictured). She recounts events in her life between 1957 and 1962, as she travels to California, New York, Cairo and Ghana, and raises her teenage son. She becomes a published author active in the US civil rights movement, and is romantically involved with a South African freedom fighter. The book explores Angelou's theme of motherhood, and ends as she looks forward to newfound independence and freedom when her son leaves for college.
"""


def count(string):
    words = (string.replace(",", "")
                  .replace(".", "")
                  .replace("'", "")
                  .replace("(", "")
                  .replace(")", "")
                  .lower()
                  .split())
    occurrences = collections.defaultdict(int)
    for word in words:
        occurrences[word] += 1
    
    for word, number in sorted(occurrences.items(), key=lambda a: a[0]):
        print(word, number)

