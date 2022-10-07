# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
  author="Jelle Carcan",
  description="Hello world",
  name="hello-world",
  version="0.1.0",
  packages=find_packages(include=["hello_world", "hello_world.*"])
)
