from docx import Document
import find_path


def write_to_doc(title, text):
    document = Document()
    document.add_heading(title, 1)

    p = document.add_paragraph(text)

    download_loc = find_path.get_download_path()
    document.save(download_loc + "\\" + title + ".docx")
    print("Saved file to ", download_loc)
