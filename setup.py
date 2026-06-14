from setuptools import setup, find_packages

setup(
    name="vectoreek",
    version="0.1.0",
    packages=find_packages(),
    author="Vectoreek Team",
    description="Mechanical Symbionts & Parasitic AI Engine",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Robotics",
    ],
    python_requires='>=3.8',
)
