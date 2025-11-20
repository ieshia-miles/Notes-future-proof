class Note:
    def __init__(self, note_id, title, body, tages=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.tags = tags or []

    def edit(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass



"""
The Note object should only handle responsibilities of a single note
(edit itself, save itself, delete itself). A book does not "find" itself
on the shelf, or create itself.
"""
