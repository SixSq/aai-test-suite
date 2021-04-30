#!/bin/bash -xe

for release_script in `ls */container-release.sh`
do
  ./$release_script
done
