from qgis.core import QgsMessageLog

def main(msg):
    QgsMessageLog.logMessage(msg, "TEST")