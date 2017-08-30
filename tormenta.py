# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:19:31 2015

@author: Barabas, Bodén, Masullo
"""
from pyqtgraph.Qt import QtGui
import nidaqmx

from control import control
import control.instruments as instruments


def main():

    app = QtGui.QApplication([])

    cobolt = 'cobolt.cobolt0601.Cobolt0601'

    # NI-DAQ channels configuration
    DO = {'405': 0, '473': 1, '488': 2, 'CAM': 3}
    AO = {'x': 0, 'y': 1, 'z': 2}
    outChannels = [DO, AO]
    nidaq = nidaqmx.system.System.local().devices['Dev1']

    with instruments.Laser(cobolt, 'COM4') as violetlaser, \
            instruments.Laser(cobolt, 'COM13') as exclaser, \
            instruments.Laser(cobolt, 'COM6') as offlaser:
#        offlaser = instruments.LinkedLaserCheck(cobolt, ['COM6', 'COM4'])
        orcaflashV3 = instruments.Camera(0)
        orcaflashV2 = instruments.Camera(1)
        print(violetlaser.idn)
        print(exclaser.idn)
        print(offlaser.idn)

        win = control.TormentaGUI(violetlaser, exclaser, offlaser, orcaflashV2,
                                  orcaflashV3, nidaq, outChannels)
        win.show()

        app.exec_()
