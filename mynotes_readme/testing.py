import marianodoc as md

#doc=md.new_doc()
#doc.show_example1()


# cd mynotes_readme
# python testing.py

import marianodoc as md
doc=md.new_doc()
doc.insert_line("sample line1")
doc.insert_line("sample line2")
doc.insert_line("sample line3")
doc.createPDFFile("some_name.pdf")
doc.createWordFile("some_name.docx")

print("Done")
