#!/usr/bin/env bash

BUILD_DIR=build
DEP_DIR=build/dependencies
GIT="bibfiles drawings"

mkdir -p $BUILD_DIR
mkdir -p $DEP_DIR

cd $DEP_DIR

for i in $GIT;do
    url="https://github.com/MilanSkocic/$i.git"
    if [[ ! -d $i/ ]]; then 
        git clone $url; 
        if [[ $?>0 ]]; then 
            echo "The repo $i could not be retrieved."; 
        fi
    fi
done

cd ../../

url=$DEP_DIR/drawings/logo/png
target=full_bw.png
cp -fv $url/$target ./src/figures/

url=$DEP_DIR/drawings/figures/png
target=EIS-*.png
cp -fv $url/$target ./src/figures/

url=$DEP_DIR/bibfiles
target=references.bib
cp -fv $url/$target ./src/references.bib
