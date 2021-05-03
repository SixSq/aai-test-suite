#!/bin/bash -xe

for release_script in `ls */container-release.sh`
do
  pushd $(echo $release_script | awk -F'/' '{print $1}')
  ./container-release.sh
  popd
done
