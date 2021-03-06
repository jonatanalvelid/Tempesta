# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:19:31 2015

@author: Barabas, Bodén, Masullo
"""
from pyqtgraph.Qt import QtGui
import nidaqmx
import sys

from control import control
import control.instruments as instruments


def main():

    app = QtGui.QApplication([])

    cobolt = 'cobolt.cobolt0601.Cobolt0601_f2'
    with instruments.Laser(cobolt, 'COM10') as actlaser, \
            instruments.PZT(8) as pzt, instruments.Webcam() as webcam:

        offlaser = instruments.LinkedLaserCheck(cobolt, ['COM4', 'COM7'])
        exclaser = instruments.LaserTTL(0)
        cameras = instruments.Cameras(0)
        print(actlaser.idn)
        print(exclaser.line)
        print(offlaser.idn)

        nidaq = nidaqmx.system.System.local().devices['Dev1']
        win = control.TormentaGUI(actlaser, offlaser, exclaser, cameras,
                                  nidaq, pzt, webcam)
        win.show()

        sys.exit(app.exec_())
