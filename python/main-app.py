import sys
import yaml
import argparse
from notes import operations

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


