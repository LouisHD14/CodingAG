<<<<<<< HEAD
from fastapi import FastAPI, Response
import requests
import random

app = FastAPI()

@app.get("/")
async def read_root():
    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=subject:fantasy&oderBy=relevance&filter=ebooks&key=AIzaSyB2CUkXUdxvolvivYFxgxmmPi7diqy2DRU")
    data = response.json()
    items = data.get('items')
    if items is None:
        return Response(content="<h1>No books found</h1>", media_type="text/html")
    content = ""
    for _ in range(3):
        random_book = random.choice(items)
        title = random_book['volumeInfo']['title']
        volume_info = random_book.get('volumeInfo')
        #isbn = random_book.get['volumeInfo']['isbn']
        if volume_info is None:
            content += f"<h1>{title}</h1><p>No description available</p>"
            continue
        description = volume_info.get('description')
        if description is None:
            description = "No description available"
        thumbnail = volume_info.get('imageLinks').get('thumbnail')
        if thumbnail is None:
            thumbnail = "https://via.placeholder.com/128x193.png?text=No+Image+Available"
        content += f"""
            <h1>{title}</h1>
            <img src={thumbnail} alt={title}>
            <p>{description}</p>
        """
=======
from fastapi import FastAPI, Response
import requests
import random

app = FastAPI()

@app.get("/")
async def read_root():
    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=random&key=AIzaSyB2CUkXUdxvolvivYFxgxmmPi7diqy2DRU")
    data = response.json()
    items = data.get('items')
    if items is None:
        return Response(content="<h1>No books found</h1>", media_type="text/html")
    content = ""
    for _ in range(3):
        random_book = random.choice(items)
        title = random_book['volumeInfo']['title']
        volume_info = random_book.get('volumeInfo')
        if volume_info is None:
            content += f"<h1>{title}</h1><p>No description available</p>"
            continue
        description = volume_info.get('description')
        if description is None:
            description = "No description available"
        thumbnail = volume_info.get('imageLinks').get('thumbnail')
        if thumbnail is None:
            thumbnail = "https://via.placeholder.com/128x193.png?text=No+Image+Available"
        content += f"""
            <h1>{title}</h1>
            <img src={thumbnail} alt={title}>
            <p>{description}</p>
        """
>>>>>>> 7920eb72adb12a57551f9427ba68c7b3e1e48bad
    return Response(content=content, media_type="text/html")