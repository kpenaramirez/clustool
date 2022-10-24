# Clustool
App for clustering data using unsupervised machine learning.

![image](assets/screenshot.png)

## How to run the App
1. `pip install -r requirements.txt`
2. `python main.py`
3. Go to http://0.0.0.0:8000/


## How to build and run the App using docker

```docker build -t clustool .```  

```docker run -d -p 8000:8000 clustool```

## Other useful docker commands for reference

To check if running:
```docker ps```

To stop a container:
```docker stop <container id>```

To delete a container:
```docker rm <container id>```

To delete an image:
```docker rmi <image id>```

Delete all previous images: 
```docker rmi -f $(docker images -aq)```

## Notes

- EDGMM algorithm from [Holoien, Marshall, & Wechsler (2016)](http://adsabs.harvard.edu/abs/2016arXiv161100363H), link to the code repository: **https://github.com/tholoien/XDGMM**. Not compatible with Python 3.

- pyUPMASK [Pera, Perren, & Moitinho (2021)](https://www.aanda.org/articles/aa/abs/2021/06/aa40252-20/aa40252-20.html). Code repository: **https://github.com/msolpera/pyUPMASK**. Not implemented in a sklearn-like fashion.
