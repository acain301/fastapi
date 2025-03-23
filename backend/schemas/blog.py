from typing import Optional
from pydantic import BaseModel, model_validator, PastDatetime
from datetime import date
from slugify import slugify



class CreateBlog(BaseModel):
    title: str 
    # slug: str 
    content: Optional[str] = None 
    
    @model_validator(mode='before')
    def generate_slug(cls, values):
        if 'title' in values:
            values['slug'] = slugify(values.get("title"))
        return values

        
class ShowBlog(BaseModel):
    title:str 
    content: Optional[str]
    created_at: PastDatetime

    class Config():
        orm_mode = True