from tika import parser 

def extract_text_from_pdf(file_path):
    raw = parser.from_file(file_path)
    return raw['content']