def recite(start_verse, end_verse):
    verses = (
        'This is the {1}',
        'that {0} the {1}'
    )
    actions_subjects = (
        ('lay in', 'house that Jack built.'),
        ('ate', 'malt'),
        ('killed', 'rat'),
        ('worried', 'cat'),
        ('tossed', 'dog'),
        ('milked', 'cow with the crumpled horn'),
        ('kissed', 'maiden all forlorn'),
        ('married', 'man all tattered and torn'),
        ('woke', 'priest all shaven and shorn'),
        ('kept', 'rooster that crowed in the morn'),
        ('belonged to', 'farmer sowing his corn'),
        ('', 'horse and the hound and the horn')
    )

    song = []
    for start in range(start_verse - 1, end_verse):
        verse = []
        for i in range(start, -1, -1):
            s = verses[i != start]
            verse.append(s.format(*actions_subjects[i]))
        song.append(' '.join(verse))

    return song
