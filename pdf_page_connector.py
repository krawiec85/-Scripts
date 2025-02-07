import PyPDF2
import os


def get_pages_from_user():
    pages = input("Podaj numery stron do połączenia (np. 1-3,5,7-9): ")
    page_ranges = []
    for part in pages.split(','):
        if '-' in part:
            start, end = part.split('-')
            page_ranges.extend(range(int(start), int(end) + 1))
        else:
            page_ranges.append(int(part))
    return page_ranges


merger = PyPDF2.PdfMerger()

selected_pages = get_pages_from_user()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        with open(file, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            selected_pages_in_file = [page for page in selected_pages if page <= len(reader.pages)]
            merger.append(file, pages=selected_pages_in_file)

merger.write("Razem.pdf")
merger.close()
