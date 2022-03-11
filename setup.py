from distutils.core import setup

setup(
    name="owl_augmentator",
    version="0.1",
    description="Augmentator library for OWLReady2",
    author ="Lukas Westhofen",
    author_email="lukas.westhofen@offis.de",
    py_modules=["owl_augmentator"],
    install_requires=["owlready2"]
    )
