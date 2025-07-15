#!/bin/sh

set -xe
dir="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"
cd $dir

mkdir data
pushd data

curl -OL https://github.com/lionsoul2014/ip2region/raw/master/data/ip2region.xdb

popd
