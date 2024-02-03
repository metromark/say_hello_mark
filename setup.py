from setuptools import setup, find_packages

setup(
  name="say_hello_mark",
  version="0.5",
  author="Mark Toledo",
  author_email="mark@onebyzero.ai",
  url="www.google.com",
  packages=find_packages(),
  install_requires=[
  long_description="Test long description",
  long_description_content_type='text/markdown'
  ],
  entry_points={
    "console_scripts": [
      "say-hello-mark = say_hello_mark:hello" 
    ]
  }
)