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
        "message": "About me"
    }

@router.get("/contact")
def contact():
    return {
        "message": "About me"
    }

@router.get("/services")
def services():
    return {
        "message": "About me"
    }

@router.get("/experience")
def experience():
    return {
        "message": "About me"
    }

@router.get("/social")
def social():
    return {
        "message": "About me"
    }
