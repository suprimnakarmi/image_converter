from setuptools import setup

setup(
    name="image_conversion",
    version="0.1.0",
    author = "Suprim Nakarmi",
    author_email = "suprimnakarmi@gmail.com",
    description="Packages that converts image format into other format. It is sometimes required for further proceed using machine learning models",
    install_requires =[
        "pillow_heif==0.20.0",
        "pillow=11.0.0"
    ]
)
