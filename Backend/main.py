from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import uvicorn
from RevSearchEngine.SearchEngine import ImageSearchEngine
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SimilarImagesResponse(BaseModel):
    similar_images: list


@app.get("/")
def index():
    return {"status": "ok"}


@app.post("/search-similar-images", response_model=SimilarImagesResponse)
async def search_similar_images(
    image: UploadFile = File(...), number_of_images: int = 3
):
    try:
        # convert to PIL Image
        image = Image.open(image.file)

        # Create an instance of ImageSearchEngine with the necessary configurations
        MODEL_PATH = "Backend/models/feature_encoder.onnx"
        MODE = "search"
        IMAGES_DIR = "/home/ibad/Desktop/RevSearch/Car196_Combined/images/"
        METADATA_DIR = "Backend/cars_dataset_metadata_dir"
        FEATURE_EXTRACTOR_NAME = "efficientnet_onnx"

        image_search_engine = ImageSearchEngine(
            model_path=MODEL_PATH,
            images_dir=IMAGES_DIR,
            mode=MODE,
            metadata_dir=METADATA_DIR,
            feature_extractor_name=FEATURE_EXTRACTOR_NAME,
        )

        similar_images = image_search_engine.get_similar_images_list_from_image(
            image=image, number_of_images=number_of_images
        )

        return {"similar_images": similar_images}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
