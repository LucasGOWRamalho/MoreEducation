from setuptools import setup, find_packages

setup(
    name="moreeducation",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "opencv-python>=4.5.0",
        "numpy>=1.21.0",
        "pydantic>=1.8.0"
    ],
    python_requires=">=3.8",
    include_package_data=True,
)