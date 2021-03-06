# fabrics-drape-data
Open exchange format for storing material parameters of textile structures for drape simulations

## Introduction
This repository consists of example files and python code for operating with related mechanical parameters of textile fabrics for clothing simulation. The drape simulation is used mainly in the clothing development, but applied as well in the composites draping. There are various CAD programs which perform drape simulation and each of these uses its own set of parameters for the characterisation of the fabrics and its own formats for their storage.
The goal of the current repository and format is to allow collection of all relevant characteristings of the textile materials for the draping and after that to allow exctration of required parameters for the different programs. 

The format is **open** and is proposed in two variants: XML and JSON, so that can be included in both types of files without additional conversions. 

The initial version of the data structure description and the scientific background for the selection of the parameters is published in the paper *"Kyosev,Y., Material description for textile draping simulation: data structure, open data exchange formats and system for
automatic analysis of experimental series"*, published in [Textile Research Journal](https://doi.org/10.1177/00405175211061192)

The repository consists of subfolder for examples (samples), python code for writing and reading data, example of extracted files. 

## Format structure

### Weight and thickness

### Tensile behaviour

### Shear behaviour

### Bending behaviour

## Python Library

## Examples