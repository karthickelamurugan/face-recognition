# face-recognition

with the help of https://pypi.org/project/face-recognition/ project, identifing users faces by comparing with existing photo of the same user.
This algorithm compare our webcam captured face with our existing phto

Things required

Web camera
Visual studio (especially for installing dlib packages)
python latest version

commands for installing face-recognition project

**pip install face-recognition


issues faced during installing 
https://stackoverflow.com/a/71220610/15495975

->  Try installation using wheel packages 
    Even it gets failed due to platform unsupport, please try the below options
->  Try to installing the source files from https://pypi.org/project/dlib/#files and run **pip setup.py install** by placing into the site packages
    If its shows any ssize_t variable issue in numpy, please declare a local variable ssize on the top of the file
    https://stackoverflow.com/questions/70046641/i-am-unable-to-install-face-recognition-library

I hope now your dlib libraries will get install without any errors





