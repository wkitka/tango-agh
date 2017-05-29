# -*- coding: utf-8 -*-
#
# This file is part of the SwitchInvalidAttribute project
#
#
#
# Distributed under the terms of the LGPL license.
# See LICENSE.txt for more info.

""" SwitchInvalidAttribute

Switches between valid and invalid attribute`s values.
"""

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango import AttrQuality, DispLevel, DevState
from PyTango import AttrWriteType, PipeWriteType
# Additional import
# PROTECTED REGION ID(SwitchInvalidAttribute.additional_import) ENABLED START #
import re
# PROTECTED REGION END #    //  SwitchInvalidAttribute.additional_import

__all__ = ["SwitchInvalidAttribute", "main"]


class SwitchInvalidAttribute(Device):
    """
    Switches beetwen valid and invalid attribute`s values.
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(SwitchInvalidAttribute.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  SwitchInvalidAttribute.class_variable

    # ----------
    # Attributes
    # ----------

    Attribute1 = attribute(
        dtype='double',
    )

    Attribute2 = attribute(
        dtype='double',
    )

    Attribute3 = attribute(
        dtype='double',
    )

    Attribute4 = attribute(
        dtype='double',
    )

    Attribute5 = attribute(
        dtype='double',
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        # PROTECTED REGION ID(SwitchInvalidAttribute.init_device) ENABLED START #
        self.set_state(DevState.ON)
        # PROTECTED REGION END #    //  SwitchInvalidAttribute.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(SwitchInvalidAttribute.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SwitchInvalidAttribute.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(SwitchInvalidAttribute.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SwitchInvalidAttribute.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_Attribute1(self):
        # PROTECTED REGION ID(SwitchInvalidAttribute.Attribute1_read) ENABLED START #
        if self.Attribute1.get_quality() == AttrQuality.ATTR_VALID:
            return 1.0
        else:
            pass
        # PROTECTED REGION END #    //  SwitchInvalidAttribute.Attribute1_read

    def read_Attribute2(self):
        # PROTECTED REGION ID(SwitchInvalidAttribute.Attribute2_read) ENABLED START #
        if self.Attribute2.get_quality() == AttrQuality.ATTR_VALID:
            return 2.0
        else:
            pass
        # PROTECTED REGION END #    //  SwitchInvalidAttribute.Attribute2_read

    def read_Attribute3(self):
        # PROTECTED REGION ID(SwitchInvalidAttribute.Attribute3_read) ENABLED START #
        if self.Attribute3.get_quality() == AttrQuality.ATTR_VALID:
            return 3.0
        else:
            pass
        # PROTECTED REGION END #    //  SwitchInvalidAttribute.Attribute3_read

    def read_Attribute4(self):
        # PROTECTED REGION ID(SwitchInvalidAttribute.Attribute4_read) ENABLED START #
        if self.Attribute4.get_quality() == AttrQuality.ATTR_VALID:
            return 4.0
        else:
            pass
        # PROTECTED REGION END #    //  SwitchInvalidAttribute.Attribute4_read

    def read_Attribute5(self):
        # PROTECTED REGION ID(SwitchInvalidAttribute.Attribute5_read) ENABLED START #
        if self.Attribute5.get_quality() == AttrQuality.ATTR_VALID:
            return 5.0
        else:
            pass
        # PROTECTED REGION END #    //  SwitchInvalidAttribute.Attribute5_read


    # --------
    # Commands
    # --------

    @command(
    dtype_in='str',
    )
    @DebugIt()
    def SwitchInvalid(self, argin):
        # PROTECTED REGION ID(SwitchInvalidAttribute.SwitchInvalid) ENABLED START #
        #argin = re.sub(r"\s+", "", argin, flags=re.UNICODE)
        if "1" in argin:
            if self.Attribute1.get_quality() == AttrQuality.ATTR_VALID:
                print self.Attribute1.get_quality()
                self.Attribute1.set_quality(AttrQuality.ATTR_INVALID)
            else:
                self.Attribute1.set_quality(AttrQuality.ATTR_VALID)
        if "2" in argin:
            if self.Attribute2.get_quality() == AttrQuality.ATTR_VALID:
                self.Attribute2.set_quality(AttrQuality.ATTR_INVALID)
            else:
                self.Attribute2.set_quality(AttrQuality.ATTR_VALID)
        if "3" in argin:
            if self.Attribute3.get_quality() == AttrQuality.ATTR_VALID:
                self.Attribute3.set_quality(AttrQuality.ATTR_INVALID)
            else:
                self.Attribute3.set_quality(AttrQuality.ATTR_VALID)
        if "4" in argin:
            if self.Attribute4.get_quality() == AttrQuality.ATTR_VALID:
                self.Attribute4.set_quality(AttrQuality.ATTR_INVALID)
            else:
                self.Attribute4.set_quality(AttrQuality.ATTR_VALID)
        if "5" in argin:
            if self.Attribute5.get_quality() == AttrQuality.VALID:
                self.Attribute5.set_quality(AttrQuality.ATTR_INVALID)
            else:
                self.Attribute5.set_quality(AttrQuality.VALID)

        else:
            pass

        # PROTECTED REGION END #    //  SwitchInvalidAttribute.SwitchInvalid


# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(SwitchInvalidAttribute.main) ENABLED START #
    return run((SwitchInvalidAttribute,), args=args, **kwargs)
    # PROTECTED REGION END #    //  SwitchInvalidAttribute.main

if __name__ == '__main__':
    main()
