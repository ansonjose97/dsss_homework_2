from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    description="A simple math quiz game with basic arithmetic operations",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[],
    extras_require={
        "dev": ["pytest", "unittest"],  # for running tests during development
    },
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
