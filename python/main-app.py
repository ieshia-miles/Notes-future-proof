import sys
from notes.notes_collection import NotesCollection
from config.notes_config import notes_dir

#cmd = command

def display_menu():
    print("==Command Menu===")
    print("Choose and option by selecting a number")
    print("1. List Notes")
    print("2. Read a note")
    print("3. Quit")

    choice = input("Choose and option:")

    if choice == "1":
        collection = NotesCollection(notes_dir)
        note_ids = collection.list_notes()

        if not note_ids:
            print("No notes found in NotesLibrary")
            return
        note_ids = sorted(note_ids)
        for index, note_id in enumerate(note_ids, start=1):
            print(f"{index}.{note_id}")
def main():
    collection = NotesCollection(notes_dir) #this creates Librarian
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == '--help':
            help_message()
        elif cmd == 'menu':
            display_menu()
        elif cmd == 'list':
            collection = NotesCollection(notes_dir)
            note_ids = collection.list_notes()

            if not note_ids:
                print("No notes found in NotesLibrary.")
                return

            noted_ids = sorted(note_ids)
            #enemerate gives me both the number (index) and note_id.
            #start=1 makes the list count from 1 instead of 0
            for index, note_id in enumerate(note_ids, start=1):
                print(f"{index}.{note_id}")
        elif cmd == 'tag':
            tag_search()
        elif cmd == 'read':
            pass
        elif cmd == 'enter note':
            collect_note_from_user()
        elif cmd == 'create':
            create_note()
        elif cmd == 'save':
            save_note()
        elif cmd == 'edit':
            edit_note()
        elif cmd == 'delete':
            delete_note(note_id)
        elif cmd == 'search':
            search_query()
        elif cmd == 'stats':
            note_stats()
        else:
            print()

if __name__ == "__main__":
    main()
