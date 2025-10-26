FNAME=main
OUTNAME=eis_basics
TEX=pdflatex
BIB=biber
VIEWER=sumatrapdf 
NCL=makeindex
BUILD_FOLDER=build
SRC_FOLDER=src
BIN_FOLDER=pdf

.PHONY: all dirs tex biber index link copy clean

all: dirs tex biber link copy

dirs:
	mkdir -p $(BUILD_FOLDER)
	mkdir -p $(BIN_FOLDER)

tex:
	$(TEX) -output-directory=./$(BUILD_FOLDER) -synctex=1 ./src/$(FNAME).tex
	
biber:
	$(BIB) ./$(BUILD_FOLDER)/$(FNAME).bcf --output-file ./$(BUILD_FOLDER)/$(FNAME).bbl

link:
	$(TEX) -output-directory=./$(BUILD_FOLDER) -synctex=1 ./src/$(FNAME).tex
	$(TEX) -output-directory=./$(BUILD_FOLDER) -synctex=1 ./src/$(FNAME).tex

index: 
	$(NCL) ./$(BUILD_FOLDER)/$(FNAME).nlo -s nomencl.ist -o ./$(BUILD_FOLDER)/$(FNAME).nls

copy: 
	cp -rf $(BUILD_FOLDER)/$(FNAME).pdf $(BIN_FOLDER)/$(OUTNAME).pdf

clean:
	rm -rf $(BUILD_FOLDER)/*
	rm -rf $(BIN_FOLDER)/*
