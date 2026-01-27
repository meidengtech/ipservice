#!/bin/sh

set -xe
dir="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"
cd $dir

mkdir -p data
pushd data

curl -OL https://github.com/lionsoul2014/ip2region/raw/master/data/ip2region_v4.xdb
mv ip2region_v4.xdb ip2region.xdb

popd
