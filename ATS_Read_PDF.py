import pdfreader
from io import BytesIO
from pdfreader import PDFDocument , SimplePDFViewer

def Read_PDF_File(FileName):
    fd = open(file=FileName,mode="rb")
    seperator = "-"*90
    viewer = SimplePDFViewer(fd)
    print(seperator)
    print("Data from 1st page is: ")
    print(seperator)
    viewer.navigate(1)
    viewer.render()
    print("Length is:",len(viewer.canvas.strings))

    for line in range(0,len(viewer.canvas.strings),1):
        
        print(viewer.canvas.strings[line])
    

    print(seperator)
    print("Data from page 2: ")
    print(seperator)
    """
    viewer.navigate(2)
    viewer.render()
    print("Length is:",len(viewer.canvas.strings))

    for line in range(0,len(viewer.canvas.strings),1):
        if(viewer.canvas.strings[line] == "Python"):
            print(viewer.canvas.strings[line]) 
    """
def main():
    Filename = "ResumeKD.pdf"
    Read_PDF_File(FileName=Filename)

if __name__ == "__main__":
    main()

"""
doc = PDFDocument(fd)

    with open(FileName,"rb") as fd:
        stream = BytesIO(fd.read())
    doc2 = PDFDocument(stream)

    print("PDF version of the document: ",doc.header.version)

    print("PDF meta data is: ",doc.metadata)

    print("Document root is: ",doc.root.Type)
    
    #print(doc.root.Outlines.First['Title'])

    pages = [p for p in doc.pages()]
    print("Pages in PDF is:",len(pages))

"""