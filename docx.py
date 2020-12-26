from docx import Document


def write_to_docx(text):
    document = Document()
    p = document.add_paragraph(text)
    document.save("demo.docx")


write_to_docx("Hello, World!")

