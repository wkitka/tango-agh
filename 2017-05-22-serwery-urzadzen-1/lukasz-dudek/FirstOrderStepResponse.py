# -*- coding: utf-8 -*-
#
# This file is part of the FirstOrderStepResponse project
#
# 
#
# Distributed under the terms of the LGPL license.
# See LICENSE.txt for more info.

""" FirstOrder

This is a sample DS for simulating a step response of a first-order intertial object.
"""

__all__ = ["FirstOrderStepResponse", "main"]

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango.server import class_property, device_property
from PyTango import AttrQuality, AttrWriteType, DispLevel, DevState
# Additional import
# PROTECTED REGION ID(FirstOrderStepResponse.additionnal_import) ENABLED START #
from scipy import signal
from numpy import arange
# PROTECTED REGION END #    //  FirstOrderStepResponse.additionnal_import


class FirstOrderStepResponse(Device):
    """
    This is a sample DS for simulating a step response of a first-order intertial object.
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(FirstOrderStepResponse.class_variable) ENABLED START #
    amplification = 1.0
    time_constant = 1.0
    output = [0.0]
    # PROTECTED REGION END #    //  FirstOrderStepResponse.class_variable
    # ----------------
    # Class Properties
    # ----------------

    # -----------------
    # Device Properties
    # -----------------

    TimeRange = device_property(
        dtype='str',
    )

    # ----------
    # Attributes
    # ----------

    TimeConstant = attribute(
        dtype='double',
        access=AttrWriteType.READ_WRITE,
    )

    Amplification = attribute(
        dtype='double',
        access=AttrWriteType.READ_WRITE,
    )

    Output = attribute(
        dtype=('double',),
        max_dim_x=10000,
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        # PROTECTED REGION ID(FirstOrderStepResponse.init_device) ENABLED START #
        self.set_state(DevState.ON)
        self.set_status("First Order working!")
        # PROTECTED REGION END #    //  FirstOrderStepResponse.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(FirstOrderStepResponse.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  FirstOrderStepResponse.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(FirstOrderStepResponse.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  FirstOrderStepResponse.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_TimeConstant(self):
        # PROTECTED REGION ID(FirstOrderStepResponse.TimeConstant_read) ENABLED START #
        return self.time_constant
        # PROTECTED REGION END #    //  FirstOrderStepResponse.TimeConstant_read

    def write_TimeConstant(self, value):
        # PROTECTED REGION ID(FirstOrderStepResponse.TimeConstant_write) ENABLED START #
        self.time_constant = value
        # PROTECTED REGION END #    //  FirstOrderStepResponse.TimeConstant_write

    def read_Amplification(self):
        # PROTECTED REGION ID(FirstOrderStepResponse.Amplification_read) ENABLED START #
        return self.amplification
        # PROTECTED REGION END #    //  FirstOrderStepResponse.Amplification_read

    def write_Amplification(self, value):
        # PROTECTED REGION ID(FirstOrderStepResponse.Amplification_write) ENABLED START #
        self.amplification = value
        # PROTECTED REGION END #    //  FirstOrderStepResponse.Amplification_write

    def read_Output(self):
        # PROTECTED REGION ID(FirstOrderStepResponse.Output_read) ENABLED START #
        return self.output
        # PROTECTED REGION END #    //  FirstOrderStepResponse.Output_read

    # --------
    # Commands
    # --------

    @command
    @DebugIt()
    def CalculateResponse(self):
        # PROTECTED REGION ID(FirstOrderStepResponse.CalculateResponse) ENABLED START #
        try:
            h_times = arange(0.0, float(self.TimeRange), 1)
            sys = signal.lti(self.amplification, [1, 1.0 / self.time_constant])
            step_response = sys.step(T=h_times)[1]
            self.output = step_response
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.set_status("Exception caught in CalculateResponse:\n%s" % e)
        # PROTECTED REGION END #    //  FirstOrderStepResponse.CalculateResponse

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    from PyTango.server import run
    return run((FirstOrderStepResponse,), args=args, **kwargs)

if __name__ == '__main__':
    main()
