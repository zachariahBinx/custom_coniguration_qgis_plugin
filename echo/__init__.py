# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Echo
                                 A QGIS plugin
 Echo
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-04-23
        copyright            : (C) 2025 by Echo
        email                : Echo
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Echo class from file Echo.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Echo import Echo
    return Echo(iface)
