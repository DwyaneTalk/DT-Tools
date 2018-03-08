#!/bin/bash

inList=$1
outPath=$2

rm -rf $outPath
mkdir -p $outPath

while read line;
do
    echo $line
    convert -flop $line $outPath/${line//\//#}
done <$inList
