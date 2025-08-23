def recite(start_verse, end_verse):
    verses = {
        'lady': 'I know an old lady who swallowed a %s.',
        'why': (
            'I don\'t know why she swallowed the fly. Perhaps she\'ll die.',
            'It wriggled and jiggled and tickled inside her.',
            'How absurd to swallow a bird!',
            'Imagine that, to swallow a cat!',
            'What a hog, to swallow a dog!',
            'Just opened her throat and swallowed a goat!',
            'I don\'t know how she swallowed a cow!',
            'She\'s dead, of course!'
        ),
        'swallow': 'She swallowed the %s to catch the %s%s',
    }
    subjects = ('fly', 'spider', 'bird', 'cat',
                'dog', 'goat', 'cow', 'horse')

    song = []
    for start in range(start_verse - 1, end_verse):
        song.append(verses['lady'] % subjects[start])
        song.append(verses['why'][start])
        if subjects[start] != subjects[-1]:
            for i in range(start, 0, -1):
                nxt, cur = subjects[i-1:i+1]
                wtf = '.'
                if cur == subjects[2]:
                    wtf = verses['why'][1].replace('It', ' that')
                song.append(verses['swallow'] % (cur, nxt, wtf))
            if subjects[start] != subjects[0]:
                song.append(verses['why'][0])
        song.append('')  # WHY?!?!
    song.pop()

    return song
