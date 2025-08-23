TOTAL_NOTES = 12

sharp_notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
flat_notes = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
steps = {"m": 1, "M": 2, "A": 3}


class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.notes = sharp_notes if self.key_signature(tonic) == "#" else flat_notes

    def key_signature(self, tonic):
        if "#" in tonic or tonic in ("C", "G", "D", "A", "E", "B", "a", "e", "b"):
            return "#"
        return "b"

    def chromatic(self):
        index = self.notes.index(self.tonic)
        return self.notes[index:] + self.notes[:index]

    def interval(self, intervals):
        index = self.notes.index(self.tonic)
        scale = [self.tonic]

        for step in tuple(intervals):
            skip = steps[step]
            index = (index + skip) % TOTAL_NOTES
            scale.append(self.notes[index])

        return scale
