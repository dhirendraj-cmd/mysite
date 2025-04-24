from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "This is home page"
    }

@router.get("/about")
def about():
    return {
        "message": "This is About me Page"
    }

@router.get("/contact")
def contact():
    return {
        "message": "This is contact page"
    }

@router.get("/services")
def services():
    return {
        "message": "This is services page"
    }

@router.get("/experience")
def experience():
    return {
        "message": "This is experience page"
    }

@router.get("/social")
def social():
    return {
        "message": "This is social page"
    }
