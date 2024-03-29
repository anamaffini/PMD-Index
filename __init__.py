# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PMDIndex
                                 A QGIS plugin
 This plugin calculates the Potential Movement Difference Index.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-03-15
        copyright            : (C) 2023 by Ana Maffini
        email                : analuisamaffini@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Ana Maffini'
__date__ = '2023-03-15'
__copyright__ = '(C) 2023 by Ana Maffini'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PMDIndex class from file PMDIndex.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .pmd_index import PMDIndexPlugin
    return PMDIndexPlugin()
