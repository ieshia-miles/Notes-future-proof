import sys
import yaml
import argparse

#function for
def help_mesg():
    help_string = "Here to help"
    print(help_string)

def list_files():
    #get all the filenames from the CWD & print them out
    #get only .note files, list comprehension, create a new list called notes
    files = os.listdir('.')
    notes = [f for f in files if f.endswith('.note')]

    for note in notes:
        print(note)

def specific_tag_notes():
    pass

def read_note(n):
    #why the n?
    with open(f"{n}.note", "r") as f:
        content = f.read()
        print(content)

def collect_note_from_user():
    noteid = input("Enter note id: ")
    notetext = input("Enter note text: ")
    return noteid, notetext

def create_note():
    noteid, notetext = collect_note_from_user
    save_note(noteid, notetext)
    print(f"Note {noteid} saved.")

def save_note(n,t):
    with open(f"{n}.note", "w") as f:
        f.write(t)

def edit_note():
    pass

def delete_note():
    pass

def search_query():
    pass

def note_stats():
    pass

#cmd = command
def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == 'help':
            help_mesg()
        elif cmd == 'list':
            list_files()
        elif cmd == 'tag':
            specific_tag_notes()
        elif cmd == 'read':
            read_note()
        elif cmd == 'enter note':
            collect_note_from_user()
        elif cmd == 'create':
            create_note()
        elif cmd == 'save':
            save_note()
        elif cmd == 'edit':
            edit_note()
        elif cmd == 'delete':
            delete_note()
        elif cmd == 'search':
            search_query()
        elif cmd == 'stats':
            note_stats()
        else:
            print()


