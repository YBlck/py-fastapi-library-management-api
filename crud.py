from sqlalchemy.orm import Session

import schemas
from db import models


def get_author_list(
    db: Session, skip: int = 0, limit: int = 5
) -> list[models.Author]:
    db_authors = db.query(models.Author).offset(skip).limit(limit).all()

    return db_authors


def get_author_count(db: Session) -> int:
    return db.query(models.Author).count()


def get_author_by_id(db: Session, author_id: int) -> models.Author | None:
    return db.query(models.Author).filter_by(id=author_id).first()


def create_author(db: Session, author: schemas.AuthorCreate):
    new_author = models.Author(
        name=author.name,
        bio=author.bio,
    )

    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    return new_author
