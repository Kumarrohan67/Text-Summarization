import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_discription =f.read()
__version__ ="0.0.0"

REPO_NAME = "Text-Summarization"
AUTHOR_USER_NAME ="Kumarrohan67"
SRC_REPO = "textSummarizer"
AUTHOR_EAIL ="rohansinghchouhan2gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EAIL,
    description="A small python package for NLP app",
    long_description=long_discription,
    long_description_content_type="text/markdown",
    url="https://github.com/"+AUTHOR_USER_NAME+"/"+REPO_NAME,
    project_urls={
        "Bug Tracker": "https://github.com/"+AUTHOR_USER_NAME+"/"+REPO_NAME+"/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)