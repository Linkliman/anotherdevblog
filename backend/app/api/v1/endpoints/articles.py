from fastapi import APIRouter, HTTPException
from app.db.models import Article, Tag
from app.db.session import SessionLocal
from app.schemas.schemas import ArticleCreate

router = APIRouter()

@router.get("/")
def get_articles(search: str = None, page: int = 1, limit: int = 10):
    db = SessionLocal()
    articles = db.query(Article).filter(
        Article.title.ilike(f"%{search}%") if search else True
    ).offset((page - 1) * limit).limit(limit).all()
    return articles

@router.get("/{id}")
def get_article(id: int):
    db = SessionLocal()
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.post("/")
def create_article(article: ArticleCreate):
    db = SessionLocal()
    db_article = Article(**article.dict(exclude={"tags"}))
    for tag_name in article.tags:
        tag = db.query(Tag).filter(Tag.name == tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
        db_article.tags.append(tag)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
