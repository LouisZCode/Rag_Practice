from langchain_community.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader

loader = TextLoader("data/love_story.txt", encoding="utf-8")
document = loader.load()



txt_loader = DirectoryLoader(
    path="data",
    glob = "**/*.txt",
    loader_cls= TextLoader,
    loader_kwargs = {'encoding' : 'utf-8'},
    show_progress=False
    )

pdf_loader = DirectoryLoader(
    path="data",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

txt_documents = txt_loader.load()
pdf_documents = pdf_loader.load()

all_docs = txt_documents + pdf_documents
print(all_docs)
