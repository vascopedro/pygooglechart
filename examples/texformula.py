#!/usr/bin/env python
"""
Copyright Vasco Pedro 2011

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import urllib

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, '..'))

from pygooglechart import TexFormula

import settings
import helper

def get_formula_image():
    """
    Data from http://indexed.blogspot.com/2007/08/real-ultimate-power.html
    """
    chart = TexFormula()
    formula = "\Large\mathbb{Q}+\lim_{x\to3}\frac{1}{x}"
    encoded_formula = urllib.quote(formula)
    chart.formula = encoded_formula
    chart.download('tex.png')

def main():
    get_formula_image()

if __name__ == '__main__':
    main()


