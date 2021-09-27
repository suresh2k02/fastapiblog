from fastapi import FastAPI
from  pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/blog")
def index(limit=10, published: bool=True):
    if published:
        return {"data": f'{limit} published blogs'}
    else:
        return {"data": f"{limit} non-published blogs from db"}
    return {"data": f"{limit} blogs from db"}

@app.get("/unpublished")
def unpublished():
    return {'data': 'unpublished'}

@app.get("/{id}")
def get_blog(id: int):
    return {'data':id}

@app.get("blog/{id}/comments")
def get_blog(id: int):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post("/blog")
def post_blog(blog: Blog):
    return {'data':f'Blog created as title {blog.title}'}

# def get(request):
#     if request.method=="GET":
#         data = Audit.objects.all()
#         serializer = AuditSerializer(data)
#         return serializer.data
#     elif request.method=="POST":
#         serializer = AuditSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


# def audit_detail(request):
#     try:
#         data = Audit.objects.get(id=pk)
#     except Audit.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method=="PUT":
#         serialzer = AuditSerializer(data, data=request.data)
#         if serialzer.is_valid():
#             serialzer.save()
#             return Response(data="update successfull")
#         return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "GET":
#         serialzer = AuditSerializer(data)
#         return Response(serialzer.data, )
#     elif request.method=="DELETE":
#         data.delete()
#         return Response({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# def delete(self, request, pk, format=None):
#     try:
#         data = Audit.objects.get(id=pk)
#     except Audit.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     data.delete()
#     return Response({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 