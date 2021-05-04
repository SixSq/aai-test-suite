# AAI test for SixSq's Nuvla service

This test is fully automated and packaged as an executable Docker Image.

## Requirements

 - Docker
 
## Build

You can find this test already packaged as a Docker Image in Docker Hub, with the name `sixsq/aai-test-sixsq-nuvla`. 

If you want nevertheless to build your own image, simple run (from this directory):

`docker build -t <image-name> .`
 
## Run the test

To run the test, use the Docker Image from above and simply do:

```
VERSION=1.0.0    # there are other versions available

docker run --rm -v $(pwd)/output:/opt/output \
    sixsq/aai-test-sixsq-nuvla:$VERSION \
    --username <test-user> \
    --password <test-password>
    
# replace <test-user> and <test-password> by the user credentials to be used for the test. The default <test-user> is "ocre-test"
```

## Results

On success you'll have a bash exit code equal to 0 (1 otherwise). The test reports can be found, both as HTML and JSON files, at `$(pwd)/output`. 
