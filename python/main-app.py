import sys
from notes.notes_collection import NotesCollection
from config.notes_config import notes_dir

#cmd = command

def display_note_details(note): #helper function
    """Prints the details of a Note object in a consistent way"""
    print(f"Title: {note.title}")
    tags = note.tags or []
    print(f"Tags: {','.join(tags)}")
    print(f"Created on: {note.created}")
    print("-" * 40)
    print(note.body)

def display_menu(collection):
    while True:
        print()
        print("==Command Menu===")
        print("Choose and option by selecting a number")
        print("1. List Notes")
        print("2. Read a note")
        print("3. Quit")

        choice = input("Choose and option:")

        if choice == "1":
            note_ids = collection.list_notes()
            if not note_ids:
                print("No notes found in NotesLibrary")
                return
            note_ids = sorted(note_ids)
            for index, note_id in enumerate(note_ids, start=1):
                print(f"{index}.{note_id}")

        elif choice == "2":
            #ask user which note they want to read
            note_id = input("Enter note id to read: ")
            note = collection.get_note(note_id)
            print() #add a blank line b4 showing the note
            display_note_details(note)

        elif choice == "3":
            print("Goodbye!")
            break #leaves the loop and returns to main()
        else:
            print("Invalid choice. Please enter 1, 2, ...")



def main():
    collection = NotesCollection(notes_dir) #this creates Librarian
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == '--help':
            help_message()

        elif cmd == 'menu':
            display_menu(collection)

        elif cmd == 'list':
            note_ids = collection.list_notes()
            if not note_ids:
                print("No notes found in NotesLibrary.")
                return
            noted_ids = sorted(note_ids)
            #enumerate gives me both the number (index) and note_id.
            #start=1 makes the list count from 1 instead of 0
            for index, note_id in enumerate(note_ids, start=1):
                print(f"{index}.{note_id}")

        elif cmd == 'tag':
            tag_search()

        elif cmd == 'read':
            #make sure user gave a note id. ex. main-app.py read grocery-list sys.argv[2] is grocery-list
            if len(sys.argv) <3:
                print("Error: Provide note id")
                return
            note_id = sys.argv[2]
            note = collection.get_note(note_id)
            print() #blank line for cleaner display
            display_note_details(note)

        elif cmd == 'enter note':
            collect_note_from_user()
        elif cmd == 'create':
            pass
        elif cmd == 'save':
            pass
        elif cmd == 'edit':
            pass
        elif cmd == 'delete':
            pass
        elif cmd == 'search':
            pass
        elif cmd == 'stats':
            pass
        else:
            print()

if __name__ == "__main__":
    main()
