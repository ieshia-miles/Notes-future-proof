import os

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
        #return or print a list of notes
        pass

    #?
    def get_note(self, note_id):
        pass

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