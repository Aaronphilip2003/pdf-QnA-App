from django.shortcuts import render
from django.http import HttpResponse
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from django.http import JsonResponse



def say_hello(request):
    return render(request,"hello.html ")

def home(req):
    return render(req,'home.html')


def remove_special_characters(text_list):
    special_chars = ["[", "]", "\\", "\n"]
    for char in special_chars:
        text_list = [text.replace(char, "") for text in text_list]
    return text_list

def norwegian_wood(request):
    embedding2 = HuggingFaceEmbeddings()
    vdb_chunks_HF = FAISS.load_local("query/vdb_chunks_HF", embedding2, index_name="indexHF")
    query = request.GET.get('query', '')
    print(query)
    ans = vdb_chunks_HF.as_retriever().get_relevant_documents(query)

    # Assuming ans is a list of documents and you want to return the first document's page content
    answer = ans[0].page_content if ans else "No answer found."

    # Return the answer directly as a JSON response
    return JsonResponse({'answer': answer})