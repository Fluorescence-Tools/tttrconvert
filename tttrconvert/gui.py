from __future__ import annotations

import sys
import copy
import os
import typing

import tttrlib

from qtpy import QtWidgets, QtGui, uic


filetypes = dict([
    ("hdf", {
        'name': "High density file",
        'ending': '.h5'
    }),
    ("bh132", {
        'name': "Becker-Hickl-132",
        'ending': '.spc',
        'nTAC': 4095,
        'nROUT': 255,
        # 'read': bh132_photons
    }),
    ("ht3", {
        'name': "PicoQuant-ht3",
        'ending': '.ht3',
        'nTAC': 65535,
        'nROUT': 255,
        # 'read': ht3_photons
    }),
    ("ht3c", {
        'name': "Suren ht3 compressed",
        'ending': '.ht3',
        'nTAC': 65535,
        'nROUT': 255,
        # 'read': ht3_sf
    }),
    ("ptu", {
        'name': "PicoQuant-PTU",
        'ending': '.ptu',
        'nTAC': 65535,
        'nROUT': 255,
        # 'read': pq_photons
    }),
    ("iss", {
        'name': "ISS-fcs",
        'ending': '.fcs',
        'nTAC': 1,
        'nROUT': 2,
        # 'read': iss_photons
    })
]
)


class FileList(QtWidgets.QListWidget):

    @property
    def filenames(self) -> typing.List[str]:
        fn = list()
        for row in range(self.count()):
            item = self.item(row)
            fn.append(str(item.text()))
        return fn

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super().dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                s = str(url.toLocalFile())
                url.setScheme("")
                if s.endswith(self.filename_ending) or \
                        s.endswith(self.filename_ending+'.gz') or \
                        s.endswith(self.filename_ending+'.bz2') or \
                        s.endswith(self.filename_ending+'.zip'):
                    self.addItem(s)
            event.acceptProposedAction()
        else:
            super().dropEvent(event)

    def __init__(
            self,
            accept_drops: bool = True,
            filename_ending: str = "*",
            icon: QtGui.QIcon = None
    ):
        """
        :param accept_drops: if True accepts files that are dropped into the list
        :param kwargs:
        """
        super().__init__()
        self.filename_ending = filename_ending
        self.drag_item = None
        self.drag_row = None

        if accept_drops:
            self.setAcceptDrops(True)
            self.setDragDropMode(
                QtWidgets.QAbstractItemView.InternalMove
            )

        if icon is None:
            icon = QtGui.QIcon(":/icons/icons/list-add.png")

        self.setWindowIcon(icon)


class TTTRConvert(QtWidgets.QWidget):

    name = "tttr-tttrconvert"

    _current_filetype = "hdf"

    @property
    def filetype(self):
        return self._current_filetype

    @property
    def ending(self):
        return filetypes[self.filetype]['ending']

    @property
    def reading_routine(self):
        return filetypes[self.filetype]['read']

    @property
    def filenames(self):
        return self.file_list.filenames

    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(
            *args,
            **kwargs
        )
        self.file_list = FileList(filename_ending=self.ending)
        # initilize UI
        uic.loadUi(
            os.path.join(
                os.path.dirname(
                    os.path.abspath(__file__)
                ),
                "tttr_convert.ui"
            ),
            self
        )

        self.comboBox.addItems(
            filetypes.keys()
        )
        self.hide()
        self.actionClear_list.triggered.connect(self.file_list.clear)
        self.actionOpen_Target.triggered.connect(self.open_target)
        self.actionEnding_changed.triggered.connect(self.ending_changed)
        self.verticalLayout.addWidget(self.file_list)

    def ending_changed(self):
        self._current_filetype = str(self.comboBox.currentText())
        self.file_list.filename_ending = self.ending

    def open_target(
            self
    ):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, "TTTR file", None, "TTTR file (*.photon.h5; *.ht3; *.ptu; *.spc)")
        self.lineEdit.setText(filename)
        tttr_files = self.filenames
        for fn in tttr_files:
            tttr = tttrlib.TTTR(fn)
            basename = os.path.splitext(os.path.basename(fn))[0]
            print(basename)
            # tttr.write()
        # h5 = chisurf.fio.fluorescence.tttr.spc2hdf(
        #     spc_files,
        #     routine_name=self.filetype,
        #     filename=filename
        # )
        # h5.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = TTTRConvert()
    win.show()
    sys.exit(app.exec_())
