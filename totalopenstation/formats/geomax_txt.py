# -*- coding: utf-8 -*-
# filename: formats/topcon_gts.py
# Copyright 2021 ENZO COCCA <enzo.ccc@gmail.com>

# This file is part of Total Open Station.
#
# Total Open Station is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Total Open Station is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Total Open Station.  If not, see
# <http://www.gnu.org/licenses/>.

from . import Feature, Parser, Point


class FormatParser(Parser):
    
   
    def is_point(self, line) :

        return True
            
    
    def get_point(self, line):
        
        line = line.replace(',','          ')

        try:    
            
            id = str(line[0:14])
            desc= str(line[0:14])
            y = float(line[14:30])  # Northing
            x = float(line[30:46])   # Easting
            z = float(line[46:-1]) # Elevation
                   
            
            point = Point(x, y, z)
            feature = Feature(point,desc=desc,id=id)
            return feature
        except Exception as e:
            print(e)
    