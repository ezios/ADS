#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Feb  6 14:36:31 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import epy_block_1
import pmt
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.viewtrame = viewtrame = False
        self.samp_rate = samp_rate = 8.e6
        self.rf_gain = rf_gain = 14
        self.if_gain = if_gain = 40
        self.bb_gain = bb_gain = 26

        ##################################################
        # Blocks
        ##################################################
        _viewtrame_check_box = Qt.QCheckBox("viewtrame")
        self._viewtrame_choices = {True: 1, False: 0}
        self._viewtrame_choices_inv = dict((v,k) for k,v in self._viewtrame_choices.iteritems())
        self._viewtrame_callback = lambda i: Qt.QMetaObject.invokeMethod(_viewtrame_check_box, "setChecked", Qt.Q_ARG("bool", self._viewtrame_choices_inv[i]))
        self._viewtrame_callback(self.viewtrame)
        _viewtrame_check_box.stateChanged.connect(lambda i: self.set_viewtrame(self._viewtrame_choices[bool(i)]))
        self.top_grid_layout.addWidget(_viewtrame_check_box)
        self._rf_gain_range = Range(0, 14, 14, 14, 200)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, "rf_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._rf_gain_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	256, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self._if_gain_range = Range(0, 40, 8, 40, 200)
        self._if_gain_win = RangeWidget(self._if_gain_range, self.set_if_gain, "if_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._if_gain_win)
        self.epy_block_1 = epy_block_1.blk(viewDebug=0)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(4, 2.e-3, 1.e-1, 6.e-2, 5.e-6*100)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((2, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, 'D:\\en_p\\trames_ads_raw.raw', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-250.e-3, ))
        self._bb_gain_range = Range(0, 60, 2, 26, 200)
        self._bb_gain_win = RangeWidget(self._bb_gain_range, self.set_bb_gain, "bb_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._bb_gain_win)
        self.analog_agc2_xx_0 = analog.agc2_ff(1.e-1, 1.e-2, 3.e-1, 5.e-1)
        self.analog_agc2_xx_0.set_max_gain(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.epy_block_1, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_viewtrame(self):
        return self.viewtrame

    def set_viewtrame(self, viewtrame):
        self.viewtrame = viewtrame
        self._viewtrame_callback(self.viewtrame)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
