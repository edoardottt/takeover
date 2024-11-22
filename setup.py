from setuptools import setup

setup(
    name="takeover",
    version="0.2",
    description="Sub-Domain TakeOver Vulnerability Scanner",
    url="https://github.com/edoardottt/takeover",
    author="edoardottt",
    author_email="edoardott@gmail.com",
    license="MIT",
    scripts=["takeover.py"],
    install_requires=[
        "requests",
        "urllib3",
    ],
    entry_points={
        "console_scripts": ["takeover=takeover:main"],
    },
    zip_safe=False,
)
