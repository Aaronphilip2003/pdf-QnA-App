from django.shortcuts import render
from django.http import HttpResponse
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def say_hello(request):
    return render(request,"hello.html ")

def home(req):
    return render(req,'home.html')


def norwegian_wood(request):
    embedding2 = HuggingFaceEmbeddings()
    vdb_chunks_HF = FAISS.load_local("query/vdb_chunks_HF", embedding2, index_name="indexHF")
    query = request.GET.get('query', '')
    print(query)
    ans = vdb_chunks_HF.as_retriever().get_relevant_documents(query)
    result = ans[0].page_content if ans else None
    
    # Pass the 'result' variable to the template for display
    return render(request, "norwood.html", {'result': result})