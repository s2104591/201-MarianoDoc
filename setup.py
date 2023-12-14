from setuptools import setup, find_packages


VERSION = '1.0.13'

DESCRIPTION = 'Produce WORD and PDF files with great ease, examples provided on import '
LONG_DESCRIPTION =  'With Mariano Doc, its easy to insert lines of texts into a WORD or PDF file. <br>'\
                    'Allows for different color font color and sizes. <br>' \
                    'For Word files only there is options for Headings sizes and listing items with bullets.<br><br>' \
                    'Sample Code:<br><br>' \
                    'import marianodoc as md <br>' \
                    'doc=md.new_doc()<br>'\
                    'doc.insert_line("sample line1")<br>'\
                    'doc.insert_line("sample line2")<br>'\
                    'doc.insert_line("sample line3")<br>'\
                    'doc.createPDFFile("some_name.pdf")<br>'\
                    'doc.createWordFile("some_name.docx")<br>'\
                    '<br><br><br>Note there are more features such as headings color fonts,highlighting, for more detail<br>'\
                    'doc.show_example1()<br>'\
                    'doc.show_example2()<br><br>'\
                    'If you like this library checkout my other library "MarianoInput" for getting user input<br>'\
                    '<a href="https://pypi.org/project/marianoinput/">MarianoInput</a><br><br>'\
                    'For help or feedback email marianoricoPy@gmail.com'            




# Setting up
setup(
    name="marianodoc",
    version=VERSION,
    author="Mariano Rico",
    author_email="<marianoricoPy@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["fpdf2","python-docx"],
    keywords=['MS WORD', 'PDF','Word' ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)