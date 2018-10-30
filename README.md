# Tanamin

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

### Preprocessing phase
 1. Dapet data
 2. Data nya harus di scale supaya ngitungnya cepet

### Main Phase
 1. Bikin objects:
    - Province(name: string, luas: int, color: Color=None)
    - Graph (jadi constraint graph): dict of Province
    - Color(hex: str, crop: str)
  2. Bikin database model (1 tabel yang berisi 2 field, yaitu Nama dan Luas)
  3. Bikin algoritma untuk arc consistency (constraint propagation)
  4. Bikin algorithm untuk backtrack search

### To Be Continued