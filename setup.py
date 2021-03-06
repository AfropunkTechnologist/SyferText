from setuptools import setup
from setuptools import find_packages


setup(
    name="syfertext",
    author="Alan Aboudib",
    author_email="agabudeeb@gmail.com",
    description="A privacy preserving NLP framework",
    url="https://github.com/OpenMined/SyferText",
    keywords="nlp smpc secure multi-party computation federated learning deep learning artificial intelligence secure model sharin natural language processing spacy spaCy",
    classifier=["Programming Language :: Python :: 3.6", "Operating System :: OS Independent"],
    license="Apache-2.0",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "tqdm==4.36.1",
        "mmh3==2.5.1",
        "syft @ git+https://github.com/OpenMined/PySyft@c430345b82cdcbaa7a15f8662498c502c4f9a1eb",
        "requests==2.22.0",
    ],
    extras_require={
        "test": [
            "black>=19.10b0",
            "pytest>=5.3.5",
            "pytest-black>=0.3.8",
            "jupyter>=1.0.0",
            "papermill>=1.2.1",
        ]
    },
)
