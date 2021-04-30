#!/bin/bash -xe

for release_script in `ls */container-release.sh`
do
  sh $release_script
done
