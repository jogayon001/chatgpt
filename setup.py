import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gptchatbot",
    version="1.0.0",
    description="Chatbot Example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Flask",
        "langchain",
        "openai",
        "pypdf",
        "gradio",
        "chromadb",
        "tiktoken",
        "jina"
    ],
    entry_points={
        "console_scripts": [
            "gptchatbot=gptchatbot.chatbot:main"
        ]
    }
)