# Project Title

Python script to find and replace version element from provided pom.xml to match the required pattern. 

## Getting Started

The script can be executed within a container. 


### Prerequisites

Docker CLI latest version

```
# Build docker image 
docker build . -t devopts:latest

#Run
docker run -it -v [Folder_Code]:/usr/src/app devopts:latest

#Build test image
docker build . -f Dockerfiletest -t devopts:test

```

## Running the tests

Unit testing can also executed within a docker container


```
#Run test
docker run -it -v [Folder_Code]:/usr/src/app devopts:test
```

## Versioning

1.0

## Authors

* **Huy Nguyen** )


## License

N/A

## Acknowledgments


