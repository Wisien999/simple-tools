import PyPDF4
import os
import sys


def get_path_from_user():
    path = input('path to file:\n')

    if not path.endswith(".pdf"):
        path = path + ".pdf"

    return os.path.abspath(path)


def get_pdf_pages():
    pdf_pages = []
    pdf_pages_content = []
    pdf = PyPDF4.PdfFileReader(f)
    for page_number in range(pdf.getNumPages()):
        pdf_pages.append(pdf.getPage(page_number))
        pdf_pages_content.append(pdf_pages[-1].extractText())
    return pdf_pages, pdf_pages_content


def find_final_pages(input_pages_content):
    final_pages_numbers = []
    for page_number in range(len(input_pages_content) - 1):
        if input_pages_content[page_number] not in input_pages_content[page_number+1]:
            final_pages_numbers.append(page_number)
    final_pages_numbers.append(len(input_pages_content)-1)
    return final_pages_numbers


def create_pdf_writer(input_pages, final_pages_numbers):
    pdf_writer = PyPDF4.PdfFileWriter()
    for page_number in final_pages_numbers:
        pdf_writer.addPage(input_pages[page_number])

    return pdf_writer


def create_final_pdf(pdf_writer, path):
    final_path = path[:-4] + "-short.pdf"
    with open(final_path, "wb") as f:
        pdf_writer.write(f)
    print("File is ready in", final_path)


def get_paths_from_arg():
    args = sys.argv[1:]
    if len(args) == 0:
        return False

    return map(os.path.abspath, args)

def main():
    paths = get_paths_from_arg()

    if not paths:
        paths = [get_path_from_user()]
    
    try:
        for path in paths:
            with open(path, "rb") as f:
                input_pages, input_pages_content = get_pdf_pages()
                final_pages_numbers = find_final_pages(input_pages_content)
                final_pdf_writer = create_pdf_writer(input_pages, final_pages_numbers)
                create_final_pdf(final_pdf_writer, path)
    except FileNotFoundError:
        print("File not found")

    #input("Press Enter to exit...")

if __name__ == "__main__":
    main()

