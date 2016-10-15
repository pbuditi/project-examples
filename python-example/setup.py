try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    description="An example of how to create and publish to pypi.org",
    author="Michal Reuven",
    author_email="michal@jfrog.com",
    url="http://localhost:8081/artifactory/project-example/project-python",
    version="0.1",
    install_requires=["nose",],
    packages=["pythonProj","tests",],
    name="pythonProj",
)
