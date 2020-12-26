from docx import Document


def write_to_doc(title, text):
    document = Document()
    document.add_heading(title, 1)

    p = document.add_paragraph(text)
    # TODO: save to Documents folder in C:
    document.save(title + ".docx")
