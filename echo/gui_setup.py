# Global imports
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from PyQt5.QtCore import QThread
from qgis.core import QgsMessageLog
from run_print_msg import main
from echo.Echo_dockwidget import WorkerThread

def run_tool(args):
    # QgsMessageLog.logMessage("Did it reload???", "TEST")
    main(args)


def setup_buttons(ui):

    def configure_setup():
        ui.pushButton.clicked.connect(lambda: browse_files(ui.lineEdit, "Select file"))
        ui.okcancel.clicked.connect(execute)

    def browse_files(widget_tag, browser_text="Select File", filter_ext=None):
        file = QFileDialog.getOpenFileName(None, browser_text, filter=filter_ext)
        if file[0] != "":
            widget_tag.setText(str(file[0]))

    def execute():
        my_file = ui.lineEdit.text()
        args = (my_file)

        # Launch the thread.
        ui.thread = QThread()
        ui.worker = WorkerThread(run_tool, args)
        ui.worker.moveToThread(ui.thread)
        ui.thread.started.connect(ui.worker.run)
        ui.thread.start()

        # Stop the WorkerThread so user can launch it again without closing the GUI
        ui.thread.exit()

    configure_setup()
