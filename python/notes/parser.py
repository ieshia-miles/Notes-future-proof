import yaml

def parse_note_text(raw_text):
    parts = raw_text.split("---", 2)
    metadata_text = parts[1].strip()
    body_text = parts[2].strip()
    metadata_dict = yaml.safe_load(metadata_text)
    return metadata_dict, body_text
