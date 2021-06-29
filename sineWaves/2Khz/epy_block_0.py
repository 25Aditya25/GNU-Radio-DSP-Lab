"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.sineTable=[0.13053, 0.25882, 0.38268, 0.5, 0.60876, 0.70711, 0.79335, 0.86603, 0.92388, 0.96593, 0.99144, 1,   0.99144, 0.96593, 0.92388, 0.86603, 0.79335, 0.70711, 0.60876, 0.5, 0.38268, 0.25882, 0.13053, 0,  -0.13053,    -0.25882,    -0.38268,    -0.5,    -0.60876,    -0.70711,    -0.79335,    -0.86603,    -0.92388,    -0.96593,    -0.99144,    -1,  -0.99144,    -0.96593,    -0.92388,    -0.86603,    -0.79335,    -0.70711,    -0.60876,    -0.5,    -0.38268,    -0.25882,    -0.13053,    0]
        self.index=0
        self.period=24

    def work(self, input_items, output_items):
        #2Khz sine wave
        for i in range (0,len(input_items[0])):
            output_items[0][i] = self.sineTable[2*self.index]
            self.index=(self.index+1)%self.period
        return len(output_items[0])
