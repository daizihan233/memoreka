import setuptools
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="moa",
    version="0.2.24.1",
    author="KuoHu",
    author_email="hantools@foxmail.com",
    description="秒花笔记API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daizihan233/moa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests']
)