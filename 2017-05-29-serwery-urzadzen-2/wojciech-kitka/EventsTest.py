# -*- coding: utf-8 -*-
#
# This file is part of the EventsTest project
#
#
#
# Distributed under the terms of the LGPL license.
# See LICENSE.txt for more info.

""" EventsTest

Switches between valid and invalid attribute`s values.
"""

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command, device_property
from PyTango import AttrQuality, DispLevel, DevState
from PyTango import AttrWriteType
# Additional import
# PROTECTED REGION ID(EventsTest.additional_import) ENABLED START #
from time import time
from PyTango import AttributeProxy
# PROTECTED REGION END #    //  EventsTest.additional_import

__all__ = ["Pu", "main"]


class EventsTest(Device):
    """
    Switches beetwen valid and invalid attribute`s values.
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(EventsTest.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  EventsTest.class_variable

    # -----------------
    # Device Properties
    # -----------------

    DeviceName = device_property(
        dtype='str',
    )

    # ----------
    # Attributes
    # ----------

    Max = attribute(
        dtype='double',
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        # PROTECTED REGION ID(EventsTest.init_device) ENABLED START #
        self.set_state(DevState.ON)
        self.proxy = AttributeProxy(self.DeviceName)
        # PROTECTED REGION END #    //  EventsTest.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(EventsTest.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  EventsTest.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(EventsTest.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  EventsTest.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_Max(self):
        # PROTECTED REGION ID(EventsTest.Attribute1_read) ENABLED START #
        value = self.proxy.read().value
        maximums = []
        for row in value:
            maximums.append(max(row))
        value = max(maximums)
        attr_quality = AttrQuality.ATTR_ALARM
        self.push_change_event("Max", float(value), time(), attr_quality)
        self.push_archive_event("Max", float(value), time(), attr_quality)
        return float(value), time(), attr_quality
        # PROTECTED REGION END #    //  EventsTest.Attribute1_read

    # --------
    # Commands
    # --------



        # PROTECTED REGION END #    //  EventsTest.SwitchInvalid


# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(EventsTest.main) ENABLED START #
    return run((EventsTest,), args=args, **kwargs)
    # PROTECTED REGION END #    //  EventsTest.main

if __name__ == '__main__':
    main()