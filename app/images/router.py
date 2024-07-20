from fastapi import APIRouter, UploadFile
import shutil

from app.tasks.tasks import process_picture

router = APIRouter(
    prefix="/images",
    tags=["Image upload"]
)


@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
    img_path = f"app/static/images/{name}.webp"
    with open(img_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_picture.delay(img_path)