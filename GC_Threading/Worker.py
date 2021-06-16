# Project Name:
# Glass Carbide
#
# By:
# Michael Gailling
# &&
# Mustafa Butt
#
# Organization:
# WIMTACH
#

from math import floor

from PySide2.QtCore import QRunnable, Slot, QObject, Signal

from GC_Services import pcloudAPI
from GC_Services.FileIo import FileIo
from GC_Services.pcloudAPI import PCloud


class DownloadWorkerSignals(QObject):
    '''
    DownloadWorkerSignals
        Defines the signals available from a running worker thread.

        Supported signals are:

        progress
            returns percent as an integer
        finished
            No data
    '''
    update_progress = Signal(int)
    finished = Signal()


class DownloadWorker(QRunnable):
    '''
    Download Worker Thread

        Summary:
            A class for DownloadWorker that includes:

            -{Description}

        Attributes:
            file_metadata, apic, apic.set_region, fio, signals

        Methods:
            run

        Attributes
        ----------
            file_metadata : !!!!!!!!!!!
                Metadata of  !!!!!
            apic : PCloud
                PCloud API class
            fio : FileIo
                File input/output
            signals : DownloadWorkerSignals
                DownloadWorkerSignals for signals from running worker threads

        Methods
        -------
            run(self)
                !!! Multithreads downloads
    '''

    def __init__(self, file_metadata=[], fio=FileIo()):
        """
            Constructs all the necessary attributes for the PCloudFileModel object.

                Parameters
                ----------
                    self
                    file_metadata
                        Metadata for file
                    fio
                        FileIo for file input/output
        :param file_metadata:
        :param fio:
        """
        super(DownloadWorker, self).__init__()

        self.file_metadata = file_metadata

        self.apic = PCloud()
        self.apic.set_region("NA")
        self.fio = fio

        self.cancel = False
        self.signals = DownloadWorkerSignals()

    def cancel_download(self):
        self.cancel = True

    @Slot()
    def run(self):
        num_processed = 0
        num_of_files = len(self.file_metadata)
        progress = 0
        self.signals.update_progress.emit(progress)

        for file_data in self.file_metadata:
            if not self.cancel:
                if not file_data.ignore:
                    print(f"Downloading: {file_data.name}")

                    code = file_data.publink_code
                    file_id = file_data.fileid

                    download_data = self.apic.get_pub_link_download(code, file_id)
                    download_link = f"http://{download_data['hosts'][0]}{download_data['path']}"
                    downloaded_file = self.apic.download_file(download_link)

                    file_type = file_data.file_type
                    dir_path = ""

                    if file_type == "audio":
                        dir_path = self.fio.sound_dir
                    elif file_type == "video":
                        dir_path = self.fio.animatic_dir
                    elif file_type == "image":
                        dir_path = self.fio.asset_dir

                    self.fio.save_file_to_dir(dir_path, file_data.name, downloaded_file)
            else:
                break

            num_processed += 1
            progress = floor((num_processed / num_of_files) * 100)
            self.signals.update_progress.emit(progress)

        self.signals.finished.emit()
