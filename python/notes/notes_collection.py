import os
from notes.note import Note
from notes.parser import parse_note_text


class NotesCollection:
    def __init__(self, notes_dir):
        self.notes_dir = notes_dir #folder where .note files live

    def search_query(self, text):
        #search notes for some text
        pass

    def stats(self):
        #return high-level stats (count, etc.)
        pass

    def tag_search(self):
        #return notes that have a given tag
        pass

    def list_notes(self):
        #return a list of notes (filenames/note_ids without .note)
        all_notes = os.listdir(self.notes_dir)
        note_ids = []
        for note in all_notes:
            if note.endswith(".note"):
                note_id = note[:-5] #strip .note
                note_ids.append(note_id)
        return note_ids

    def get_note(self, note_id):
        #load a .note file from disk, parse, then return a Note object
        raw_text = self.load_note_text(note_id)
        metadata_dict, body_text = parse_note_text(raw_text)
        note = Note(note_id=note_id, title=metadata_dict["title"], body=body_text,
                    tags=metadata_dict.get("tags"), created=metadata_dict.get("created"))
        return note

    def create_note(self):
        title = input("Title: ")
        body = input("Body: ")
        tags = input("Tags: ").split(",") #split each tag with a comma

    def load_note_text(self, note_id):
        # Load raw text of a note file, given its note_id. For now this returns a string
        filename = f"{note_id}.note"
        filepath = os.path.join(self.notes_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        return content


"""
NotesCollection is responsible for finding, loading, creating,
and organizing notes. Creates note from user input, read from disk,
check if note_id is taken, generate ids. Think of it like a "library system"
"""