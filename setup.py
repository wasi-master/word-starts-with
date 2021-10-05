import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wsw",
    version="0.1.0",
    author="Wasi Master",
    author_email="arianmollik323@gmail.com",
    description="A command line tool to easily check what words start with certain characters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/wasi-master/word-starts-with/issues",
        "Source": "https://github.com/wasi-master/word-starts-with",
        "Say Thanks": "https://saythanks.io/to/arianmollik323@gmail.com",
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Terminals",
    ],
    keywords=["startswith", "starts with", "word", "starts", "with", "wsw"],
    packages=["wsw"],
    python_requires=">=3.6",
    install_requires=["rich"],
    entry_points={
        "console_scripts": ["wsw=wsw.__main__:run"],
    },
)
