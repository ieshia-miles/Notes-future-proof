import os
#import yaml?
#import datetime?

#user requests help menu
def help_mesg():
    help_string = "Here to help"
    print(help_string)

#menu-ask for user input
def menu_display():
    pass

#list all notes, get only .note files
def list_files():
    files = os.listdir('.')
    notes = [f for f in files if f.endswith('.note')]

    for note in notes:
        print(note)

#list notes with a specific tag
def tag_search():
    pass

#display a specific note
def read_note(note_id):
    with open(f"{note_id}.note", "r") as f:
        content = f.read()
        print(content)

def collect_note_from_user():
    note_id = input("Enter note id: ")
    note_text = input("Enter note text: ")
    return note_id, note_text

#create a new note (opens in default editor)
def create_note():
    note_id, note_text = collect_note_from_user
    save_note(note_id, note_text)
    print(f"Note {note_id} saved.")

#save a specific note
def save_note(n,t):
    with open(f"{n}.note", "w") as f:
        f.write(t)

#edit a specific note
def edit_note(note_id):
    pass

#delete a specific note
def delete_note(note_id):
    pass

#search notes for text (title, tags, content)
def search_query():
    pass

#stats about your notes
def note_stats():
    pass