# Tiling-Problem-ASA

This repository contains the implementation of a project for the "Análise e Síntese de Algoritmos" course at Instituto Superior Técnico during the academic year 2022/2023.

## Problem Description
The goal of this project is to solve the tile tiling problem, which involves covering a given area defined on a rectangular grid with tiles. The area is delimited by a stair-like path, and the tiles used are squares with dimensions that are multiples of the unit size (e.g., 1 × 1, 2 × 2, etc.). The task is to find the number of distinct configurations of tiles that can completely cover the specified area.

## Input and Output
The input file for the program should follow the following format:

```
<n>                // Number of rows in the grid
<m>                // Number of columns in the grid
<c1>               // Index of the column the path passes on the 1st row
<c2>               // Index of the column the path passes on the 2nd row
...
<cn>               // Index of the column the path passes on the nth row
```

The program reads this input and writes the output to the standard output. The output consists of a single integer representing the number of distinct tile configurations that cover the given area.

## Implementation
The project was prefered be implemented in C++ or C. Submissions in Java/Python were also allowed but not recommended due to potential performance issues. However our prototype in python ended up being fast enough to beat the private tests.
