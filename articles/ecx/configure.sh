#!/usr/bin/env bash

url=../../../3-Resource/logo/png
target=full_bw.png
cp -fv $url/$target ./src/figures/

url=../../../3-Resource/figures/png
target=PEC-*.png
cp -fv $url/$target ./src/figures/

url=../../../3-Resource/references
target=references.bib
cp -fv $url/$target ./src/references.bib

