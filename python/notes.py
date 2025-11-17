import sys
import yaml
import argparse

#function for
def help_mesg():
    help_string = "Here to help"
    print(help_string)

def create_note():

def list_notes():
    #get all the filenames from the CWD
    #print them out
    print("All Note Files")

def specific_tag_notes():
    pass

def read_note(n):
    #why the n?
    pass

def edit_note():
    pass

def delete_note():
    pass

def search_query():
    pass

def note_stats():
    pass

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == 'help':
            help_mesg()
        elif cmd == 'create':
            create_note()
        elif cmd == 'list':
            list_notes
        elif cmd == 'tag':
            specific_tag_notes()
        elif cmd == 'read':
            read_note()
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
