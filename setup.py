import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="live-coder",
    version="0.0.116",
    author="Fraser Greenlee",
    author_email="frassyg@gmail.com",
    description="Snoop wrapper for Live Coder, should be used with the Live Coder VSCode extension.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Fraser-Greenlee/live-coding/tree/server",
    packages=['live_coder'],
    install_requires=[
        'snoop==0.3.0'
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
