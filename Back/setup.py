from setuptools import setup, find_packages

setup(
    name="moreeducation",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "pydantic>=1.8.0",
        "python-dotenv>=0.19.0",
        "scikit-learn",
        "pyttsx3",
        "pytesseract"
    ],
    python_requires=">=3.8",
)