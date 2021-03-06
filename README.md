# django rest framework demo

## Features

This app is able to to following operations,

- List all articles
- Create new article
- Update existing article
- Delete article
- list all tags

## API's

- api/articles  LIST ALL ARTICLES WITH TAGS
- api/articles/5 FETCH SINGLE ARTICLE WITH TAGS
- api/articles  CREATE ARTICLE WITH TAGS
- api/articles/4 UPDATE ARTICLE WITH TAG
- api/articles/3 DELETE ARTICLE (NOT DELETING ANY TAG, MIGHT BE USING ANOTHER ARTICLE)
- api/tags LIST ALL TAGS
- 

## Model's

- Article
    1. Title
    2. Description
    3. Publish_date
    4. Author_name
- Tag
    1. Name
    2. FK -> Article
