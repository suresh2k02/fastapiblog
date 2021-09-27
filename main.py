from fastapi import FastAPI, Depends, status, Response, HTTPException
import schemas
import models
import database
from sqlalchemy.orm import Session


models.Base.metadata.create_all(database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post('/blog')
# def create(title, body):
#     return {'title':title, 'body':body}

@app.post('/blog', status_code=201)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    print(db)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def get_all(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog

@app.get('/blog/{id}')
def get_single_blog(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {id} is not available'}
    return blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'Blog with id {id} not available...please give proper id')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': f'Blog with id {id} deleted succesfully'}

@app.put('/blog/{id}', status_code=status.HTTP_200_OK)
def update_blog(id, request: schemas.Blog,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not available.')
    blog.update(request)
    db.commit()
    return 'updated'
