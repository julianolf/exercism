TOTAL_NOTES = 12

sharp_notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
flat_notes = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
steps = {"m": 1, "M": 2, "A": 3}


class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.capitalize()

        if self.key_signature(tonic) == "#":
            self.notes = sharp_notes
        else:
            self.notes = flat_notes

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

    @staticmethod
    def key_signature(tonic, ascending=True):
        if ascending and tonic in ("C", "a"):
            return "#"

        if "#" in tonic or tonic in ("G", "D", "A", "E", "B", "e", "b"):
            return "#"

        return "b"
