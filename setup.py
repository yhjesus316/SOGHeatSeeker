from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SOGHeatSeeker",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Advanced surveillance monitoring toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourname/sogheatseeker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "opencv-python",
        "flask",
        "requests",
        "schedule",
        "pyautogui",
        "psutil",
    ],
    entry_points={
        "console_scripts": [
            "sogheatseeker=sog_heatseeker.core:main",
        ],
    },
)
