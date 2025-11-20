import sys
#import yaml
import argparse
from notes.operations import (help_mesg,
                              list_files,
                              tag_search,
                              read_note,
                              collect_note_from_user,
                              create_note,
                              save_note,
                              edit_note,
                              delete_note,
                              search_query,
                              note_stats)

#cmd = command

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == '--help':
            help_mesg()
        elif cmd == 'list':
            list_files()
        elif cmd == 'tag':
            tag_search()
        elif cmd == 'read':
            read_note(note_id)
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
