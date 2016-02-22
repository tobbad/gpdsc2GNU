# ./binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2016-02-18 23:45:07.637177 by PyXB version 1.2.4 using Python 3.5.1.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4231f470-d691-11e5-bc67-081196403c14')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: NonNegativeInteger
class NonNegativeInteger (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NonNegativeInteger')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 52, 2)
    _Documentation = None
NonNegativeInteger._CF_pattern = pyxb.binding.facets.CF_pattern()
NonNegativeInteger._CF_pattern.addPattern(pattern='[+]?(0x|0X)?[0-9a-fA-F]+')
NonNegativeInteger._InitializeFacetMap(NonNegativeInteger._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'NonNegativeInteger', NonNegativeInteger)

# Atomic simple type: DeviceVendorEnum
class DeviceVendorEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeviceVendorEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 59, 2)
    _Documentation = None
DeviceVendorEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeviceVendorEnum, enum_prefix=None)
DeviceVendorEnum.ABOV_Semiconductor126 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='ABOV Semiconductor:126', tag='ABOV_Semiconductor126')
DeviceVendorEnum.Actel56 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Actel:56', tag='Actel56')
DeviceVendorEnum.Altera85 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Altera:85', tag='Altera85')
DeviceVendorEnum.Altium65 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Altium:65', tag='Altium65')
DeviceVendorEnum.Ambiq_Micro120 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Ambiq Micro:120', tag='Ambiq_Micro120')
DeviceVendorEnum.Analog_Devices1 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Analog Devices:1', tag='Analog_Devices1')
DeviceVendorEnum.ARM82 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='ARM:82', tag='ARM82')
DeviceVendorEnum.ARM_CMSIS109 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='ARM CMSIS:109', tag='ARM_CMSIS109')
DeviceVendorEnum.Atmel3 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Atmel:3', tag='Atmel3')
DeviceVendorEnum.CSR118 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='CSR:118', tag='CSR118')
DeviceVendorEnum.Cypress19 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Cypress:19', tag='Cypress19')
DeviceVendorEnum.Dialog_Semiconductor113 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Dialog Semiconductor:113', tag='Dialog_Semiconductor113')
DeviceVendorEnum.Dolphin57 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Dolphin:57', tag='Dolphin57')
DeviceVendorEnum.Domosys26 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Domosys:26', tag='Domosys26')
DeviceVendorEnum.Ember98 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Ember:98', tag='Ember98')
DeviceVendorEnum.Energy_Micro97 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Energy Micro:97', tag='Energy_Micro97')
DeviceVendorEnum.EnOcean91 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='EnOcean:91', tag='EnOcean91')
DeviceVendorEnum.Evatronix64 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Evatronix:64', tag='Evatronix64')
DeviceVendorEnum.Freescale78 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Freescale:78', tag='Freescale78')
DeviceVendorEnum.Generic5 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Generic:5', tag='Generic5')
DeviceVendorEnum.GigaDevice123 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='GigaDevice:123', tag='GigaDevice123')
DeviceVendorEnum.Holtek106 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Holtek:106', tag='Holtek106')
DeviceVendorEnum.Hynix_Semiconductor6 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Hynix Semiconductor:6', tag='Hynix_Semiconductor6')
DeviceVendorEnum.Hyundai35 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Hyundai:35', tag='Hyundai35')
DeviceVendorEnum.Infineon7 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Infineon:7', tag='Infineon7')
DeviceVendorEnum.Kionix127 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Kionix:127', tag='Kionix127')
DeviceVendorEnum.Lapis_Semiconductor10 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Lapis Semiconductor:10', tag='Lapis_Semiconductor10')
DeviceVendorEnum.Luminary_Micro76 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Luminary Micro:76', tag='Luminary_Micro76')
DeviceVendorEnum.Maxim23 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Maxim:23', tag='Maxim23')
DeviceVendorEnum.MegaChips128 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='MegaChips:128', tag='MegaChips128')
DeviceVendorEnum.Mentor_Graphics_Co_24 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Mentor Graphics Co.:24', tag='Mentor_Graphics_Co_24')
DeviceVendorEnum.Micronas30 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Micronas:30', tag='Micronas30')
DeviceVendorEnum.Microsemi112 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Microsemi:112', tag='Microsemi112')
DeviceVendorEnum.Milandr99 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Milandr:99', tag='Milandr99')
DeviceVendorEnum.NetSilicon67 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='NetSilicon:67', tag='NetSilicon67')
DeviceVendorEnum.Nordic_Semiconductor54 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Nordic Semiconductor:54', tag='Nordic_Semiconductor54')
DeviceVendorEnum.Nuvoton18 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Nuvoton:18', tag='Nuvoton18')
DeviceVendorEnum.NXP11 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='NXP:11', tag='NXP11')
DeviceVendorEnum.OKI_SEMICONDUCTOR_CO_LTD_108 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='OKI SEMICONDUCTOR CO.,LTD.:108', tag='OKI_SEMICONDUCTOR_CO_LTD_108')
DeviceVendorEnum.Realtek_Semiconductor124 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Realtek Semiconductor:124', tag='Realtek_Semiconductor124')
DeviceVendorEnum.Redpine_Signals125 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Redpine Signals:125', tag='Redpine_Signals125')
DeviceVendorEnum.Renesas117 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Renesas:117', tag='Renesas117')
DeviceVendorEnum.ROHM103 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='ROHM:103', tag='ROHM103')
DeviceVendorEnum.Samsung47 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Samsung:47', tag='Samsung47')
DeviceVendorEnum.Silicon_Labs21 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Silicon Labs:21', tag='Silicon_Labs21')
DeviceVendorEnum.SONiX110 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='SONiX:110', tag='SONiX110')
DeviceVendorEnum.Spansion100 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Spansion:100', tag='Spansion100')
DeviceVendorEnum.STMicroelectronics13 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='STMicroelectronics:13', tag='STMicroelectronics13')
DeviceVendorEnum.Sunrise_Micro_Devices121 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Sunrise Micro Devices:121', tag='Sunrise_Micro_Devices121')
DeviceVendorEnum.TI16 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='TI:16', tag='TI16')
DeviceVendorEnum.Texas_Instruments16 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Texas Instruments:16', tag='Texas_Instruments16')
DeviceVendorEnum.Toshiba92 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Toshiba:92', tag='Toshiba92')
DeviceVendorEnum.Triad_Semiconductor104 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Triad Semiconductor:104', tag='Triad_Semiconductor104')
DeviceVendorEnum.WIZnet122 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='WIZnet:122', tag='WIZnet122')
DeviceVendorEnum.Freescale_Semiconductor78 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='Freescale Semiconductor:78', tag='Freescale_Semiconductor78')
DeviceVendorEnum.NXP_founded_by_Philips11 = DeviceVendorEnum._CF_enumeration.addEnumeration(unicode_value='NXP (founded by Philips):11', tag='NXP_founded_by_Philips11')
DeviceVendorEnum._InitializeFacetMap(DeviceVendorEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeviceVendorEnum', DeviceVendorEnum)

# Atomic simple type: CclassType
class CclassType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CclassType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 122, 2)
    _Documentation = None
CclassType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
CclassType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
CclassType._InitializeFacetMap(CclassType._CF_minLength,
   CclassType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'CclassType', CclassType)

# Atomic simple type: CgroupType
class CgroupType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CgroupType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 130, 2)
    _Documentation = None
CgroupType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
CgroupType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
CgroupType._InitializeFacetMap(CgroupType._CF_minLength,
   CgroupType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'CgroupType', CgroupType)

# Atomic simple type: CsubType
class CsubType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CsubType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 138, 2)
    _Documentation = None
CsubType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
CsubType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
CsubType._InitializeFacetMap(CsubType._CF_minLength,
   CsubType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'CsubType', CsubType)

# Atomic simple type: CvariantType
class CvariantType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CvariantType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 146, 2)
    _Documentation = None
CvariantType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
CvariantType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
CvariantType._InitializeFacetMap(CvariantType._CF_minLength,
   CvariantType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'CvariantType', CvariantType)

# Atomic simple type: DebugProtocolEnum
class DebugProtocolEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DebugProtocolEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 194, 2)
    _Documentation = None
DebugProtocolEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DebugProtocolEnum, enum_prefix=None)
DebugProtocolEnum.jtag = DebugProtocolEnum._CF_enumeration.addEnumeration(unicode_value='jtag', tag='jtag')
DebugProtocolEnum.swd = DebugProtocolEnum._CF_enumeration.addEnumeration(unicode_value='swd', tag='swd')
DebugProtocolEnum._InitializeFacetMap(DebugProtocolEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DebugProtocolEnum', DebugProtocolEnum)

# Atomic simple type: DataPatchAccessTypeEnum
class DataPatchAccessTypeEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataPatchAccessTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 236, 2)
    _Documentation = None
DataPatchAccessTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DataPatchAccessTypeEnum, enum_prefix=None)
DataPatchAccessTypeEnum.DP = DataPatchAccessTypeEnum._CF_enumeration.addEnumeration(unicode_value='DP', tag='DP')
DataPatchAccessTypeEnum.AP = DataPatchAccessTypeEnum._CF_enumeration.addEnumeration(unicode_value='AP', tag='AP')
DataPatchAccessTypeEnum.Mem = DataPatchAccessTypeEnum._CF_enumeration.addEnumeration(unicode_value='Mem', tag='Mem')
DataPatchAccessTypeEnum._InitializeFacetMap(DataPatchAccessTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DataPatchAccessTypeEnum', DataPatchAccessTypeEnum)

# Atomic simple type: ExpressionType
class ExpressionType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExpressionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 245, 2)
    _Documentation = None
ExpressionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ExpressionType', ExpressionType)

# Atomic simple type: DcoreEnum
class DcoreEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DcoreEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 491, 2)
    _Documentation = None
DcoreEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DcoreEnum, enum_prefix=None)
DcoreEnum.SC000 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='SC000', tag='SC000')
DcoreEnum.SC300 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='SC300', tag='SC300')
DcoreEnum.Cortex_M0 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-M0', tag='Cortex_M0')
DcoreEnum.Cortex_M0_ = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-M0+', tag='Cortex_M0_')
DcoreEnum.Cortex_M1 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-M1', tag='Cortex_M1')
DcoreEnum.Cortex_M3 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-M3', tag='Cortex_M3')
DcoreEnum.Cortex_M4 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-M4', tag='Cortex_M4')
DcoreEnum.Cortex_M7 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-M7', tag='Cortex_M7')
DcoreEnum.Cortex_R4 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-R4', tag='Cortex_R4')
DcoreEnum.Cortex_R5 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-R5', tag='Cortex_R5')
DcoreEnum.Cortex_A5 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-A5', tag='Cortex_A5')
DcoreEnum.Cortex_A7 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-A7', tag='Cortex_A7')
DcoreEnum.Cortex_A8 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-A8', tag='Cortex_A8')
DcoreEnum.Cortex_A9 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-A9', tag='Cortex_A9')
DcoreEnum.Cortex_A15 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-A15', tag='Cortex_A15')
DcoreEnum.Cortex_A17 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-A17', tag='Cortex_A17')
DcoreEnum.Cortex_A53 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-A53', tag='Cortex_A53')
DcoreEnum.Cortex_A57 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-A57', tag='Cortex_A57')
DcoreEnum.Cortex_A72 = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='Cortex-A72', tag='Cortex_A72')
DcoreEnum.other = DcoreEnum._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
DcoreEnum._InitializeFacetMap(DcoreEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DcoreEnum', DcoreEnum)

# Atomic simple type: DeviceFeatureTypeEnum
class DeviceFeatureTypeEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeviceFeatureTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 518, 2)
    _Documentation = None
DeviceFeatureTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeviceFeatureTypeEnum, enum_prefix=None)
DeviceFeatureTypeEnum.Crypto = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Crypto', tag='Crypto')
DeviceFeatureTypeEnum.NVIC = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='NVIC', tag='NVIC')
DeviceFeatureTypeEnum.DMA = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='DMA', tag='DMA')
DeviceFeatureTypeEnum.RNG = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='RNG', tag='RNG')
DeviceFeatureTypeEnum.CoreOther = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='CoreOther', tag='CoreOther')
DeviceFeatureTypeEnum.ExtBus = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ExtBus', tag='ExtBus')
DeviceFeatureTypeEnum.Memory = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Memory', tag='Memory')
DeviceFeatureTypeEnum.MemoryOther = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='MemoryOther', tag='MemoryOther')
DeviceFeatureTypeEnum.XTAL = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='XTAL', tag='XTAL')
DeviceFeatureTypeEnum.IntRC = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='IntRC', tag='IntRC')
DeviceFeatureTypeEnum.PLL = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='PLL', tag='PLL')
DeviceFeatureTypeEnum.RTC = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='RTC', tag='RTC')
DeviceFeatureTypeEnum.ClockOther = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ClockOther', tag='ClockOther')
DeviceFeatureTypeEnum.PowerMode = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='PowerMode', tag='PowerMode')
DeviceFeatureTypeEnum.VCC = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='VCC', tag='VCC')
DeviceFeatureTypeEnum.Consumption = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Consumption', tag='Consumption')
DeviceFeatureTypeEnum.PowerOther = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='PowerOther', tag='PowerOther')
DeviceFeatureTypeEnum.BGA = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='BGA', tag='BGA')
DeviceFeatureTypeEnum.CSP = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='CSP', tag='CSP')
DeviceFeatureTypeEnum.PLCC = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='PLCC', tag='PLCC')
DeviceFeatureTypeEnum.QFN = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='QFN', tag='QFN')
DeviceFeatureTypeEnum.QFP = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='QFP', tag='QFP')
DeviceFeatureTypeEnum.SOP = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='SOP', tag='SOP')
DeviceFeatureTypeEnum.DIP = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='DIP', tag='DIP')
DeviceFeatureTypeEnum.PackageOther = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='PackageOther', tag='PackageOther')
DeviceFeatureTypeEnum.IOs = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='IOs', tag='IOs')
DeviceFeatureTypeEnum.ExtInt = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ExtInt', tag='ExtInt')
DeviceFeatureTypeEnum.Temp = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Temp', tag='Temp')
DeviceFeatureTypeEnum.ADC = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ADC', tag='ADC')
DeviceFeatureTypeEnum.DAC = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='DAC', tag='DAC')
DeviceFeatureTypeEnum.TempSens = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='TempSens', tag='TempSens')
DeviceFeatureTypeEnum.AnalogOther = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='AnalogOther', tag='AnalogOther')
DeviceFeatureTypeEnum.PWM = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='PWM', tag='PWM')
DeviceFeatureTypeEnum.Timer = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Timer', tag='Timer')
DeviceFeatureTypeEnum.WDT = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='WDT', tag='WDT')
DeviceFeatureTypeEnum.TimerOther = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='TimerOther', tag='TimerOther')
DeviceFeatureTypeEnum.MPSerial = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='MPSerial', tag='MPSerial')
DeviceFeatureTypeEnum.CAN = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='CAN', tag='CAN')
DeviceFeatureTypeEnum.ETH = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ETH', tag='ETH')
DeviceFeatureTypeEnum.I2C = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='I2C', tag='I2C')
DeviceFeatureTypeEnum.I2S = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='I2S', tag='I2S')
DeviceFeatureTypeEnum.LIN = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='LIN', tag='LIN')
DeviceFeatureTypeEnum.SDIO = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='SDIO', tag='SDIO')
DeviceFeatureTypeEnum.SPI = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='SPI', tag='SPI')
DeviceFeatureTypeEnum.UART = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='UART', tag='UART')
DeviceFeatureTypeEnum.USART = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='USART', tag='USART')
DeviceFeatureTypeEnum.USBD = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='USBD', tag='USBD')
DeviceFeatureTypeEnum.USBH = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='USBH', tag='USBH')
DeviceFeatureTypeEnum.USBOTG = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='USBOTG', tag='USBOTG')
DeviceFeatureTypeEnum.ComOther = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ComOther', tag='ComOther')
DeviceFeatureTypeEnum.Camera = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Camera', tag='Camera')
DeviceFeatureTypeEnum.GLCD = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='GLCD', tag='GLCD')
DeviceFeatureTypeEnum.LCD = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='LCD', tag='LCD')
DeviceFeatureTypeEnum.Touch = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Touch', tag='Touch')
DeviceFeatureTypeEnum.Other = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
DeviceFeatureTypeEnum.IO = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='I/O', tag='IO')
DeviceFeatureTypeEnum.DA = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='D/A', tag='DA')
DeviceFeatureTypeEnum.AD = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='A/D', tag='AD')
DeviceFeatureTypeEnum.Com = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Com', tag='Com')
DeviceFeatureTypeEnum.USB = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='USB', tag='USB')
DeviceFeatureTypeEnum.Package = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Package', tag='Package')
DeviceFeatureTypeEnum.Backup = DeviceFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Backup', tag='Backup')
DeviceFeatureTypeEnum._InitializeFacetMap(DeviceFeatureTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeviceFeatureTypeEnum', DeviceFeatureTypeEnum)

# Atomic simple type: BoardFeatureTypeEnum
class BoardFeatureTypeEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoardFeatureTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 587, 2)
    _Documentation = None
BoardFeatureTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BoardFeatureTypeEnum, enum_prefix=None)
BoardFeatureTypeEnum.ODbg = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ODbg', tag='ODbg')
BoardFeatureTypeEnum.XTAL = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='XTAL', tag='XTAL')
BoardFeatureTypeEnum.PWR = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='PWR', tag='PWR')
BoardFeatureTypeEnum.PWR_ = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='PWR', tag='PWR_')
BoardFeatureTypeEnum.PWRSock = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='PWRSock', tag='PWRSock')
BoardFeatureTypeEnum.Batt = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Batt', tag='Batt')
BoardFeatureTypeEnum.Curr = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Curr', tag='Curr')
BoardFeatureTypeEnum.CoreOther = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='CoreOther', tag='CoreOther')
BoardFeatureTypeEnum.RAM = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='RAM', tag='RAM')
BoardFeatureTypeEnum.ROM = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ROM', tag='ROM')
BoardFeatureTypeEnum.Memory = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Memory', tag='Memory')
BoardFeatureTypeEnum.MemCard = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='MemCard', tag='MemCard')
BoardFeatureTypeEnum.MemoryOther = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='MemoryOther', tag='MemoryOther')
BoardFeatureTypeEnum.DIO = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='DIO', tag='DIO')
BoardFeatureTypeEnum.AIO = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='AIO', tag='AIO')
BoardFeatureTypeEnum.Proto = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Proto', tag='Proto')
BoardFeatureTypeEnum.USB = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='USB', tag='USB')
BoardFeatureTypeEnum.ETH = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ETH', tag='ETH')
BoardFeatureTypeEnum.SPI = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='SPI', tag='SPI')
BoardFeatureTypeEnum.I2C = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='I2C', tag='I2C')
BoardFeatureTypeEnum.RS232 = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='RS232', tag='RS232')
BoardFeatureTypeEnum.RS422 = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='RS422', tag='RS422')
BoardFeatureTypeEnum.RS485 = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='RS485', tag='RS485')
BoardFeatureTypeEnum.CAN = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='CAN', tag='CAN')
BoardFeatureTypeEnum.IrDA = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='IrDA', tag='IrDA')
BoardFeatureTypeEnum.LineIn = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='LineIn', tag='LineIn')
BoardFeatureTypeEnum.LineOut = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='LineOut', tag='LineOut')
BoardFeatureTypeEnum.MIC = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='MIC', tag='MIC')
BoardFeatureTypeEnum.Edge = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Edge', tag='Edge')
BoardFeatureTypeEnum.ConnOther = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ConnOther', tag='ConnOther')
BoardFeatureTypeEnum.Button = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Button', tag='Button')
BoardFeatureTypeEnum.Poti = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Poti', tag='Poti')
BoardFeatureTypeEnum.Joystick = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Joystick', tag='Joystick')
BoardFeatureTypeEnum.Touch = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Touch', tag='Touch')
BoardFeatureTypeEnum.ContOther = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ContOther', tag='ContOther')
BoardFeatureTypeEnum.Accelerometer = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Accelerometer', tag='Accelerometer')
BoardFeatureTypeEnum.Gyro = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Gyro', tag='Gyro')
BoardFeatureTypeEnum.Compass = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Compass', tag='Compass')
BoardFeatureTypeEnum.TempSens = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='TempSens', tag='TempSens')
BoardFeatureTypeEnum.PressSens = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='PressSens', tag='PressSens')
BoardFeatureTypeEnum.LightSens = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='LightSens', tag='LightSens')
BoardFeatureTypeEnum.SensOther = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='SensOther', tag='SensOther')
BoardFeatureTypeEnum.CustomFF = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='CustomFF', tag='CustomFF')
BoardFeatureTypeEnum.ArduinoFF = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='ArduinoFF', tag='ArduinoFF')
BoardFeatureTypeEnum.FreedomFF = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='FreedomFF', tag='FreedomFF')
BoardFeatureTypeEnum.TowerFF = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='TowerFF', tag='TowerFF')
BoardFeatureTypeEnum.LED = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='LED', tag='LED')
BoardFeatureTypeEnum.Camera = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Camera', tag='Camera')
BoardFeatureTypeEnum.LCD = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='LCD', tag='LCD')
BoardFeatureTypeEnum.GLCD = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='GLCD', tag='GLCD')
BoardFeatureTypeEnum.Speaker = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Speaker', tag='Speaker')
BoardFeatureTypeEnum.Other = BoardFeatureTypeEnum._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
BoardFeatureTypeEnum._InitializeFacetMap(BoardFeatureTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BoardFeatureTypeEnum', BoardFeatureTypeEnum)

# Atomic simple type: EraseTypeEnum
class EraseTypeEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EraseTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 645, 2)
    _Documentation = None
EraseTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EraseTypeEnum, enum_prefix=None)
EraseTypeEnum.sector = EraseTypeEnum._CF_enumeration.addEnumeration(unicode_value='sector', tag='sector')
EraseTypeEnum.full = EraseTypeEnum._CF_enumeration.addEnumeration(unicode_value='full', tag='full')
EraseTypeEnum.no = EraseTypeEnum._CF_enumeration.addEnumeration(unicode_value='no', tag='no')
EraseTypeEnum._InitializeFacetMap(EraseTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EraseTypeEnum', EraseTypeEnum)

# Atomic simple type: MemoryIDTypeEnum
class MemoryIDTypeEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MemoryIDTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 654, 2)
    _Documentation = None
MemoryIDTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MemoryIDTypeEnum, enum_prefix=None)
MemoryIDTypeEnum.IRAM1 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IRAM1', tag='IRAM1')
MemoryIDTypeEnum.IRAM2 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IRAM2', tag='IRAM2')
MemoryIDTypeEnum.IRAM3 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IRAM3', tag='IRAM3')
MemoryIDTypeEnum.IRAM4 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IRAM4', tag='IRAM4')
MemoryIDTypeEnum.IRAM5 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IRAM5', tag='IRAM5')
MemoryIDTypeEnum.IRAM6 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IRAM6', tag='IRAM6')
MemoryIDTypeEnum.IRAM7 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IRAM7', tag='IRAM7')
MemoryIDTypeEnum.IRAM8 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IRAM8', tag='IRAM8')
MemoryIDTypeEnum.IROM1 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IROM1', tag='IROM1')
MemoryIDTypeEnum.IROM2 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IROM2', tag='IROM2')
MemoryIDTypeEnum.IROM3 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IROM3', tag='IROM3')
MemoryIDTypeEnum.IROM4 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IROM4', tag='IROM4')
MemoryIDTypeEnum.IROM5 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IROM5', tag='IROM5')
MemoryIDTypeEnum.IROM6 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IROM6', tag='IROM6')
MemoryIDTypeEnum.IROM7 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IROM7', tag='IROM7')
MemoryIDTypeEnum.IROM8 = MemoryIDTypeEnum._CF_enumeration.addEnumeration(unicode_value='IROM8', tag='IROM8')
MemoryIDTypeEnum._InitializeFacetMap(MemoryIDTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MemoryIDTypeEnum', MemoryIDTypeEnum)

# Atomic simple type: DendianEnum
class DendianEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DendianEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 676, 2)
    _Documentation = None
DendianEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DendianEnum, enum_prefix=None)
DendianEnum.Little_endian = DendianEnum._CF_enumeration.addEnumeration(unicode_value='Little-endian', tag='Little_endian')
DendianEnum.Big_endian = DendianEnum._CF_enumeration.addEnumeration(unicode_value='Big-endian', tag='Big_endian')
DendianEnum.Configurable = DendianEnum._CF_enumeration.addEnumeration(unicode_value='Configurable', tag='Configurable')
DendianEnum.emptyString = DendianEnum._CF_enumeration.addEnumeration(unicode_value='*', tag='emptyString')
DendianEnum._InitializeFacetMap(DendianEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DendianEnum', DendianEnum)

# Atomic simple type: DfpuEnum
class DfpuEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DfpuEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 686, 2)
    _Documentation = None
DfpuEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DfpuEnum, enum_prefix=None)
DfpuEnum.FPU = DfpuEnum._CF_enumeration.addEnumeration(unicode_value='FPU', tag='FPU')
DfpuEnum.n1 = DfpuEnum._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
DfpuEnum.NO_FPU = DfpuEnum._CF_enumeration.addEnumeration(unicode_value='NO_FPU', tag='NO_FPU')
DfpuEnum.n0 = DfpuEnum._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
DfpuEnum.SP_FPU = DfpuEnum._CF_enumeration.addEnumeration(unicode_value='SP_FPU', tag='SP_FPU')
DfpuEnum.DP_FPU = DfpuEnum._CF_enumeration.addEnumeration(unicode_value='DP_FPU', tag='DP_FPU')
DfpuEnum.emptyString = DfpuEnum._CF_enumeration.addEnumeration(unicode_value='*', tag='emptyString')
DfpuEnum._InitializeFacetMap(DfpuEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DfpuEnum', DfpuEnum)

# Atomic simple type: DmpuEnum
class DmpuEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DmpuEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 704, 2)
    _Documentation = None
DmpuEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DmpuEnum, enum_prefix=None)
DmpuEnum.MPU = DmpuEnum._CF_enumeration.addEnumeration(unicode_value='MPU', tag='MPU')
DmpuEnum.NO_MPU = DmpuEnum._CF_enumeration.addEnumeration(unicode_value='NO_MPU', tag='NO_MPU')
DmpuEnum.n0 = DmpuEnum._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
DmpuEnum.n1 = DmpuEnum._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
DmpuEnum.emptyString = DmpuEnum._CF_enumeration.addEnumeration(unicode_value='*', tag='emptyString')
DmpuEnum._InitializeFacetMap(DmpuEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DmpuEnum', DmpuEnum)

# Atomic simple type: FileCategoryType
class FileCategoryType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FileCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 715, 2)
    _Documentation = None
FileCategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FileCategoryType, enum_prefix=None)
FileCategoryType.doc = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='doc', tag='doc')
FileCategoryType.header = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='header', tag='header')
FileCategoryType.include = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='include', tag='include')
FileCategoryType.library = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='library', tag='library')
FileCategoryType.object = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='object', tag='object')
FileCategoryType.source = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='source', tag='source')
FileCategoryType.sourceC = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='sourceC', tag='sourceC')
FileCategoryType.sourceCpp = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='sourceCpp', tag='sourceCpp')
FileCategoryType.sourceAsm = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='sourceAsm', tag='sourceAsm')
FileCategoryType.linkerScript = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='linkerScript', tag='linkerScript')
FileCategoryType.utility = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='utility', tag='utility')
FileCategoryType.image = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='image', tag='image')
FileCategoryType.other = FileCategoryType._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
FileCategoryType._InitializeFacetMap(FileCategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FileCategoryType', FileCategoryType)

# Atomic simple type: FileAttributeType
class FileAttributeType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FileAttributeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 734, 2)
    _Documentation = None
FileAttributeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FileAttributeType, enum_prefix=None)
FileAttributeType.config = FileAttributeType._CF_enumeration.addEnumeration(unicode_value='config', tag='config')
FileAttributeType.copy = FileAttributeType._CF_enumeration.addEnumeration(unicode_value='copy', tag='copy')
FileAttributeType.template = FileAttributeType._CF_enumeration.addEnumeration(unicode_value='template', tag='template')
FileAttributeType.interface = FileAttributeType._CF_enumeration.addEnumeration(unicode_value='interface', tag='interface')
FileAttributeType._InitializeFacetMap(FileAttributeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FileAttributeType', FileAttributeType)

# Atomic simple type: CompilerEnumType
class CompilerEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompilerEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 745, 2)
    _Documentation = None
CompilerEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CompilerEnumType, enum_prefix=None)
CompilerEnumType.GCC = CompilerEnumType._CF_enumeration.addEnumeration(unicode_value='GCC', tag='GCC')
CompilerEnumType.ARMCC = CompilerEnumType._CF_enumeration.addEnumeration(unicode_value='ARMCC', tag='ARMCC')
CompilerEnumType.IAR = CompilerEnumType._CF_enumeration.addEnumeration(unicode_value='IAR', tag='IAR')
CompilerEnumType.Tasking = CompilerEnumType._CF_enumeration.addEnumeration(unicode_value='Tasking', tag='Tasking')
CompilerEnumType.GHS = CompilerEnumType._CF_enumeration.addEnumeration(unicode_value='GHS', tag='GHS')
CompilerEnumType.Cosmic = CompilerEnumType._CF_enumeration.addEnumeration(unicode_value='Cosmic', tag='Cosmic')
CompilerEnumType.G = CompilerEnumType._CF_enumeration.addEnumeration(unicode_value='G++', tag='G')
CompilerEnumType.emptyString = CompilerEnumType._CF_enumeration.addEnumeration(unicode_value='*', tag='emptyString')
CompilerEnumType._InitializeFacetMap(CompilerEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CompilerEnumType', CompilerEnumType)

# Atomic simple type: CompilerOutputType
class CompilerOutputType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompilerOutputType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 758, 2)
    _Documentation = None
CompilerOutputType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CompilerOutputType, enum_prefix=None)
CompilerOutputType.exe = CompilerOutputType._CF_enumeration.addEnumeration(unicode_value='exe', tag='exe')
CompilerOutputType.lib = CompilerOutputType._CF_enumeration.addEnumeration(unicode_value='lib', tag='lib')
CompilerOutputType.emptyString = CompilerOutputType._CF_enumeration.addEnumeration(unicode_value='*', tag='emptyString')
CompilerOutputType._InitializeFacetMap(CompilerOutputType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CompilerOutputType', CompilerOutputType)

# Atomic simple type: BoardBookCategoryEnum
class BoardBookCategoryEnum (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoardBookCategoryEnum')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 900, 2)
    _Documentation = None
BoardBookCategoryEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BoardBookCategoryEnum, enum_prefix=None)
BoardBookCategoryEnum.setup = BoardBookCategoryEnum._CF_enumeration.addEnumeration(unicode_value='setup', tag='setup')
BoardBookCategoryEnum.schematic = BoardBookCategoryEnum._CF_enumeration.addEnumeration(unicode_value='schematic', tag='schematic')
BoardBookCategoryEnum.overview = BoardBookCategoryEnum._CF_enumeration.addEnumeration(unicode_value='overview', tag='overview')
BoardBookCategoryEnum.manual = BoardBookCategoryEnum._CF_enumeration.addEnumeration(unicode_value='manual', tag='manual')
BoardBookCategoryEnum.other = BoardBookCategoryEnum._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
BoardBookCategoryEnum._InitializeFacetMap(BoardBookCategoryEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BoardBookCategoryEnum', BoardBookCategoryEnum)

# Atomic simple type: MaxInstancesType
class MaxInstancesType (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaxInstancesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 999, 2)
    _Documentation = None
MaxInstancesType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=MaxInstancesType, value=pyxb.binding.datatypes.integer(1))
MaxInstancesType._InitializeFacetMap(MaxInstancesType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'MaxInstancesType', MaxInstancesType)

# Atomic simple type: RestrictedString
class RestrictedString (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RestrictedString')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1027, 2)
    _Documentation = None
RestrictedString._CF_pattern = pyxb.binding.facets.CF_pattern()
RestrictedString._CF_pattern.addPattern(pattern='[\\-_A-Za-z0-9]+')
RestrictedString._InitializeFacetMap(RestrictedString._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RestrictedString', RestrictedString)

# Atomic simple type: VersionType
class VersionType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VersionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1035, 2)
    _Documentation = None
VersionType._CF_pattern = pyxb.binding.facets.CF_pattern()
VersionType._CF_pattern.addPattern(pattern='[\\.\\-_A-Za-z0-9]+')
VersionType._InitializeFacetMap(VersionType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'VersionType', VersionType)

# Atomic simple type: ConditionVersionType
class ConditionVersionType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConditionVersionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1041, 2)
    _Documentation = None
ConditionVersionType._CF_pattern = pyxb.binding.facets.CF_pattern()
ConditionVersionType._CF_pattern.addPattern(pattern='[\\.:\\-_A-Za-z0-9]+')
ConditionVersionType._InitializeFacetMap(ConditionVersionType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ConditionVersionType', ConditionVersionType)

# Complex type DebugPortType with content type ELEMENT_ONLY
class DebugPortType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DebugPortType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DebugPortType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 226, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element jtag uses Python identifier jtag
    __jtag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'jtag'), 'jtag', '__AbsentNamespace0_DebugPortType_jtag', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 228, 6), )

    
    jtag = property(__jtag.value, __jtag.set, None, None)

    
    # Element swd uses Python identifier swd
    __swd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'swd'), 'swd', '__AbsentNamespace0_DebugPortType_swd', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 229, 6), )

    
    swd = property(__swd.value, __swd.set, None, None)

    
    # Attribute __dp uses Python identifier dp
    __dp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, '__dp'), 'dp', '__AbsentNamespace0_DebugPortType___dp', pyxb.binding.datatypes.unsignedInt)
    __dp._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 231, 4)
    __dp._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 231, 4)
    
    dp = property(__dp.value, __dp.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __jtag.name() : __jtag,
        __swd.name() : __swd
    })
    _AttributeMap.update({
        __dp.name() : __dp
    })
Namespace.addCategoryObject('typeBinding', 'DebugPortType', DebugPortType)


# Complex type SequenceBlockType with content type SIMPLE
class SequenceBlockType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SequenceBlockType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequenceBlockType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 262, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute atomic uses Python identifier atomic
    __atomic = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'atomic'), 'atomic', '__AbsentNamespace0_SequenceBlockType_atomic', pyxb.binding.datatypes.boolean)
    __atomic._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 265, 8)
    __atomic._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 265, 8)
    
    atomic = property(__atomic.value, __atomic.set, None, None)

    
    # Attribute info uses Python identifier info
    __info = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'info'), 'info', '__AbsentNamespace0_SequenceBlockType_info', pyxb.binding.datatypes.string)
    __info._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 266, 8)
    __info._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 266, 8)
    
    info = property(__info.value, __info.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __atomic.name() : __atomic,
        __info.name() : __info
    })
Namespace.addCategoryObject('typeBinding', 'SequenceBlockType', SequenceBlockType)


# Complex type SequencesType with content type ELEMENT_ONLY
class SequencesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SequencesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequencesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 306, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sequence uses Python identifier sequence
    __sequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sequence'), 'sequence', '__AbsentNamespace0_SequencesType_sequence', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 308, 6), )

    
    sequence = property(__sequence.value, __sequence.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __sequence.name() : __sequence
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SequencesType', SequencesType)


# Complex type SerialWireType with content type EMPTY
class SerialWireType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SerialWireType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SerialWireType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 326, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SerialWireType', SerialWireType)


# Complex type BoardFeatureType with content type EMPTY
class BoardFeatureType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BoardFeatureType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoardFeatureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 423, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_BoardFeatureType_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 425, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 425, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute n uses Python identifier n
    __n = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'n'), 'n', '__AbsentNamespace0_BoardFeatureType_n', pyxb.binding.datatypes.decimal)
    __n._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 426, 4)
    __n._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 426, 4)
    
    n = property(__n.value, __n.set, None, None)

    
    # Attribute m uses Python identifier m
    __m = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'm'), 'm', '__AbsentNamespace0_BoardFeatureType_m', pyxb.binding.datatypes.decimal)
    __m._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 427, 4)
    __m._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 427, 4)
    
    m = property(__m.value, __m.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_BoardFeatureType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 428, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 428, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __n.name() : __n,
        __m.name() : __m,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'BoardFeatureType', BoardFeatureType)


# Complex type DeviceType with content type ELEMENT_ONLY
class DeviceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DeviceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeviceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 472, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element compile uses Python identifier compile
    __compile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'compile'), 'compile', '__AbsentNamespace0_DeviceType_compile', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6), )

    
    compile = property(__compile.value, __compile.set, None, None)

    
    # Element memory uses Python identifier memory
    __memory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'memory'), 'memory', '__AbsentNamespace0_DeviceType_memory', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6), )

    
    memory = property(__memory.value, __memory.set, None, None)

    
    # Element algorithm uses Python identifier algorithm
    __algorithm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'algorithm'), 'algorithm', '__AbsentNamespace0_DeviceType_algorithm', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6), )

    
    algorithm = property(__algorithm.value, __algorithm.set, None, None)

    
    # Element book uses Python identifier book
    __book = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'book'), 'book', '__AbsentNamespace0_DeviceType_book', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6), )

    
    book = property(__book.value, __book.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_DeviceType_description', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element feature uses Python identifier feature
    __feature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'feature'), 'feature', '__AbsentNamespace0_DeviceType_feature', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6), )

    
    feature = property(__feature.value, __feature.set, None, None)

    
    # Element environment uses Python identifier environment
    __environment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'environment'), 'environment', '__AbsentNamespace0_DeviceType_environment', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6), )

    
    environment = property(__environment.value, __environment.set, None, None)

    
    # Element debugport uses Python identifier debugport
    __debugport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugport'), 'debugport', '__AbsentNamespace0_DeviceType_debugport', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6), )

    
    debugport = property(__debugport.value, __debugport.set, None, None)

    
    # Element debug uses Python identifier debug
    __debug = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debug'), 'debug', '__AbsentNamespace0_DeviceType_debug', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6), )

    
    debug = property(__debug.value, __debug.set, None, None)

    
    # Element trace uses Python identifier trace
    __trace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trace'), 'trace', '__AbsentNamespace0_DeviceType_trace', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6), )

    
    trace = property(__trace.value, __trace.set, None, None)

    
    # Element debugvars uses Python identifier debugvars
    __debugvars = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugvars'), 'debugvars', '__AbsentNamespace0_DeviceType_debugvars', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6), )

    
    debugvars = property(__debugvars.value, __debugvars.set, None, None)

    
    # Element sequences uses Python identifier sequences
    __sequences = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sequences'), 'sequences', '__AbsentNamespace0_DeviceType_sequences', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6), )

    
    sequences = property(__sequences.value, __sequences.set, None, None)

    
    # Element processor uses Python identifier processor
    __processor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'processor'), 'processor', '__AbsentNamespace0_DeviceType_processor', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6), )

    
    processor = property(__processor.value, __processor.set, None, None)

    
    # Element debugconfig uses Python identifier debugconfig
    __debugconfig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugconfig'), 'debugconfig', '__AbsentNamespace0_DeviceType_debugconfig', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6), )

    
    debugconfig = property(__debugconfig.value, __debugconfig.set, None, None)

    
    # Element variant uses Python identifier variant
    __variant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'variant'), 'variant', '__AbsentNamespace0_DeviceType_variant', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 476, 6), )

    
    variant = property(__variant.value, __variant.set, None, None)

    
    # Attribute Dname uses Python identifier Dname
    __Dname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dname'), 'Dname', '__AbsentNamespace0_DeviceType_Dname', pyxb.binding.datatypes.string, required=True)
    __Dname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 486, 4)
    __Dname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 486, 4)
    
    Dname = property(__Dname.value, __Dname.set, None, None)

    _ElementMap.update({
        __compile.name() : __compile,
        __memory.name() : __memory,
        __algorithm.name() : __algorithm,
        __book.name() : __book,
        __description.name() : __description,
        __feature.name() : __feature,
        __environment.name() : __environment,
        __debugport.name() : __debugport,
        __debug.name() : __debug,
        __trace.name() : __trace,
        __debugvars.name() : __debugvars,
        __sequences.name() : __sequences,
        __processor.name() : __processor,
        __debugconfig.name() : __debugconfig,
        __variant.name() : __variant
    })
    _AttributeMap.update({
        __Dname.name() : __Dname
    })
Namespace.addCategoryObject('typeBinding', 'DeviceType', DeviceType)


# Complex type TaxonomyType with content type ELEMENT_ONLY
class TaxonomyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TaxonomyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxonomyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 804, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_TaxonomyType_description', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 806, 6), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TaxonomyType', TaxonomyType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 816, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'file'), 'file', '__AbsentNamespace0_CTD_ANON_file', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 818, 12), )

    
    file = property(__file.value, __file.set, None, None)

    _ElementMap.update({
        __file.name() : __file
    })
    _AttributeMap.update({
        
    })



# Complex type ApisType with content type ELEMENT_ONLY
class ApisType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ApisType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ApisType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 829, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element api uses Python identifier api
    __api = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'api'), 'api', '__AbsentNamespace0_ApisType_api', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 831, 6), )

    
    api = property(__api.value, __api.set, None, None)

    _ElementMap.update({
        __api.name() : __api
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ApisType', ApisType)


# Complex type ConditionType with content type ELEMENT_ONLY
class ConditionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ConditionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConditionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 835, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_ConditionType_description', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 837, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element accept uses Python identifier accept
    __accept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'accept'), 'accept', '__AbsentNamespace0_ConditionType_accept', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 839, 8), )

    
    accept = property(__accept.value, __accept.set, None, None)

    
    # Element require uses Python identifier require
    __require = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'require'), 'require', '__AbsentNamespace0_ConditionType_require', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 840, 8), )

    
    require = property(__require.value, __require.set, None, None)

    
    # Element deny uses Python identifier deny
    __deny = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deny'), 'deny', '__AbsentNamespace0_ConditionType_deny', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 841, 8), )

    
    deny = property(__deny.value, __deny.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_ConditionType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 844, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 844, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __accept.name() : __accept,
        __require.name() : __require,
        __deny.name() : __deny
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'ConditionType', ConditionType)


# Complex type ConditionsType with content type ELEMENT_ONLY
class ConditionsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ConditionsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConditionsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 847, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element condition uses Python identifier condition
    __condition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'condition'), 'condition', '__AbsentNamespace0_ConditionsType_condition', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 849, 6), )

    
    condition = property(__condition.value, __condition.set, None, None)

    _ElementMap.update({
        __condition.name() : __condition
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ConditionsType', ConditionsType)


# Complex type ExampleProjectType with content type ELEMENT_ONLY
class ExampleProjectType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ExampleProjectType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExampleProjectType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 864, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element environment uses Python identifier environment
    __environment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'environment'), 'environment', '__AbsentNamespace0_ExampleProjectType_environment', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 866, 6), )

    
    environment = property(__environment.value, __environment.set, None, None)

    _ElementMap.update({
        __environment.name() : __environment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ExampleProjectType', ExampleProjectType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 867, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON__name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 868, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 868, 10)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute load uses Python identifier load
    __load = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'load'), 'load', '__AbsentNamespace0_CTD_ANON__load', pyxb.binding.datatypes.string, required=True)
    __load._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 869, 10)
    __load._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 869, 10)
    
    load = property(__load.value, __load.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __load.name() : __load
    })



# Complex type DebugInterfaceType with content type EMPTY
class DebugInterfaceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DebugInterfaceType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DebugInterfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 916, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute adapter uses Python identifier adapter
    __adapter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'adapter'), 'adapter', '__AbsentNamespace0_DebugInterfaceType_adapter', pyxb.binding.datatypes.string)
    __adapter._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 917, 4)
    __adapter._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 917, 4)
    
    adapter = property(__adapter.value, __adapter.set, None, None)

    
    # Attribute connector uses Python identifier connector
    __connector = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'connector'), 'connector', '__AbsentNamespace0_DebugInterfaceType_connector', pyxb.binding.datatypes.string)
    __connector._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 918, 4)
    __connector._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 918, 4)
    
    connector = property(__connector.value, __connector.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __adapter.name() : __adapter,
        __connector.name() : __connector
    })
Namespace.addCategoryObject('typeBinding', 'DebugInterfaceType', DebugInterfaceType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 928, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute small uses Python identifier small
    __small = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'small'), 'small', '__AbsentNamespace0_CTD_ANON_2_small', pyxb.binding.datatypes.string)
    __small._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 929, 10)
    __small._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 929, 10)
    
    small = property(__small.value, __small.set, None, None)

    
    # Attribute large uses Python identifier large
    __large = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'large'), 'large', '__AbsentNamespace0_CTD_ANON_2_large', pyxb.binding.datatypes.string)
    __large._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 930, 10)
    __large._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 930, 10)
    
    large = property(__large.value, __large.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __small.name() : __small,
        __large.name() : __large
    })



# Complex type BoardType with content type ELEMENT_ONLY
class BoardType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BoardType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoardType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 938, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_BoardType_description', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 923, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element feature uses Python identifier feature
    __feature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'feature'), 'feature', '__AbsentNamespace0_BoardType_feature', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 924, 6), )

    
    feature = property(__feature.value, __feature.set, None, None)

    
    # Element mountedDevice uses Python identifier mountedDevice
    __mountedDevice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mountedDevice'), 'mountedDevice', '__AbsentNamespace0_BoardType_mountedDevice', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 925, 6), )

    
    mountedDevice = property(__mountedDevice.value, __mountedDevice.set, None, None)

    
    # Element compatibleDevice uses Python identifier compatibleDevice
    __compatibleDevice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'compatibleDevice'), 'compatibleDevice', '__AbsentNamespace0_BoardType_compatibleDevice', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 926, 6), )

    
    compatibleDevice = property(__compatibleDevice.value, __compatibleDevice.set, None, None)

    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'image'), 'image', '__AbsentNamespace0_BoardType_image', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 927, 6), )

    
    image = property(__image.value, __image.set, None, None)

    
    # Element debugInterface uses Python identifier debugInterface
    __debugInterface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugInterface'), 'debugInterface', '__AbsentNamespace0_BoardType_debugInterface', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 933, 6), )

    
    debugInterface = property(__debugInterface.value, __debugInterface.set, None, None)

    
    # Element book uses Python identifier book
    __book = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'book'), 'book', '__AbsentNamespace0_BoardType_book', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 934, 6), )

    
    book = property(__book.value, __book.set, None, None)

    
    # Attribute vendor uses Python identifier vendor
    __vendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vendor'), 'vendor', '__AbsentNamespace0_BoardType_vendor', pyxb.binding.datatypes.string, required=True)
    __vendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 942, 4)
    __vendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 942, 4)
    
    vendor = property(__vendor.value, __vendor.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_BoardType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 943, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 943, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute revision uses Python identifier revision
    __revision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'revision'), 'revision', '__AbsentNamespace0_BoardType_revision', pyxb.binding.datatypes.string)
    __revision._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 944, 4)
    __revision._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 944, 4)
    
    revision = property(__revision.value, __revision.set, None, None)

    
    # Attribute salesContact uses Python identifier salesContact
    __salesContact = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'salesContact'), 'salesContact', '__AbsentNamespace0_BoardType_salesContact', pyxb.binding.datatypes.string)
    __salesContact._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 945, 4)
    __salesContact._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 945, 4)
    
    salesContact = property(__salesContact.value, __salesContact.set, None, None)

    
    # Attribute orderForm uses Python identifier orderForm
    __orderForm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'orderForm'), 'orderForm', '__AbsentNamespace0_BoardType_orderForm', pyxb.binding.datatypes.anyURI)
    __orderForm._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 946, 4)
    __orderForm._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 946, 4)
    
    orderForm = property(__orderForm.value, __orderForm.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __feature.name() : __feature,
        __mountedDevice.name() : __mountedDevice,
        __compatibleDevice.name() : __compatibleDevice,
        __image.name() : __image,
        __debugInterface.name() : __debugInterface,
        __book.name() : __book
    })
    _AttributeMap.update({
        __vendor.name() : __vendor,
        __name.name() : __name,
        __revision.name() : __revision,
        __salesContact.name() : __salesContact,
        __orderForm.name() : __orderForm
    })
Namespace.addCategoryObject('typeBinding', 'BoardType', BoardType)


# Complex type BoardsType with content type ELEMENT_ONLY
class BoardsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BoardsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoardsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 949, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element board uses Python identifier board
    __board = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'board'), 'board', '__AbsentNamespace0_BoardsType_board', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 951, 6), )

    
    board = property(__board.value, __board.set, None, None)

    _ElementMap.update({
        __board.name() : __board
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BoardsType', BoardsType)


# Complex type ExampleAttributesType with content type ELEMENT_ONLY
class ExampleAttributesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ExampleAttributesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExampleAttributesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 955, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__AbsentNamespace0_ExampleAttributesType_category', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 957, 6), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element component uses Python identifier component
    __component = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'component'), 'component', '__AbsentNamespace0_ExampleAttributesType_component', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 958, 6), )

    
    component = property(__component.value, __component.set, None, None)

    
    # Element keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keyword'), 'keyword', '__AbsentNamespace0_ExampleAttributesType_keyword', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 959, 6), )

    
    keyword = property(__keyword.value, __keyword.set, None, None)

    _ElementMap.update({
        __category.name() : __category,
        __component.name() : __component,
        __keyword.name() : __keyword
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ExampleAttributesType', ExampleAttributesType)


# Complex type ExampleType with content type ELEMENT_ONLY
class ExampleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ExampleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExampleType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 963, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_ExampleType_description', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 966, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element board uses Python identifier board
    __board = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'board'), 'board', '__AbsentNamespace0_ExampleType_board', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 968, 6), )

    
    board = property(__board.value, __board.set, None, None)

    
    # Element project uses Python identifier project
    __project = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'project'), 'project', '__AbsentNamespace0_ExampleType_project', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 970, 6), )

    
    project = property(__project.value, __project.set, None, None)

    
    # Element attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'attributes'), 'attributes', '__AbsentNamespace0_ExampleType_attributes', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 972, 6), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_ExampleType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 975, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 975, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute folder uses Python identifier folder
    __folder = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'folder'), 'folder', '__AbsentNamespace0_ExampleType_folder', pyxb.binding.datatypes.string, required=True)
    __folder._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 977, 4)
    __folder._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 977, 4)
    
    folder = property(__folder.value, __folder.set, None, None)

    
    # Attribute archive uses Python identifier archive
    __archive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'archive'), 'archive', '__AbsentNamespace0_ExampleType_archive', pyxb.binding.datatypes.string)
    __archive._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 979, 4)
    __archive._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 979, 4)
    
    archive = property(__archive.value, __archive.set, None, None)

    
    # Attribute doc uses Python identifier doc
    __doc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'doc'), 'doc', '__AbsentNamespace0_ExampleType_doc', pyxb.binding.datatypes.string, required=True)
    __doc._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 981, 4)
    __doc._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 981, 4)
    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_ExampleType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 983, 4)
    __version._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 983, 4)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __board.name() : __board,
        __project.name() : __project,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        __name.name() : __name,
        __folder.name() : __folder,
        __archive.name() : __archive,
        __doc.name() : __doc,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', 'ExampleType', ExampleType)


# Complex type ExamplesType with content type ELEMENT_ONLY
class ExamplesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ExamplesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExamplesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 987, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element example uses Python identifier example
    __example = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'example'), 'example', '__AbsentNamespace0_ExamplesType_example', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 989, 6), )

    
    example = property(__example.value, __example.set, None, None)

    _ElementMap.update({
        __example.name() : __example
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ExamplesType', ExamplesType)


# Complex type KeywordsType with content type ELEMENT_ONLY
class KeywordsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type KeywordsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'KeywordsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 993, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keyword'), 'keyword', '__AbsentNamespace0_KeywordsType_keyword', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 995, 6), )

    
    keyword = property(__keyword.value, __keyword.set, None, None)

    _ElementMap.update({
        __keyword.name() : __keyword
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'KeywordsType', KeywordsType)


# Complex type ReleasesType with content type ELEMENT_ONLY
class ReleasesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ReleasesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleasesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1060, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element release uses Python identifier release
    __release = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'release'), 'release', '__AbsentNamespace0_ReleasesType_release', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1062, 6), )

    
    release = property(__release.value, __release.set, None, None)

    _ElementMap.update({
        __release.name() : __release
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ReleasesType', ReleasesType)


# Complex type GeneratorCommandArgumentType with content type SIMPLE
class GeneratorCommandArgumentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GeneratorCommandArgumentType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneratorCommandArgumentType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1086, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute switch uses Python identifier switch
    __switch = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'switch'), 'switch', '__AbsentNamespace0_GeneratorCommandArgumentType_switch', pyxb.binding.datatypes.string)
    __switch._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1089, 8)
    __switch._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1089, 8)
    
    switch = property(__switch.value, __switch.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __switch.name() : __switch
    })
Namespace.addCategoryObject('typeBinding', 'GeneratorCommandArgumentType', GeneratorCommandArgumentType)


# Complex type GeneratorCommandArgumentsType with content type ELEMENT_ONLY
class GeneratorCommandArgumentsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GeneratorCommandArgumentsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneratorCommandArgumentsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1094, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element argument uses Python identifier argument
    __argument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'argument'), 'argument', '__AbsentNamespace0_GeneratorCommandArgumentsType_argument', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1096, 6), )

    
    argument = property(__argument.value, __argument.set, None, None)

    _ElementMap.update({
        __argument.name() : __argument
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GeneratorCommandArgumentsType', GeneratorCommandArgumentsType)


# Complex type GpdscFileType with content type EMPTY
class GpdscFileType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GpdscFileType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GpdscFileType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1100, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_GpdscFileType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1101, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1101, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'GpdscFileType', GpdscFileType)


# Complex type GeneratorType with content type ELEMENT_ONLY
class GeneratorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GeneratorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneratorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1105, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_GeneratorType_description', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1107, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element select uses Python identifier select
    __select = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'select'), 'select', '__AbsentNamespace0_GeneratorType_select', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1108, 6), )

    
    select = property(__select.value, __select.set, None, None)

    
    # Element command uses Python identifier command
    __command = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'command'), 'command', '__AbsentNamespace0_GeneratorType_command', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1109, 6), )

    
    command = property(__command.value, __command.set, None, None)

    
    # Element workingDir uses Python identifier workingDir
    __workingDir = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'workingDir'), 'workingDir', '__AbsentNamespace0_GeneratorType_workingDir', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1110, 6), )

    
    workingDir = property(__workingDir.value, __workingDir.set, None, None)

    
    # Element arguments uses Python identifier arguments
    __arguments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'arguments'), 'arguments', '__AbsentNamespace0_GeneratorType_arguments', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1111, 6), )

    
    arguments = property(__arguments.value, __arguments.set, None, None)

    
    # Element gpdsc uses Python identifier gpdsc
    __gpdsc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gpdsc'), 'gpdsc', '__AbsentNamespace0_GeneratorType_gpdsc', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1112, 6), )

    
    gpdsc = property(__gpdsc.value, __gpdsc.set, None, None)

    
    # Element project_files uses Python identifier project_files
    __project_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'project_files'), 'project_files', '__AbsentNamespace0_GeneratorType_project_files', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1114, 6), )

    
    project_files = property(__project_files.value, __project_files.set, None, None)

    
    # Element files uses Python identifier files
    __files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'files'), 'files', '__AbsentNamespace0_GeneratorType_files', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1122, 6), )

    
    files = property(__files.value, __files.set, None, None)

    
    # Element extensions uses Python identifier extensions
    __extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'extensions'), 'extensions', '__AbsentNamespace0_GeneratorType_extensions', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1131, 6), )

    
    extensions = property(__extensions.value, __extensions.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_GeneratorType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1140, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1140, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute Gvendor uses Python identifier Gvendor
    __Gvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Gvendor'), 'Gvendor', '__AbsentNamespace0_GeneratorType_Gvendor', pyxb.binding.datatypes.string)
    __Gvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1141, 4)
    __Gvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1141, 4)
    
    Gvendor = property(__Gvendor.value, __Gvendor.set, None, None)

    
    # Attribute Gtool uses Python identifier Gtool
    __Gtool = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Gtool'), 'Gtool', '__AbsentNamespace0_GeneratorType_Gtool', pyxb.binding.datatypes.string)
    __Gtool._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1142, 4)
    __Gtool._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1142, 4)
    
    Gtool = property(__Gtool.value, __Gtool.set, None, None)

    
    # Attribute Gversion uses Python identifier Gversion
    __Gversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Gversion'), 'Gversion', '__AbsentNamespace0_GeneratorType_Gversion', pyxb.binding.datatypes.string)
    __Gversion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1143, 4)
    __Gversion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1143, 4)
    
    Gversion = property(__Gversion.value, __Gversion.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __select.name() : __select,
        __command.name() : __command,
        __workingDir.name() : __workingDir,
        __arguments.name() : __arguments,
        __gpdsc.name() : __gpdsc,
        __project_files.name() : __project_files,
        __files.name() : __files,
        __extensions.name() : __extensions
    })
    _AttributeMap.update({
        __id.name() : __id,
        __Gvendor.name() : __Gvendor,
        __Gtool.name() : __Gtool,
        __Gversion.name() : __Gversion
    })
Namespace.addCategoryObject('typeBinding', 'GeneratorType', GeneratorType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1115, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'file'), 'file', '__AbsentNamespace0_CTD_ANON_3_file', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1117, 12), )

    
    file = property(__file.value, __file.set, None, None)

    _ElementMap.update({
        __file.name() : __file
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1123, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'file'), 'file', '__AbsentNamespace0_CTD_ANON_4_file', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1126, 12), )

    
    file = property(__file.value, __file.set, None, None)

    _ElementMap.update({
        __file.name() : __file
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1132, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type GeneratorsType with content type ELEMENT_ONLY
class GeneratorsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GeneratorsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneratorsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1147, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element generator uses Python identifier generator
    __generator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'generator'), 'generator', '__AbsentNamespace0_GeneratorsType_generator', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1149, 6), )

    
    generator = property(__generator.value, __generator.set, None, None)

    _ElementMap.update({
        __generator.name() : __generator
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GeneratorsType', GeneratorsType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1176, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element family uses Python identifier family
    __family = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'family'), 'family', '__AbsentNamespace0_CTD_ANON_6_family', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1180, 14), )

    
    family = property(__family.value, __family.set, None, None)

    _ElementMap.update({
        __family.name() : __family
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1187, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element compile uses Python identifier compile
    __compile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'compile'), 'compile', '__AbsentNamespace0_CTD_ANON_7_compile', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6), )

    
    compile = property(__compile.value, __compile.set, None, None)

    
    # Element memory uses Python identifier memory
    __memory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'memory'), 'memory', '__AbsentNamespace0_CTD_ANON_7_memory', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6), )

    
    memory = property(__memory.value, __memory.set, None, None)

    
    # Element algorithm uses Python identifier algorithm
    __algorithm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'algorithm'), 'algorithm', '__AbsentNamespace0_CTD_ANON_7_algorithm', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6), )

    
    algorithm = property(__algorithm.value, __algorithm.set, None, None)

    
    # Element book uses Python identifier book
    __book = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'book'), 'book', '__AbsentNamespace0_CTD_ANON_7_book', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6), )

    
    book = property(__book.value, __book.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_7_description', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element feature uses Python identifier feature
    __feature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'feature'), 'feature', '__AbsentNamespace0_CTD_ANON_7_feature', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6), )

    
    feature = property(__feature.value, __feature.set, None, None)

    
    # Element environment uses Python identifier environment
    __environment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'environment'), 'environment', '__AbsentNamespace0_CTD_ANON_7_environment', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6), )

    
    environment = property(__environment.value, __environment.set, None, None)

    
    # Element debugport uses Python identifier debugport
    __debugport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugport'), 'debugport', '__AbsentNamespace0_CTD_ANON_7_debugport', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6), )

    
    debugport = property(__debugport.value, __debugport.set, None, None)

    
    # Element debug uses Python identifier debug
    __debug = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debug'), 'debug', '__AbsentNamespace0_CTD_ANON_7_debug', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6), )

    
    debug = property(__debug.value, __debug.set, None, None)

    
    # Element trace uses Python identifier trace
    __trace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trace'), 'trace', '__AbsentNamespace0_CTD_ANON_7_trace', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6), )

    
    trace = property(__trace.value, __trace.set, None, None)

    
    # Element debugvars uses Python identifier debugvars
    __debugvars = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugvars'), 'debugvars', '__AbsentNamespace0_CTD_ANON_7_debugvars', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6), )

    
    debugvars = property(__debugvars.value, __debugvars.set, None, None)

    
    # Element sequences uses Python identifier sequences
    __sequences = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sequences'), 'sequences', '__AbsentNamespace0_CTD_ANON_7_sequences', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6), )

    
    sequences = property(__sequences.value, __sequences.set, None, None)

    
    # Element processor uses Python identifier processor
    __processor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'processor'), 'processor', '__AbsentNamespace0_CTD_ANON_7_processor', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6), )

    
    processor = property(__processor.value, __processor.set, None, None)

    
    # Element debugconfig uses Python identifier debugconfig
    __debugconfig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugconfig'), 'debugconfig', '__AbsentNamespace0_CTD_ANON_7_debugconfig', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6), )

    
    debugconfig = property(__debugconfig.value, __debugconfig.set, None, None)

    
    # Element device uses Python identifier device
    __device = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device'), 'device', '__AbsentNamespace0_CTD_ANON_7_device', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1191, 26), )

    
    device = property(__device.value, __device.set, None, None)

    
    # Attribute DsubFamily uses Python identifier DsubFamily
    __DsubFamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DsubFamily'), 'DsubFamily', '__AbsentNamespace0_CTD_ANON_7_DsubFamily', pyxb.binding.datatypes.string, required=True)
    __DsubFamily._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1194, 24)
    __DsubFamily._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1194, 24)
    
    DsubFamily = property(__DsubFamily.value, __DsubFamily.set, None, None)

    _ElementMap.update({
        __compile.name() : __compile,
        __memory.name() : __memory,
        __algorithm.name() : __algorithm,
        __book.name() : __book,
        __description.name() : __description,
        __feature.name() : __feature,
        __environment.name() : __environment,
        __debugport.name() : __debugport,
        __debug.name() : __debug,
        __trace.name() : __trace,
        __debugvars.name() : __debugvars,
        __sequences.name() : __sequences,
        __processor.name() : __processor,
        __debugconfig.name() : __debugconfig,
        __device.name() : __device
    })
    _AttributeMap.update({
        __DsubFamily.name() : __DsubFamily
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1221, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element bundle uses Python identifier bundle
    __bundle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bundle'), 'bundle', '__AbsentNamespace0_CTD_ANON_8_bundle', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1224, 14), )

    
    bundle = property(__bundle.value, __bundle.set, None, None)

    
    # Element component uses Python identifier component
    __component = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'component'), 'component', '__AbsentNamespace0_CTD_ANON_8_component', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1271, 14), )

    
    component = property(__component.value, __component.set, None, None)

    
    # Attribute generator uses Python identifier generator
    __generator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'generator'), 'generator', '__AbsentNamespace0_CTD_ANON_8_generator', pyxb.binding.datatypes.string)
    __generator._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1307, 12)
    __generator._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1307, 12)
    
    generator = property(__generator.value, __generator.set, None, None)

    _ElementMap.update({
        __bundle.name() : __bundle,
        __component.name() : __component
    })
    _AttributeMap.update({
        __generator.name() : __generator
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1240, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'file'), 'file', '__AbsentNamespace0_CTD_ANON_9_file', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1242, 32), )

    
    file = property(__file.value, __file.set, None, None)

    _ElementMap.update({
        __file.name() : __file
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1282, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'file'), 'file', '__AbsentNamespace0_CTD_ANON_10_file', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1284, 26), )

    
    file = property(__file.value, __file.set, None, None)

    _ElementMap.update({
        __file.name() : __file
    })
    _AttributeMap.update({
        
    })



# Complex type ProcessorType with content type EMPTY
class ProcessorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ProcessorType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 154, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_ProcessorType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 156, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 156, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    
    # Attribute Dcore uses Python identifier Dcore
    __Dcore = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dcore'), 'Dcore', '__AbsentNamespace0_ProcessorType_Dcore', DcoreEnum)
    __Dcore._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 158, 4)
    __Dcore._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 158, 4)
    
    Dcore = property(__Dcore.value, __Dcore.set, None, None)

    
    # Attribute Dfpu uses Python identifier Dfpu
    __Dfpu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dfpu'), 'Dfpu', '__AbsentNamespace0_ProcessorType_Dfpu', DfpuEnum)
    __Dfpu._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 160, 4)
    __Dfpu._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 160, 4)
    
    Dfpu = property(__Dfpu.value, __Dfpu.set, None, None)

    
    # Attribute Dmpu uses Python identifier Dmpu
    __Dmpu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dmpu'), 'Dmpu', '__AbsentNamespace0_ProcessorType_Dmpu', DmpuEnum)
    __Dmpu._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 162, 4)
    __Dmpu._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 162, 4)
    
    Dmpu = property(__Dmpu.value, __Dmpu.set, None, None)

    
    # Attribute Dendian uses Python identifier Dendian
    __Dendian = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dendian'), 'Dendian', '__AbsentNamespace0_ProcessorType_Dendian', DendianEnum)
    __Dendian._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 164, 4)
    __Dendian._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 164, 4)
    
    Dendian = property(__Dendian.value, __Dendian.set, None, None)

    
    # Attribute Dclock uses Python identifier Dclock
    __Dclock = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dclock'), 'Dclock', '__AbsentNamespace0_ProcessorType_Dclock', pyxb.binding.datatypes.unsignedInt)
    __Dclock._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 166, 4)
    __Dclock._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 166, 4)
    
    Dclock = property(__Dclock.value, __Dclock.set, None, None)

    
    # Attribute DcoreVersion uses Python identifier DcoreVersion
    __DcoreVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DcoreVersion'), 'DcoreVersion', '__AbsentNamespace0_ProcessorType_DcoreVersion', pyxb.binding.datatypes.string)
    __DcoreVersion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 168, 4)
    __DcoreVersion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 168, 4)
    
    DcoreVersion = property(__DcoreVersion.value, __DcoreVersion.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Pname.name() : __Pname,
        __Dcore.name() : __Dcore,
        __Dfpu.name() : __Dfpu,
        __Dmpu.name() : __Dmpu,
        __Dendian.name() : __Dendian,
        __Dclock.name() : __Dclock,
        __DcoreVersion.name() : __DcoreVersion
    })
Namespace.addCategoryObject('typeBinding', 'ProcessorType', ProcessorType)


# Complex type CompileType with content type EMPTY
class CompileType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CompileType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompileType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 172, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_CompileType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 174, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 174, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    
    # Attribute header uses Python identifier header
    __header = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'header'), 'header', '__AbsentNamespace0_CompileType_header', pyxb.binding.datatypes.string)
    __header._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 176, 4)
    __header._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 176, 4)
    
    header = property(__header.value, __header.set, None, None)

    
    # Attribute define uses Python identifier define
    __define = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'define'), 'define', '__AbsentNamespace0_CompileType_define', pyxb.binding.datatypes.string)
    __define._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 178, 4)
    __define._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 178, 4)
    
    define = property(__define.value, __define.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Pname.name() : __Pname,
        __header.name() : __header,
        __define.name() : __define
    })
Namespace.addCategoryObject('typeBinding', 'CompileType', CompileType)


# Complex type DebugVarsType with content type SIMPLE
class DebugVarsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DebugVarsType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DebugVarsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 182, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute configfile uses Python identifier configfile
    __configfile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'configfile'), 'configfile', '__AbsentNamespace0_DebugVarsType_configfile', pyxb.binding.datatypes.string)
    __configfile._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 185, 8)
    __configfile._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 185, 8)
    
    configfile = property(__configfile.value, __configfile.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_DebugVarsType_version', VersionType)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 186, 8)
    __version._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 186, 8)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_DebugVarsType_Pname', pyxb.binding.datatypes.string)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 187, 8)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 187, 8)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __configfile.name() : __configfile,
        __version.name() : __version,
        __Pname.name() : __Pname
    })
Namespace.addCategoryObject('typeBinding', 'DebugVarsType', DebugVarsType)


# Complex type DebugConfigType with content type EMPTY
class DebugConfigType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DebugConfigType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DebugConfigType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 202, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute default uses Python identifier default
    __default = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'default'), 'default', '__AbsentNamespace0_DebugConfigType_default', DebugProtocolEnum)
    __default._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 203, 4)
    __default._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 203, 4)
    
    default = property(__default.value, __default.set, None, None)

    
    # Attribute clock uses Python identifier clock
    __clock = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'clock'), 'clock', '__AbsentNamespace0_DebugConfigType_clock', pyxb.binding.datatypes.unsignedInt)
    __clock._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 204, 4)
    __clock._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 204, 4)
    
    clock = property(__clock.value, __clock.set, None, None)

    
    # Attribute swj uses Python identifier swj
    __swj = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'swj'), 'swj', '__AbsentNamespace0_DebugConfigType_swj', pyxb.binding.datatypes.boolean)
    __swj._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 205, 4)
    __swj._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 205, 4)
    
    swj = property(__swj.value, __swj.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __default.name() : __default,
        __clock.name() : __clock,
        __swj.name() : __swj
    })
Namespace.addCategoryObject('typeBinding', 'DebugConfigType', DebugConfigType)


# Complex type JtagType with content type EMPTY
class JtagType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type JtagType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JtagType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 210, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tapindex uses Python identifier tapindex
    __tapindex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tapindex'), 'tapindex', '__AbsentNamespace0_JtagType_tapindex', NonNegativeInteger)
    __tapindex._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 211, 4)
    __tapindex._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 211, 4)
    
    tapindex = property(__tapindex.value, __tapindex.set, None, None)

    
    # Attribute idcode uses Python identifier idcode
    __idcode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'idcode'), 'idcode', '__AbsentNamespace0_JtagType_idcode', NonNegativeInteger)
    __idcode._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 212, 4)
    __idcode._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 212, 4)
    
    idcode = property(__idcode.value, __idcode.set, None, None)

    
    # Attribute targetsel uses Python identifier targetsel
    __targetsel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetsel'), 'targetsel', '__AbsentNamespace0_JtagType_targetsel', NonNegativeInteger)
    __targetsel._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 213, 4)
    __targetsel._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 213, 4)
    
    targetsel = property(__targetsel.value, __targetsel.set, None, None)

    
    # Attribute irlen uses Python identifier irlen
    __irlen = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'irlen'), 'irlen', '__AbsentNamespace0_JtagType_irlen', pyxb.binding.datatypes.unsignedInt)
    __irlen._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 214, 4)
    __irlen._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 214, 4)
    
    irlen = property(__irlen.value, __irlen.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tapindex.name() : __tapindex,
        __idcode.name() : __idcode,
        __targetsel.name() : __targetsel,
        __irlen.name() : __irlen
    })
Namespace.addCategoryObject('typeBinding', 'JtagType', JtagType)


# Complex type SwdType with content type EMPTY
class SwdType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SwdType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SwdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 219, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute idcode uses Python identifier idcode
    __idcode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'idcode'), 'idcode', '__AbsentNamespace0_SwdType_idcode', NonNegativeInteger)
    __idcode._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 220, 4)
    __idcode._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 220, 4)
    
    idcode = property(__idcode.value, __idcode.set, None, None)

    
    # Attribute targetsel uses Python identifier targetsel
    __targetsel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetsel'), 'targetsel', '__AbsentNamespace0_SwdType_targetsel', NonNegativeInteger)
    __targetsel._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 221, 4)
    __targetsel._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 221, 4)
    
    targetsel = property(__targetsel.value, __targetsel.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __idcode.name() : __idcode,
        __targetsel.name() : __targetsel
    })
Namespace.addCategoryObject('typeBinding', 'SwdType', SwdType)


# Complex type DataPatchType with content type EMPTY
class DataPatchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DataPatchType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataPatchType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 250, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_DataPatchType_type', DataPatchAccessTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 251, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 251, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute address uses Python identifier address
    __address = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'address'), 'address', '__AbsentNamespace0_DataPatchType_address', NonNegativeInteger, required=True)
    __address._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 252, 4)
    __address._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 252, 4)
    
    address = property(__address.value, __address.set, None, None)

    
    # Attribute __dp uses Python identifier dp
    __dp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, '__dp'), 'dp', '__AbsentNamespace0_DataPatchType___dp', pyxb.binding.datatypes.unsignedInt)
    __dp._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 253, 4)
    __dp._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 253, 4)
    
    dp = property(__dp.value, __dp.set, None, None)

    
    # Attribute __ap uses Python identifier ap
    __ap = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, '__ap'), 'ap', '__AbsentNamespace0_DataPatchType___ap', pyxb.binding.datatypes.unsignedInt)
    __ap._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 254, 4)
    __ap._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 254, 4)
    
    ap = property(__ap.value, __ap.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_DataPatchType_value', NonNegativeInteger, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 255, 4)
    __value._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 255, 4)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute mask uses Python identifier mask
    __mask = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mask'), 'mask', '__AbsentNamespace0_DataPatchType_mask', NonNegativeInteger)
    __mask._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 256, 4)
    __mask._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 256, 4)
    
    mask = property(__mask.value, __mask.set, None, None)

    
    # Attribute info uses Python identifier info
    __info = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'info'), 'info', '__AbsentNamespace0_DataPatchType_info', pyxb.binding.datatypes.string)
    __info._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 257, 4)
    __info._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 257, 4)
    
    info = property(__info.value, __info.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __address.name() : __address,
        __dp.name() : __dp,
        __ap.name() : __ap,
        __value.name() : __value,
        __mask.name() : __mask,
        __info.name() : __info
    })
Namespace.addCategoryObject('typeBinding', 'DataPatchType', DataPatchType)


# Complex type SequenceControlType with content type ELEMENT_ONLY
class SequenceControlType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SequenceControlType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequenceControlType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 273, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element block uses Python identifier block
    __block = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'block'), 'block', '__AbsentNamespace0_SequenceControlType_block', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 287, 6), )

    
    block = property(__block.value, __block.set, None, None)

    
    # Element control uses Python identifier control
    __control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'control'), 'control', '__AbsentNamespace0_SequenceControlType_control', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 288, 6), )

    
    control = property(__control.value, __control.set, None, None)

    
    # Attribute if uses Python identifier if_
    __if = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'if'), 'if_', '__AbsentNamespace0_SequenceControlType_if', pyxb.binding.datatypes.string)
    __if._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 277, 4)
    __if._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 277, 4)
    
    if_ = property(__if.value, __if.set, None, None)

    
    # Attribute while uses Python identifier while_
    __while = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'while'), 'while_', '__AbsentNamespace0_SequenceControlType_while', ExpressionType)
    __while._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 278, 4)
    __while._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 278, 4)
    
    while_ = property(__while.value, __while.set, None, None)

    
    # Attribute timeout uses Python identifier timeout
    __timeout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timeout'), 'timeout', '__AbsentNamespace0_SequenceControlType_timeout', pyxb.binding.datatypes.unsignedInt)
    __timeout._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 279, 4)
    __timeout._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 279, 4)
    
    timeout = property(__timeout.value, __timeout.set, None, None)

    
    # Attribute info uses Python identifier info
    __info = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'info'), 'info', '__AbsentNamespace0_SequenceControlType_info', pyxb.binding.datatypes.string)
    __info._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 280, 4)
    __info._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 280, 4)
    
    info = property(__info.value, __info.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __block.name() : __block,
        __control.name() : __control
    })
    _AttributeMap.update({
        __if.name() : __if,
        __while.name() : __while,
        __timeout.name() : __timeout,
        __info.name() : __info
    })
Namespace.addCategoryObject('typeBinding', 'SequenceControlType', SequenceControlType)


# Complex type SequenceType with content type ELEMENT_ONLY
class SequenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SequenceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 294, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element block uses Python identifier block
    __block = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'block'), 'block', '__AbsentNamespace0_SequenceType_block', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 287, 6), )

    
    block = property(__block.value, __block.set, None, None)

    
    # Element control uses Python identifier control
    __control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'control'), 'control', '__AbsentNamespace0_SequenceType_control', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 288, 6), )

    
    control = property(__control.value, __control.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_SequenceType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 298, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 298, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_SequenceType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 299, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 299, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    
    # Attribute disable uses Python identifier disable
    __disable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'disable'), 'disable', '__AbsentNamespace0_SequenceType_disable', pyxb.binding.datatypes.boolean)
    __disable._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 300, 4)
    __disable._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 300, 4)
    
    disable = property(__disable.value, __disable.set, None, None)

    
    # Attribute info uses Python identifier info
    __info = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'info'), 'info', '__AbsentNamespace0_SequenceType_info', pyxb.binding.datatypes.string)
    __info._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 301, 4)
    __info._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 301, 4)
    
    info = property(__info.value, __info.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __block.name() : __block,
        __control.name() : __control
    })
    _AttributeMap.update({
        __name.name() : __name,
        __Pname.name() : __Pname,
        __disable.name() : __disable,
        __info.name() : __info
    })
Namespace.addCategoryObject('typeBinding', 'SequenceType', SequenceType)


# Complex type DebugType with content type ELEMENT_ONLY
class DebugType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DebugType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DebugType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 314, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element datapatch uses Python identifier datapatch
    __datapatch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'datapatch'), 'datapatch', '__AbsentNamespace0_DebugType_datapatch', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 316, 6), )

    
    datapatch = property(__datapatch.value, __datapatch.set, None, None)

    
    # Attribute __dp uses Python identifier dp
    __dp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, '__dp'), 'dp', '__AbsentNamespace0_DebugType___dp', pyxb.binding.datatypes.unsignedInt)
    __dp._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 318, 4)
    __dp._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 318, 4)
    
    dp = property(__dp.value, __dp.set, None, None)

    
    # Attribute __ap uses Python identifier ap
    __ap = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, '__ap'), 'ap', '__AbsentNamespace0_DebugType___ap', pyxb.binding.datatypes.unsignedInt)
    __ap._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 319, 4)
    __ap._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 319, 4)
    
    ap = property(__ap.value, __ap.set, None, None)

    
    # Attribute svd uses Python identifier svd
    __svd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'svd'), 'svd', '__AbsentNamespace0_DebugType_svd', pyxb.binding.datatypes.string)
    __svd._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 320, 4)
    __svd._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 320, 4)
    
    svd = property(__svd.value, __svd.set, None, None)

    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_DebugType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 321, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 321, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __datapatch.name() : __datapatch
    })
    _AttributeMap.update({
        __dp.name() : __dp,
        __ap.name() : __ap,
        __svd.name() : __svd,
        __Pname.name() : __Pname
    })
Namespace.addCategoryObject('typeBinding', 'DebugType', DebugType)


# Complex type TracePortType with content type EMPTY
class TracePortType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TracePortType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TracePortType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 331, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_TracePortType_width', NonNegativeInteger)
    __width._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 332, 4)
    __width._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 332, 4)
    
    width = property(__width.value, __width.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __width.name() : __width
    })
Namespace.addCategoryObject('typeBinding', 'TracePortType', TracePortType)


# Complex type TraceBufferType with content type EMPTY
class TraceBufferType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TraceBufferType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TraceBufferType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 337, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__AbsentNamespace0_TraceBufferType_start', NonNegativeInteger)
    __start._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 338, 4)
    __start._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 338, 4)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_TraceBufferType_size', NonNegativeInteger)
    __size._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 339, 4)
    __size._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 339, 4)
    
    size = property(__size.value, __size.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __start.name() : __start,
        __size.name() : __size
    })
Namespace.addCategoryObject('typeBinding', 'TraceBufferType', TraceBufferType)


# Complex type TraceType with content type ELEMENT_ONLY
class TraceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TraceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TraceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 344, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element serialwire uses Python identifier serialwire
    __serialwire = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'serialwire'), 'serialwire', '__AbsentNamespace0_TraceType_serialwire', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 346, 6), )

    
    serialwire = property(__serialwire.value, __serialwire.set, None, None)

    
    # Element traceport uses Python identifier traceport
    __traceport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'traceport'), 'traceport', '__AbsentNamespace0_TraceType_traceport', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 347, 6), )

    
    traceport = property(__traceport.value, __traceport.set, None, None)

    
    # Element tracebuffer uses Python identifier tracebuffer
    __tracebuffer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tracebuffer'), 'tracebuffer', '__AbsentNamespace0_TraceType_tracebuffer', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 348, 6), )

    
    tracebuffer = property(__tracebuffer.value, __tracebuffer.set, None, None)

    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_TraceType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 350, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 350, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __serialwire.name() : __serialwire,
        __traceport.name() : __traceport,
        __tracebuffer.name() : __tracebuffer
    })
    _AttributeMap.update({
        __Pname.name() : __Pname
    })
Namespace.addCategoryObject('typeBinding', 'TraceType', TraceType)


# Complex type MemoryType with content type EMPTY
class MemoryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MemoryType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MemoryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 355, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_MemoryType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 357, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 357, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_MemoryType_id', MemoryIDTypeEnum, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 359, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 359, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__AbsentNamespace0_MemoryType_start', NonNegativeInteger, required=True)
    __start._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 361, 4)
    __start._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 361, 4)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_MemoryType_size', NonNegativeInteger, required=True)
    __size._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 363, 4)
    __size._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 363, 4)
    
    size = property(__size.value, __size.set, None, None)

    
    # Attribute init uses Python identifier init
    __init = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'init'), 'init', '__AbsentNamespace0_MemoryType_init', pyxb.binding.datatypes.boolean, unicode_default='0')
    __init._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 365, 4)
    __init._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 365, 4)
    
    init = property(__init.value, __init.set, None, None)

    
    # Attribute default uses Python identifier default
    __default = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'default'), 'default', '__AbsentNamespace0_MemoryType_default', pyxb.binding.datatypes.boolean, unicode_default='0')
    __default._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 367, 4)
    __default._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 367, 4)
    
    default = property(__default.value, __default.set, None, None)

    
    # Attribute startup uses Python identifier startup
    __startup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'startup'), 'startup', '__AbsentNamespace0_MemoryType_startup', pyxb.binding.datatypes.boolean, unicode_default='0')
    __startup._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 369, 4)
    __startup._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 369, 4)
    
    startup = property(__startup.value, __startup.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Pname.name() : __Pname,
        __id.name() : __id,
        __start.name() : __start,
        __size.name() : __size,
        __init.name() : __init,
        __default.name() : __default,
        __startup.name() : __startup
    })
Namespace.addCategoryObject('typeBinding', 'MemoryType', MemoryType)


# Complex type AlgorithmType with content type EMPTY
class AlgorithmType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type AlgorithmType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlgorithmType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 373, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_AlgorithmType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 375, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 375, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_AlgorithmType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 377, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 377, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__AbsentNamespace0_AlgorithmType_start', NonNegativeInteger)
    __start._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 379, 4)
    __start._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 379, 4)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_AlgorithmType_size', NonNegativeInteger)
    __size._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 381, 4)
    __size._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 381, 4)
    
    size = property(__size.value, __size.set, None, None)

    
    # Attribute RAMstart uses Python identifier RAMstart
    __RAMstart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'RAMstart'), 'RAMstart', '__AbsentNamespace0_AlgorithmType_RAMstart', NonNegativeInteger)
    __RAMstart._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 383, 4)
    __RAMstart._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 383, 4)
    
    RAMstart = property(__RAMstart.value, __RAMstart.set, None, None)

    
    # Attribute RAMsize uses Python identifier RAMsize
    __RAMsize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'RAMsize'), 'RAMsize', '__AbsentNamespace0_AlgorithmType_RAMsize', NonNegativeInteger)
    __RAMsize._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 385, 4)
    __RAMsize._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 385, 4)
    
    RAMsize = property(__RAMsize.value, __RAMsize.set, None, None)

    
    # Attribute default uses Python identifier default
    __default = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'default'), 'default', '__AbsentNamespace0_AlgorithmType_default', pyxb.binding.datatypes.boolean, unicode_default='0')
    __default._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 387, 4)
    __default._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 387, 4)
    
    default = property(__default.value, __default.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Pname.name() : __Pname,
        __name.name() : __name,
        __start.name() : __start,
        __size.name() : __size,
        __RAMstart.name() : __RAMstart,
        __RAMsize.name() : __RAMsize,
        __default.name() : __default
    })
Namespace.addCategoryObject('typeBinding', 'AlgorithmType', AlgorithmType)


# Complex type BookType with content type EMPTY
class BookType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BookType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BookType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 391, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_BookType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 393, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 393, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_BookType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 395, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 395, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__AbsentNamespace0_BookType_title', pyxb.binding.datatypes.string, required=True)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 397, 4)
    __title._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 397, 4)
    
    title = property(__title.value, __title.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Pname.name() : __Pname,
        __name.name() : __name,
        __title.name() : __title
    })
Namespace.addCategoryObject('typeBinding', 'BookType', BookType)


# Complex type DescriptionType with content type SIMPLE
class DescriptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DescriptionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 401, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_DescriptionType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 405, 8)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 405, 8)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Pname.name() : __Pname
    })
Namespace.addCategoryObject('typeBinding', 'DescriptionType', DescriptionType)


# Complex type DeviceFeatureType with content type EMPTY
class DeviceFeatureType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DeviceFeatureType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeviceFeatureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 411, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_DeviceFeatureType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 412, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 412, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_DeviceFeatureType_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 414, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 414, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute n uses Python identifier n
    __n = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'n'), 'n', '__AbsentNamespace0_DeviceFeatureType_n', pyxb.binding.datatypes.decimal)
    __n._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 415, 4)
    __n._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 415, 4)
    
    n = property(__n.value, __n.set, None, None)

    
    # Attribute m uses Python identifier m
    __m = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'm'), 'm', '__AbsentNamespace0_DeviceFeatureType_m', pyxb.binding.datatypes.decimal)
    __m._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 416, 4)
    __m._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 416, 4)
    
    m = property(__m.value, __m.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_DeviceFeatureType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 417, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 417, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute count uses Python identifier count
    __count = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'count'), 'count', '__AbsentNamespace0_DeviceFeatureType_count', pyxb.binding.datatypes.int)
    __count._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 419, 4)
    __count._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 419, 4)
    
    count = property(__count.value, __count.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Pname.name() : __Pname,
        __type.name() : __type,
        __n.name() : __n,
        __m.name() : __m,
        __name.name() : __name,
        __count.name() : __count
    })
Namespace.addCategoryObject('typeBinding', 'DeviceFeatureType', DeviceFeatureType)


# Complex type EnvironmentType with content type ELEMENT_ONLY
class EnvironmentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type EnvironmentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EnvironmentType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 432, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_EnvironmentType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 437, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 437, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_EnvironmentType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 439, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 439, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __Pname.name() : __Pname
    })
Namespace.addCategoryObject('typeBinding', 'EnvironmentType', EnvironmentType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 477, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element compile uses Python identifier compile
    __compile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'compile'), 'compile', '__AbsentNamespace0_CTD_ANON_11_compile', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6), )

    
    compile = property(__compile.value, __compile.set, None, None)

    
    # Element memory uses Python identifier memory
    __memory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'memory'), 'memory', '__AbsentNamespace0_CTD_ANON_11_memory', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6), )

    
    memory = property(__memory.value, __memory.set, None, None)

    
    # Element algorithm uses Python identifier algorithm
    __algorithm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'algorithm'), 'algorithm', '__AbsentNamespace0_CTD_ANON_11_algorithm', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6), )

    
    algorithm = property(__algorithm.value, __algorithm.set, None, None)

    
    # Element book uses Python identifier book
    __book = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'book'), 'book', '__AbsentNamespace0_CTD_ANON_11_book', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6), )

    
    book = property(__book.value, __book.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_11_description', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element feature uses Python identifier feature
    __feature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'feature'), 'feature', '__AbsentNamespace0_CTD_ANON_11_feature', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6), )

    
    feature = property(__feature.value, __feature.set, None, None)

    
    # Element environment uses Python identifier environment
    __environment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'environment'), 'environment', '__AbsentNamespace0_CTD_ANON_11_environment', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6), )

    
    environment = property(__environment.value, __environment.set, None, None)

    
    # Element debugport uses Python identifier debugport
    __debugport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugport'), 'debugport', '__AbsentNamespace0_CTD_ANON_11_debugport', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6), )

    
    debugport = property(__debugport.value, __debugport.set, None, None)

    
    # Element debug uses Python identifier debug
    __debug = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debug'), 'debug', '__AbsentNamespace0_CTD_ANON_11_debug', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6), )

    
    debug = property(__debug.value, __debug.set, None, None)

    
    # Element trace uses Python identifier trace
    __trace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trace'), 'trace', '__AbsentNamespace0_CTD_ANON_11_trace', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6), )

    
    trace = property(__trace.value, __trace.set, None, None)

    
    # Element debugvars uses Python identifier debugvars
    __debugvars = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugvars'), 'debugvars', '__AbsentNamespace0_CTD_ANON_11_debugvars', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6), )

    
    debugvars = property(__debugvars.value, __debugvars.set, None, None)

    
    # Element sequences uses Python identifier sequences
    __sequences = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sequences'), 'sequences', '__AbsentNamespace0_CTD_ANON_11_sequences', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6), )

    
    sequences = property(__sequences.value, __sequences.set, None, None)

    
    # Element processor uses Python identifier processor
    __processor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'processor'), 'processor', '__AbsentNamespace0_CTD_ANON_11_processor', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6), )

    
    processor = property(__processor.value, __processor.set, None, None)

    
    # Element debugconfig uses Python identifier debugconfig
    __debugconfig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugconfig'), 'debugconfig', '__AbsentNamespace0_CTD_ANON_11_debugconfig', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6), )

    
    debugconfig = property(__debugconfig.value, __debugconfig.set, None, None)

    
    # Attribute Dvariant uses Python identifier Dvariant
    __Dvariant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dvariant'), 'Dvariant', '__AbsentNamespace0_CTD_ANON_11_Dvariant', RestrictedString, required=True)
    __Dvariant._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 481, 10)
    __Dvariant._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 481, 10)
    
    Dvariant = property(__Dvariant.value, __Dvariant.set, None, None)

    _ElementMap.update({
        __compile.name() : __compile,
        __memory.name() : __memory,
        __algorithm.name() : __algorithm,
        __book.name() : __book,
        __description.name() : __description,
        __feature.name() : __feature,
        __environment.name() : __environment,
        __debugport.name() : __debugport,
        __debug.name() : __debug,
        __trace.name() : __trace,
        __debugvars.name() : __debugvars,
        __sequences.name() : __sequences,
        __processor.name() : __processor,
        __debugconfig.name() : __debugconfig
    })
    _AttributeMap.update({
        __Dvariant.name() : __Dvariant
    })



# Complex type FilterType with content type EMPTY
class FilterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type FilterType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FilterType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 768, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Dfamily uses Python identifier Dfamily
    __Dfamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dfamily'), 'Dfamily', '__AbsentNamespace0_FilterType_Dfamily', pyxb.binding.datatypes.string)
    __Dfamily._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 769, 4)
    __Dfamily._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 769, 4)
    
    Dfamily = property(__Dfamily.value, __Dfamily.set, None, None)

    
    # Attribute DsubFamily uses Python identifier DsubFamily
    __DsubFamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DsubFamily'), 'DsubFamily', '__AbsentNamespace0_FilterType_DsubFamily', pyxb.binding.datatypes.string)
    __DsubFamily._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 770, 4)
    __DsubFamily._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 770, 4)
    
    DsubFamily = property(__DsubFamily.value, __DsubFamily.set, None, None)

    
    # Attribute Dvariant uses Python identifier Dvariant
    __Dvariant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dvariant'), 'Dvariant', '__AbsentNamespace0_FilterType_Dvariant', pyxb.binding.datatypes.string)
    __Dvariant._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 771, 4)
    __Dvariant._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 771, 4)
    
    Dvariant = property(__Dvariant.value, __Dvariant.set, None, None)

    
    # Attribute Dvendor uses Python identifier Dvendor
    __Dvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dvendor'), 'Dvendor', '__AbsentNamespace0_FilterType_Dvendor', DeviceVendorEnum)
    __Dvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 772, 4)
    __Dvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 772, 4)
    
    Dvendor = property(__Dvendor.value, __Dvendor.set, None, None)

    
    # Attribute Dname uses Python identifier Dname
    __Dname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dname'), 'Dname', '__AbsentNamespace0_FilterType_Dname', RestrictedString)
    __Dname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 773, 4)
    __Dname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 773, 4)
    
    Dname = property(__Dname.value, __Dname.set, None, None)

    
    # Attribute Dcore uses Python identifier Dcore
    __Dcore = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dcore'), 'Dcore', '__AbsentNamespace0_FilterType_Dcore', DcoreEnum)
    __Dcore._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 774, 4)
    __Dcore._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 774, 4)
    
    Dcore = property(__Dcore.value, __Dcore.set, None, None)

    
    # Attribute Dfpu uses Python identifier Dfpu
    __Dfpu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dfpu'), 'Dfpu', '__AbsentNamespace0_FilterType_Dfpu', DfpuEnum)
    __Dfpu._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 775, 4)
    __Dfpu._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 775, 4)
    
    Dfpu = property(__Dfpu.value, __Dfpu.set, None, None)

    
    # Attribute Dmpu uses Python identifier Dmpu
    __Dmpu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dmpu'), 'Dmpu', '__AbsentNamespace0_FilterType_Dmpu', DmpuEnum)
    __Dmpu._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 776, 4)
    __Dmpu._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 776, 4)
    
    Dmpu = property(__Dmpu.value, __Dmpu.set, None, None)

    
    # Attribute Dendian uses Python identifier Dendian
    __Dendian = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dendian'), 'Dendian', '__AbsentNamespace0_FilterType_Dendian', DendianEnum)
    __Dendian._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 777, 4)
    __Dendian._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 777, 4)
    
    Dendian = property(__Dendian.value, __Dendian.set, None, None)

    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_FilterType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 778, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 778, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    
    # Attribute Cvendor uses Python identifier Cvendor
    __Cvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cvendor'), 'Cvendor', '__AbsentNamespace0_FilterType_Cvendor', pyxb.binding.datatypes.string)
    __Cvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 779, 4)
    __Cvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 779, 4)
    
    Cvendor = property(__Cvendor.value, __Cvendor.set, None, None)

    
    # Attribute Cbundle uses Python identifier Cbundle
    __Cbundle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cbundle'), 'Cbundle', '__AbsentNamespace0_FilterType_Cbundle', pyxb.binding.datatypes.string)
    __Cbundle._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 780, 4)
    __Cbundle._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 780, 4)
    
    Cbundle = property(__Cbundle.value, __Cbundle.set, None, None)

    
    # Attribute Cclass uses Python identifier Cclass
    __Cclass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cclass'), 'Cclass', '__AbsentNamespace0_FilterType_Cclass', CclassType)
    __Cclass._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 781, 4)
    __Cclass._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 781, 4)
    
    Cclass = property(__Cclass.value, __Cclass.set, None, None)

    
    # Attribute Cgroup uses Python identifier Cgroup
    __Cgroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cgroup'), 'Cgroup', '__AbsentNamespace0_FilterType_Cgroup', CgroupType)
    __Cgroup._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 782, 4)
    __Cgroup._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 782, 4)
    
    Cgroup = property(__Cgroup.value, __Cgroup.set, None, None)

    
    # Attribute Csub uses Python identifier Csub
    __Csub = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Csub'), 'Csub', '__AbsentNamespace0_FilterType_Csub', CsubType)
    __Csub._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 783, 4)
    __Csub._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 783, 4)
    
    Csub = property(__Csub.value, __Csub.set, None, None)

    
    # Attribute Cvariant uses Python identifier Cvariant
    __Cvariant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cvariant'), 'Cvariant', '__AbsentNamespace0_FilterType_Cvariant', CvariantType)
    __Cvariant._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 784, 4)
    __Cvariant._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 784, 4)
    
    Cvariant = property(__Cvariant.value, __Cvariant.set, None, None)

    
    # Attribute Cversion uses Python identifier Cversion
    __Cversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cversion'), 'Cversion', '__AbsentNamespace0_FilterType_Cversion', ConditionVersionType)
    __Cversion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 785, 4)
    __Cversion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 785, 4)
    
    Cversion = property(__Cversion.value, __Cversion.set, None, None)

    
    # Attribute Capiversion uses Python identifier Capiversion
    __Capiversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Capiversion'), 'Capiversion', '__AbsentNamespace0_FilterType_Capiversion', ConditionVersionType)
    __Capiversion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 786, 4)
    __Capiversion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 786, 4)
    
    Capiversion = property(__Capiversion.value, __Capiversion.set, None, None)

    
    # Attribute Tcompiler uses Python identifier Tcompiler
    __Tcompiler = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Tcompiler'), 'Tcompiler', '__AbsentNamespace0_FilterType_Tcompiler', CompilerEnumType)
    __Tcompiler._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 787, 4)
    __Tcompiler._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 787, 4)
    
    Tcompiler = property(__Tcompiler.value, __Tcompiler.set, None, None)

    
    # Attribute Toutput uses Python identifier Toutput
    __Toutput = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Toutput'), 'Toutput', '__AbsentNamespace0_FilterType_Toutput', CompilerOutputType)
    __Toutput._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 788, 4)
    __Toutput._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 788, 4)
    
    Toutput = property(__Toutput.value, __Toutput.set, None, None)

    
    # Attribute condition uses Python identifier condition
    __condition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'condition'), 'condition', '__AbsentNamespace0_FilterType_condition', pyxb.binding.datatypes.string)
    __condition._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 789, 4)
    __condition._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 789, 4)
    
    condition = property(__condition.value, __condition.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Dfamily.name() : __Dfamily,
        __DsubFamily.name() : __DsubFamily,
        __Dvariant.name() : __Dvariant,
        __Dvendor.name() : __Dvendor,
        __Dname.name() : __Dname,
        __Dcore.name() : __Dcore,
        __Dfpu.name() : __Dfpu,
        __Dmpu.name() : __Dmpu,
        __Dendian.name() : __Dendian,
        __Pname.name() : __Pname,
        __Cvendor.name() : __Cvendor,
        __Cbundle.name() : __Cbundle,
        __Cclass.name() : __Cclass,
        __Cgroup.name() : __Cgroup,
        __Csub.name() : __Csub,
        __Cvariant.name() : __Cvariant,
        __Cversion.name() : __Cversion,
        __Capiversion.name() : __Capiversion,
        __Tcompiler.name() : __Tcompiler,
        __Toutput.name() : __Toutput,
        __condition.name() : __condition
    })
Namespace.addCategoryObject('typeBinding', 'FilterType', FilterType)


# Complex type TaxonomyDescriptionType with content type SIMPLE
class TaxonomyDescriptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TaxonomyDescriptionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxonomyDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 793, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute Cclass uses Python identifier Cclass
    __Cclass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cclass'), 'Cclass', '__AbsentNamespace0_TaxonomyDescriptionType_Cclass', CclassType, required=True)
    __Cclass._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 796, 8)
    __Cclass._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 796, 8)
    
    Cclass = property(__Cclass.value, __Cclass.set, None, None)

    
    # Attribute Cgroup uses Python identifier Cgroup
    __Cgroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cgroup'), 'Cgroup', '__AbsentNamespace0_TaxonomyDescriptionType_Cgroup', CgroupType)
    __Cgroup._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 797, 8)
    __Cgroup._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 797, 8)
    
    Cgroup = property(__Cgroup.value, __Cgroup.set, None, None)

    
    # Attribute doc uses Python identifier doc
    __doc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'doc'), 'doc', '__AbsentNamespace0_TaxonomyDescriptionType_doc', pyxb.binding.datatypes.string)
    __doc._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 798, 8)
    __doc._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 798, 8)
    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Attribute generator uses Python identifier generator
    __generator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'generator'), 'generator', '__AbsentNamespace0_TaxonomyDescriptionType_generator', pyxb.binding.datatypes.string)
    __generator._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 799, 8)
    __generator._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 799, 8)
    
    generator = property(__generator.value, __generator.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Cclass.name() : __Cclass,
        __Cgroup.name() : __Cgroup,
        __doc.name() : __doc,
        __generator.name() : __generator
    })
Namespace.addCategoryObject('typeBinding', 'TaxonomyDescriptionType', TaxonomyDescriptionType)


# Complex type ApiType with content type ELEMENT_ONLY
class ApiType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ApiType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ApiType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 811, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_ApiType_description', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 813, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element files uses Python identifier files
    __files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'files'), 'files', '__AbsentNamespace0_ApiType_files', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 815, 6), )

    
    files = property(__files.value, __files.set, None, None)

    
    # Attribute Cclass uses Python identifier Cclass
    __Cclass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cclass'), 'Cclass', '__AbsentNamespace0_ApiType_Cclass', CclassType, required=True)
    __Cclass._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 823, 4)
    __Cclass._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 823, 4)
    
    Cclass = property(__Cclass.value, __Cclass.set, None, None)

    
    # Attribute Cgroup uses Python identifier Cgroup
    __Cgroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cgroup'), 'Cgroup', '__AbsentNamespace0_ApiType_Cgroup', CgroupType, required=True)
    __Cgroup._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 824, 4)
    __Cgroup._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 824, 4)
    
    Cgroup = property(__Cgroup.value, __Cgroup.set, None, None)

    
    # Attribute exclusive uses Python identifier exclusive
    __exclusive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'exclusive'), 'exclusive', '__AbsentNamespace0_ApiType_exclusive', pyxb.binding.datatypes.boolean, unicode_default='1')
    __exclusive._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 825, 4)
    __exclusive._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 825, 4)
    
    exclusive = property(__exclusive.value, __exclusive.set, None, None)

    
    # Attribute Capiversion uses Python identifier Capiversion
    __Capiversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Capiversion'), 'Capiversion', '__AbsentNamespace0_ApiType_Capiversion', VersionType)
    __Capiversion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 826, 4)
    __Capiversion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 826, 4)
    
    Capiversion = property(__Capiversion.value, __Capiversion.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __files.name() : __files
    })
    _AttributeMap.update({
        __Cclass.name() : __Cclass,
        __Cgroup.name() : __Cgroup,
        __exclusive.name() : __exclusive,
        __Capiversion.name() : __Capiversion
    })
Namespace.addCategoryObject('typeBinding', 'ApiType', ApiType)


# Complex type ComponentCategoryType with content type EMPTY
class ComponentCategoryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ComponentCategoryType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComponentCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 853, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Cvendor uses Python identifier Cvendor
    __Cvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cvendor'), 'Cvendor', '__AbsentNamespace0_ComponentCategoryType_Cvendor', pyxb.binding.datatypes.string)
    __Cvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 854, 4)
    __Cvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 854, 4)
    
    Cvendor = property(__Cvendor.value, __Cvendor.set, None, None)

    
    # Attribute Cbundle uses Python identifier Cbundle
    __Cbundle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cbundle'), 'Cbundle', '__AbsentNamespace0_ComponentCategoryType_Cbundle', pyxb.binding.datatypes.string)
    __Cbundle._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 855, 4)
    __Cbundle._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 855, 4)
    
    Cbundle = property(__Cbundle.value, __Cbundle.set, None, None)

    
    # Attribute Cclass uses Python identifier Cclass
    __Cclass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cclass'), 'Cclass', '__AbsentNamespace0_ComponentCategoryType_Cclass', CclassType, required=True)
    __Cclass._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 856, 4)
    __Cclass._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 856, 4)
    
    Cclass = property(__Cclass.value, __Cclass.set, None, None)

    
    # Attribute Cgroup uses Python identifier Cgroup
    __Cgroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cgroup'), 'Cgroup', '__AbsentNamespace0_ComponentCategoryType_Cgroup', CgroupType)
    __Cgroup._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 857, 4)
    __Cgroup._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 857, 4)
    
    Cgroup = property(__Cgroup.value, __Cgroup.set, None, None)

    
    # Attribute Csub uses Python identifier Csub
    __Csub = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Csub'), 'Csub', '__AbsentNamespace0_ComponentCategoryType_Csub', CsubType)
    __Csub._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 858, 4)
    __Csub._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 858, 4)
    
    Csub = property(__Csub.value, __Csub.set, None, None)

    
    # Attribute Cvariant uses Python identifier Cvariant
    __Cvariant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cvariant'), 'Cvariant', '__AbsentNamespace0_ComponentCategoryType_Cvariant', CvariantType)
    __Cvariant._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 859, 4)
    __Cvariant._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 859, 4)
    
    Cvariant = property(__Cvariant.value, __Cvariant.set, None, None)

    
    # Attribute Cversion uses Python identifier Cversion
    __Cversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cversion'), 'Cversion', '__AbsentNamespace0_ComponentCategoryType_Cversion', VersionType)
    __Cversion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 860, 4)
    __Cversion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 860, 4)
    
    Cversion = property(__Cversion.value, __Cversion.set, None, None)

    
    # Attribute Capiversion uses Python identifier Capiversion
    __Capiversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Capiversion'), 'Capiversion', '__AbsentNamespace0_ComponentCategoryType_Capiversion', VersionType)
    __Capiversion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 861, 4)
    __Capiversion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 861, 4)
    
    Capiversion = property(__Capiversion.value, __Capiversion.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Cvendor.name() : __Cvendor,
        __Cbundle.name() : __Cbundle,
        __Cclass.name() : __Cclass,
        __Cgroup.name() : __Cgroup,
        __Csub.name() : __Csub,
        __Cvariant.name() : __Cvariant,
        __Cversion.name() : __Cversion,
        __Capiversion.name() : __Capiversion
    })
Namespace.addCategoryObject('typeBinding', 'ComponentCategoryType', ComponentCategoryType)


# Complex type BoardReferenceType with content type EMPTY
class BoardReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BoardReferenceType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoardReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 875, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_BoardReferenceType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 876, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 876, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute vendor uses Python identifier vendor
    __vendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vendor'), 'vendor', '__AbsentNamespace0_BoardReferenceType_vendor', pyxb.binding.datatypes.string, required=True)
    __vendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 877, 4)
    __vendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 877, 4)
    
    vendor = property(__vendor.value, __vendor.set, None, None)

    
    # Attribute Dvendor uses Python identifier Dvendor
    __Dvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dvendor'), 'Dvendor', '__AbsentNamespace0_BoardReferenceType_Dvendor', DeviceVendorEnum)
    __Dvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 878, 4)
    __Dvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 878, 4)
    
    Dvendor = property(__Dvendor.value, __Dvendor.set, None, None)

    
    # Attribute Dfamily uses Python identifier Dfamily
    __Dfamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dfamily'), 'Dfamily', '__AbsentNamespace0_BoardReferenceType_Dfamily', pyxb.binding.datatypes.string)
    __Dfamily._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 879, 4)
    __Dfamily._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 879, 4)
    
    Dfamily = property(__Dfamily.value, __Dfamily.set, None, None)

    
    # Attribute DsubFamily uses Python identifier DsubFamily
    __DsubFamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DsubFamily'), 'DsubFamily', '__AbsentNamespace0_BoardReferenceType_DsubFamily', pyxb.binding.datatypes.string)
    __DsubFamily._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 880, 4)
    __DsubFamily._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 880, 4)
    
    DsubFamily = property(__DsubFamily.value, __DsubFamily.set, None, None)

    
    # Attribute Dname uses Python identifier Dname
    __Dname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dname'), 'Dname', '__AbsentNamespace0_BoardReferenceType_Dname', pyxb.binding.datatypes.string)
    __Dname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 881, 4)
    __Dname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 881, 4)
    
    Dname = property(__Dname.value, __Dname.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __vendor.name() : __vendor,
        __Dvendor.name() : __Dvendor,
        __Dfamily.name() : __Dfamily,
        __DsubFamily.name() : __DsubFamily,
        __Dname.name() : __Dname
    })
Namespace.addCategoryObject('typeBinding', 'BoardReferenceType', BoardReferenceType)


# Complex type CompatibleDeviceType with content type EMPTY
class CompatibleDeviceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CompatibleDeviceType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompatibleDeviceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 884, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute deviceIndex uses Python identifier deviceIndex
    __deviceIndex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deviceIndex'), 'deviceIndex', '__AbsentNamespace0_CompatibleDeviceType_deviceIndex', pyxb.binding.datatypes.string)
    __deviceIndex._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 885, 4)
    __deviceIndex._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 885, 4)
    
    deviceIndex = property(__deviceIndex.value, __deviceIndex.set, None, None)

    
    # Attribute Dvendor uses Python identifier Dvendor
    __Dvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dvendor'), 'Dvendor', '__AbsentNamespace0_CompatibleDeviceType_Dvendor', DeviceVendorEnum)
    __Dvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 886, 4)
    __Dvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 886, 4)
    
    Dvendor = property(__Dvendor.value, __Dvendor.set, None, None)

    
    # Attribute Dfamily uses Python identifier Dfamily
    __Dfamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dfamily'), 'Dfamily', '__AbsentNamespace0_CompatibleDeviceType_Dfamily', pyxb.binding.datatypes.string)
    __Dfamily._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 887, 4)
    __Dfamily._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 887, 4)
    
    Dfamily = property(__Dfamily.value, __Dfamily.set, None, None)

    
    # Attribute DsubFamily uses Python identifier DsubFamily
    __DsubFamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DsubFamily'), 'DsubFamily', '__AbsentNamespace0_CompatibleDeviceType_DsubFamily', pyxb.binding.datatypes.string)
    __DsubFamily._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 888, 4)
    __DsubFamily._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 888, 4)
    
    DsubFamily = property(__DsubFamily.value, __DsubFamily.set, None, None)

    
    # Attribute Dname uses Python identifier Dname
    __Dname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dname'), 'Dname', '__AbsentNamespace0_CompatibleDeviceType_Dname', pyxb.binding.datatypes.string)
    __Dname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 889, 4)
    __Dname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 889, 4)
    
    Dname = property(__Dname.value, __Dname.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __deviceIndex.name() : __deviceIndex,
        __Dvendor.name() : __Dvendor,
        __Dfamily.name() : __Dfamily,
        __DsubFamily.name() : __DsubFamily,
        __Dname.name() : __Dname
    })
Namespace.addCategoryObject('typeBinding', 'CompatibleDeviceType', CompatibleDeviceType)


# Complex type BoardsDeviceType with content type EMPTY
class BoardsDeviceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BoardsDeviceType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoardsDeviceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 892, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute deviceIndex uses Python identifier deviceIndex
    __deviceIndex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deviceIndex'), 'deviceIndex', '__AbsentNamespace0_BoardsDeviceType_deviceIndex', pyxb.binding.datatypes.string)
    __deviceIndex._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 893, 4)
    __deviceIndex._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 893, 4)
    
    deviceIndex = property(__deviceIndex.value, __deviceIndex.set, None, None)

    
    # Attribute Dvendor uses Python identifier Dvendor
    __Dvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dvendor'), 'Dvendor', '__AbsentNamespace0_BoardsDeviceType_Dvendor', DeviceVendorEnum, required=True)
    __Dvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 894, 4)
    __Dvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 894, 4)
    
    Dvendor = property(__Dvendor.value, __Dvendor.set, None, None)

    
    # Attribute Dfamily uses Python identifier Dfamily
    __Dfamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dfamily'), 'Dfamily', '__AbsentNamespace0_BoardsDeviceType_Dfamily', pyxb.binding.datatypes.string)
    __Dfamily._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 895, 4)
    __Dfamily._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 895, 4)
    
    Dfamily = property(__Dfamily.value, __Dfamily.set, None, None)

    
    # Attribute DsubFamily uses Python identifier DsubFamily
    __DsubFamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DsubFamily'), 'DsubFamily', '__AbsentNamespace0_BoardsDeviceType_DsubFamily', pyxb.binding.datatypes.string)
    __DsubFamily._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 896, 4)
    __DsubFamily._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 896, 4)
    
    DsubFamily = property(__DsubFamily.value, __DsubFamily.set, None, None)

    
    # Attribute Dname uses Python identifier Dname
    __Dname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dname'), 'Dname', '__AbsentNamespace0_BoardsDeviceType_Dname', pyxb.binding.datatypes.string)
    __Dname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 897, 4)
    __Dname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 897, 4)
    
    Dname = property(__Dname.value, __Dname.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __deviceIndex.name() : __deviceIndex,
        __Dvendor.name() : __Dvendor,
        __Dfamily.name() : __Dfamily,
        __DsubFamily.name() : __DsubFamily,
        __Dname.name() : __Dname
    })
Namespace.addCategoryObject('typeBinding', 'BoardsDeviceType', BoardsDeviceType)


# Complex type BoardsBookType with content type EMPTY
class BoardsBookType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BoardsBookType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoardsBookType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 910, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__AbsentNamespace0_BoardsBookType_category', BoardBookCategoryEnum)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 911, 4)
    __category._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 911, 4)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_BoardsBookType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 912, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 912, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__AbsentNamespace0_BoardsBookType_title', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 913, 4)
    __title._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 913, 4)
    
    title = property(__title.value, __title.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __category.name() : __category,
        __name.name() : __name,
        __title.name() : __title
    })
Namespace.addCategoryObject('typeBinding', 'BoardsBookType', BoardsBookType)


# Complex type FileType with content type EMPTY
class FileType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type FileType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FileType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1006, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute condition uses Python identifier condition
    __condition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'condition'), 'condition', '__AbsentNamespace0_FileType_condition', pyxb.binding.datatypes.string)
    __condition._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1007, 4)
    __condition._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1007, 4)
    
    condition = property(__condition.value, __condition.set, None, None)

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__AbsentNamespace0_FileType_category', FileCategoryType, required=True)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1009, 4)
    __category._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1009, 4)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute attr uses Python identifier attr
    __attr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'attr'), 'attr', '__AbsentNamespace0_FileType_attr', FileAttributeType)
    __attr._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1011, 4)
    __attr._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1011, 4)
    
    attr = property(__attr.value, __attr.set, None, None)

    
    # Attribute select uses Python identifier select
    __select = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'select'), 'select', '__AbsentNamespace0_FileType_select', pyxb.binding.datatypes.string)
    __select._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1013, 4)
    __select._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1013, 4)
    
    select = property(__select.value, __select.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_FileType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1015, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1015, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute copy uses Python identifier copy
    __copy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'copy'), 'copy', '__AbsentNamespace0_FileType_copy', pyxb.binding.datatypes.string)
    __copy._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1017, 4)
    __copy._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1017, 4)
    
    copy = property(__copy.value, __copy.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_FileType_version', VersionType)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1019, 4)
    __version._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1019, 4)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute src uses Python identifier src
    __src = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'src'), 'src', '__AbsentNamespace0_FileType_src', pyxb.binding.datatypes.string)
    __src._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1021, 4)
    __src._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1021, 4)
    
    src = property(__src.value, __src.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __condition.name() : __condition,
        __category.name() : __category,
        __attr.name() : __attr,
        __select.name() : __select,
        __name.name() : __name,
        __copy.name() : __copy,
        __version.name() : __version,
        __src.name() : __src
    })
Namespace.addCategoryObject('typeBinding', 'FileType', FileType)


# Complex type ReleaseType with content type SIMPLE
class ReleaseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ReleaseType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1049, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_ReleaseType_version', VersionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1052, 8)
    __version._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1052, 8)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__AbsentNamespace0_ReleaseType_date', pyxb.binding.datatypes.date)
    __date._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1053, 8)
    __date._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1053, 8)
    
    date = property(__date.value, __date.set, None, None)

    
    # Attribute deprecated uses Python identifier deprecated
    __deprecated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deprecated'), 'deprecated', '__AbsentNamespace0_ReleaseType_deprecated', pyxb.binding.datatypes.date)
    __deprecated._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1054, 8)
    __deprecated._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1054, 8)
    
    deprecated = property(__deprecated.value, __deprecated.set, None, None)

    
    # Attribute replacement uses Python identifier replacement
    __replacement = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'replacement'), 'replacement', '__AbsentNamespace0_ReleaseType_replacement', pyxb.binding.datatypes.string)
    __replacement._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1055, 8)
    __replacement._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1055, 8)
    
    replacement = property(__replacement.value, __replacement.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __version.name() : __version,
        __date.name() : __date,
        __deprecated.name() : __deprecated,
        __replacement.name() : __replacement
    })
Namespace.addCategoryObject('typeBinding', 'ReleaseType', ReleaseType)


# Complex type GeneratorFileType with content type EMPTY
class GeneratorFileType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GeneratorFileType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneratorFileType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1067, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute condition uses Python identifier condition
    __condition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'condition'), 'condition', '__AbsentNamespace0_GeneratorFileType_condition', pyxb.binding.datatypes.string)
    __condition._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1070, 4)
    __condition._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1070, 4)
    
    condition = property(__condition.value, __condition.set, None, None)

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__AbsentNamespace0_GeneratorFileType_category', pyxb.binding.datatypes.string, required=True)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1072, 4)
    __category._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1072, 4)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_GeneratorFileType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1074, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1074, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_GeneratorFileType_version', VersionType)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1076, 4)
    __version._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1076, 4)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __condition.name() : __condition,
        __category.name() : __category,
        __name.name() : __name,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', 'GeneratorFileType', GeneratorFileType)


# Complex type GeneratorDeviceSelectType with content type EMPTY
class GeneratorDeviceSelectType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GeneratorDeviceSelectType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneratorDeviceSelectType')
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1079, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Dvendor uses Python identifier Dvendor
    __Dvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dvendor'), 'Dvendor', '__AbsentNamespace0_GeneratorDeviceSelectType_Dvendor', DeviceVendorEnum, required=True)
    __Dvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1080, 4)
    __Dvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1080, 4)
    
    Dvendor = property(__Dvendor.value, __Dvendor.set, None, None)

    
    # Attribute Dname uses Python identifier Dname
    __Dname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dname'), 'Dname', '__AbsentNamespace0_GeneratorDeviceSelectType_Dname', pyxb.binding.datatypes.string)
    __Dname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1081, 4)
    __Dname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1081, 4)
    
    Dname = property(__Dname.value, __Dname.set, None, None)

    
    # Attribute Dvariant uses Python identifier Dvariant
    __Dvariant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dvariant'), 'Dvariant', '__AbsentNamespace0_GeneratorDeviceSelectType_Dvariant', pyxb.binding.datatypes.string)
    __Dvariant._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1082, 4)
    __Dvariant._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1082, 4)
    
    Dvariant = property(__Dvariant.value, __Dvariant.set, None, None)

    
    # Attribute Pname uses Python identifier Pname
    __Pname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Pname'), 'Pname', '__AbsentNamespace0_GeneratorDeviceSelectType_Pname', RestrictedString)
    __Pname._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1083, 4)
    __Pname._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1083, 4)
    
    Pname = property(__Pname.value, __Pname.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Dvendor.name() : __Dvendor,
        __Dname.name() : __Dname,
        __Dvariant.name() : __Dvariant,
        __Pname.name() : __Pname
    })
Namespace.addCategoryObject('typeBinding', 'GeneratorDeviceSelectType', GeneratorDeviceSelectType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1155, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_12_name', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1158, 8), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element vendor uses Python identifier vendor
    __vendor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vendor'), 'vendor', '__AbsentNamespace0_CTD_ANON_12_vendor', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1160, 8), )

    
    vendor = property(__vendor.value, __vendor.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_12_description', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1162, 8), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__AbsentNamespace0_CTD_ANON_12_url', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1164, 8), )

    
    url = property(__url.value, __url.set, None, None)

    
    # Element supportContact uses Python identifier supportContact
    __supportContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'supportContact'), 'supportContact', '__AbsentNamespace0_CTD_ANON_12_supportContact', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1166, 8), )

    
    supportContact = property(__supportContact.value, __supportContact.set, None, None)

    
    # Element license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'license'), 'license', '__AbsentNamespace0_CTD_ANON_12_license', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1168, 8), )

    
    license = property(__license.value, __license.set, None, None)

    
    # Element releases uses Python identifier releases
    __releases = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'releases'), 'releases', '__AbsentNamespace0_CTD_ANON_12_releases', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1169, 8), )

    
    releases = property(__releases.value, __releases.set, None, None)

    
    # Element keywords uses Python identifier keywords
    __keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keywords'), 'keywords', '__AbsentNamespace0_CTD_ANON_12_keywords', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1171, 8), )

    
    keywords = property(__keywords.value, __keywords.set, None, None)

    
    # Element generators uses Python identifier generators
    __generators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'generators'), 'generators', '__AbsentNamespace0_CTD_ANON_12_generators', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1173, 8), )

    
    generators = property(__generators.value, __generators.set, None, None)

    
    # Element devices uses Python identifier devices
    __devices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'devices'), 'devices', '__AbsentNamespace0_CTD_ANON_12_devices', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1175, 8), )

    
    devices = property(__devices.value, __devices.set, None, None)

    
    # Element boards uses Python identifier boards
    __boards = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boards'), 'boards', '__AbsentNamespace0_CTD_ANON_12_boards', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1209, 8), )

    
    boards = property(__boards.value, __boards.set, None, None)

    
    # Element taxonomy uses Python identifier taxonomy
    __taxonomy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'taxonomy'), 'taxonomy', '__AbsentNamespace0_CTD_ANON_12_taxonomy', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1212, 8), )

    
    taxonomy = property(__taxonomy.value, __taxonomy.set, None, None)

    
    # Element apis uses Python identifier apis
    __apis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'apis'), 'apis', '__AbsentNamespace0_CTD_ANON_12_apis', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1214, 8), )

    
    apis = property(__apis.value, __apis.set, None, None)

    
    # Element conditions uses Python identifier conditions
    __conditions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'conditions'), 'conditions', '__AbsentNamespace0_CTD_ANON_12_conditions', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1216, 8), )

    
    conditions = property(__conditions.value, __conditions.set, None, None)

    
    # Element examples uses Python identifier examples
    __examples = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'examples'), 'examples', '__AbsentNamespace0_CTD_ANON_12_examples', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1218, 8), )

    
    examples = property(__examples.value, __examples.set, None, None)

    
    # Element components uses Python identifier components
    __components = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'components'), 'components', '__AbsentNamespace0_CTD_ANON_12_components', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1220, 8), )

    
    components = property(__components.value, __components.set, None, None)

    
    # Attribute schemaVersion uses Python identifier schemaVersion
    __schemaVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemaVersion'), 'schemaVersion', '__AbsentNamespace0_CTD_ANON_12_schemaVersion', VersionType, required=True)
    __schemaVersion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1311, 6)
    __schemaVersion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1311, 6)
    
    schemaVersion = property(__schemaVersion.value, __schemaVersion.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __vendor.name() : __vendor,
        __description.name() : __description,
        __url.name() : __url,
        __supportContact.name() : __supportContact,
        __license.name() : __license,
        __releases.name() : __releases,
        __keywords.name() : __keywords,
        __generators.name() : __generators,
        __devices.name() : __devices,
        __boards.name() : __boards,
        __taxonomy.name() : __taxonomy,
        __apis.name() : __apis,
        __conditions.name() : __conditions,
        __examples.name() : __examples,
        __components.name() : __components
    })
    _AttributeMap.update({
        __schemaVersion.name() : __schemaVersion
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1181, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element compile uses Python identifier compile
    __compile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'compile'), 'compile', '__AbsentNamespace0_CTD_ANON_13_compile', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6), )

    
    compile = property(__compile.value, __compile.set, None, None)

    
    # Element memory uses Python identifier memory
    __memory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'memory'), 'memory', '__AbsentNamespace0_CTD_ANON_13_memory', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6), )

    
    memory = property(__memory.value, __memory.set, None, None)

    
    # Element algorithm uses Python identifier algorithm
    __algorithm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'algorithm'), 'algorithm', '__AbsentNamespace0_CTD_ANON_13_algorithm', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6), )

    
    algorithm = property(__algorithm.value, __algorithm.set, None, None)

    
    # Element book uses Python identifier book
    __book = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'book'), 'book', '__AbsentNamespace0_CTD_ANON_13_book', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6), )

    
    book = property(__book.value, __book.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_13_description', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element feature uses Python identifier feature
    __feature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'feature'), 'feature', '__AbsentNamespace0_CTD_ANON_13_feature', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6), )

    
    feature = property(__feature.value, __feature.set, None, None)

    
    # Element environment uses Python identifier environment
    __environment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'environment'), 'environment', '__AbsentNamespace0_CTD_ANON_13_environment', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6), )

    
    environment = property(__environment.value, __environment.set, None, None)

    
    # Element debugport uses Python identifier debugport
    __debugport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugport'), 'debugport', '__AbsentNamespace0_CTD_ANON_13_debugport', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6), )

    
    debugport = property(__debugport.value, __debugport.set, None, None)

    
    # Element debug uses Python identifier debug
    __debug = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debug'), 'debug', '__AbsentNamespace0_CTD_ANON_13_debug', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6), )

    
    debug = property(__debug.value, __debug.set, None, None)

    
    # Element trace uses Python identifier trace
    __trace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trace'), 'trace', '__AbsentNamespace0_CTD_ANON_13_trace', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6), )

    
    trace = property(__trace.value, __trace.set, None, None)

    
    # Element debugvars uses Python identifier debugvars
    __debugvars = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugvars'), 'debugvars', '__AbsentNamespace0_CTD_ANON_13_debugvars', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6), )

    
    debugvars = property(__debugvars.value, __debugvars.set, None, None)

    
    # Element sequences uses Python identifier sequences
    __sequences = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sequences'), 'sequences', '__AbsentNamespace0_CTD_ANON_13_sequences', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6), )

    
    sequences = property(__sequences.value, __sequences.set, None, None)

    
    # Element processor uses Python identifier processor
    __processor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'processor'), 'processor', '__AbsentNamespace0_CTD_ANON_13_processor', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6), )

    
    processor = property(__processor.value, __processor.set, None, None)

    
    # Element debugconfig uses Python identifier debugconfig
    __debugconfig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'debugconfig'), 'debugconfig', '__AbsentNamespace0_CTD_ANON_13_debugconfig', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6), )

    
    debugconfig = property(__debugconfig.value, __debugconfig.set, None, None)

    
    # Element device uses Python identifier device
    __device = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device'), 'device', '__AbsentNamespace0_CTD_ANON_13_device', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1184, 20), )

    
    device = property(__device.value, __device.set, None, None)

    
    # Element subFamily uses Python identifier subFamily
    __subFamily = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'subFamily'), 'subFamily', '__AbsentNamespace0_CTD_ANON_13_subFamily', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1186, 20), )

    
    subFamily = property(__subFamily.value, __subFamily.set, None, None)

    
    # Attribute Dfamily uses Python identifier Dfamily
    __Dfamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dfamily'), 'Dfamily', '__AbsentNamespace0_CTD_ANON_13_Dfamily', pyxb.binding.datatypes.string, required=True)
    __Dfamily._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1199, 18)
    __Dfamily._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1199, 18)
    
    Dfamily = property(__Dfamily.value, __Dfamily.set, None, None)

    
    # Attribute Dvendor uses Python identifier Dvendor
    __Dvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dvendor'), 'Dvendor', '__AbsentNamespace0_CTD_ANON_13_Dvendor', DeviceVendorEnum, required=True)
    __Dvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1200, 18)
    __Dvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1200, 18)
    
    Dvendor = property(__Dvendor.value, __Dvendor.set, None, None)

    _ElementMap.update({
        __compile.name() : __compile,
        __memory.name() : __memory,
        __algorithm.name() : __algorithm,
        __book.name() : __book,
        __description.name() : __description,
        __feature.name() : __feature,
        __environment.name() : __environment,
        __debugport.name() : __debugport,
        __debug.name() : __debug,
        __trace.name() : __trace,
        __debugvars.name() : __debugvars,
        __sequences.name() : __sequences,
        __processor.name() : __processor,
        __debugconfig.name() : __debugconfig,
        __device.name() : __device,
        __subFamily.name() : __subFamily
    })
    _AttributeMap.update({
        __Dfamily.name() : __Dfamily,
        __Dvendor.name() : __Dvendor
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1225, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_14_description', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1227, 20), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'doc'), 'doc', '__AbsentNamespace0_CTD_ANON_14_doc', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1228, 20), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element component uses Python identifier component
    __component = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'component'), 'component', '__AbsentNamespace0_CTD_ANON_14_component', True, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1229, 20), )

    
    component = property(__component.value, __component.set, None, None)

    
    # Attribute Cbundle uses Python identifier Cbundle
    __Cbundle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cbundle'), 'Cbundle', '__AbsentNamespace0_CTD_ANON_14_Cbundle', pyxb.binding.datatypes.string, required=True)
    __Cbundle._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1263, 18)
    __Cbundle._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1263, 18)
    
    Cbundle = property(__Cbundle.value, __Cbundle.set, None, None)

    
    # Attribute Cvendor uses Python identifier Cvendor
    __Cvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cvendor'), 'Cvendor', '__AbsentNamespace0_CTD_ANON_14_Cvendor', pyxb.binding.datatypes.string)
    __Cvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1264, 18)
    __Cvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1264, 18)
    
    Cvendor = property(__Cvendor.value, __Cvendor.set, None, None)

    
    # Attribute Cclass uses Python identifier Cclass
    __Cclass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cclass'), 'Cclass', '__AbsentNamespace0_CTD_ANON_14_Cclass', CclassType, required=True)
    __Cclass._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1265, 18)
    __Cclass._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1265, 18)
    
    Cclass = property(__Cclass.value, __Cclass.set, None, None)

    
    # Attribute Cversion uses Python identifier Cversion
    __Cversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cversion'), 'Cversion', '__AbsentNamespace0_CTD_ANON_14_Cversion', VersionType, required=True)
    __Cversion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1266, 18)
    __Cversion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1266, 18)
    
    Cversion = property(__Cversion.value, __Cversion.set, None, None)

    
    # Attribute generator uses Python identifier generator
    __generator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'generator'), 'generator', '__AbsentNamespace0_CTD_ANON_14_generator', pyxb.binding.datatypes.string)
    __generator._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1268, 18)
    __generator._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1268, 18)
    
    generator = property(__generator.value, __generator.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __doc.name() : __doc,
        __component.name() : __component
    })
    _AttributeMap.update({
        __Cbundle.name() : __Cbundle,
        __Cvendor.name() : __Cvendor,
        __Cclass.name() : __Cclass,
        __Cversion.name() : __Cversion,
        __generator.name() : __generator
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1230, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element deprecated uses Python identifier deprecated
    __deprecated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deprecated'), 'deprecated', '__AbsentNamespace0_CTD_ANON_15_deprecated', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1233, 26), )

    
    deprecated = property(__deprecated.value, __deprecated.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_15_description', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1235, 26), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element RTE_Components_h uses Python identifier RTE_Components_h
    __RTE_Components_h = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RTE_Components_h'), 'RTE_Components_h', '__AbsentNamespace0_CTD_ANON_15_RTE_Components_h', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1237, 26), )

    
    RTE_Components_h = property(__RTE_Components_h.value, __RTE_Components_h.set, None, None)

    
    # Element files uses Python identifier files
    __files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'files'), 'files', '__AbsentNamespace0_CTD_ANON_15_files', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1239, 26), )

    
    files = property(__files.value, __files.set, None, None)

    
    # Attribute Cgroup uses Python identifier Cgroup
    __Cgroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cgroup'), 'Cgroup', '__AbsentNamespace0_CTD_ANON_15_Cgroup', CgroupType, required=True)
    __Cgroup._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1248, 24)
    __Cgroup._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1248, 24)
    
    Cgroup = property(__Cgroup.value, __Cgroup.set, None, None)

    
    # Attribute Csub uses Python identifier Csub
    __Csub = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Csub'), 'Csub', '__AbsentNamespace0_CTD_ANON_15_Csub', CsubType)
    __Csub._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1249, 24)
    __Csub._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1249, 24)
    
    Csub = property(__Csub.value, __Csub.set, None, None)

    
    # Attribute Cvariant uses Python identifier Cvariant
    __Cvariant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cvariant'), 'Cvariant', '__AbsentNamespace0_CTD_ANON_15_Cvariant', CvariantType)
    __Cvariant._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1250, 24)
    __Cvariant._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1250, 24)
    
    Cvariant = property(__Cvariant.value, __Cvariant.set, None, None)

    
    # Attribute Capiversion uses Python identifier Capiversion
    __Capiversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Capiversion'), 'Capiversion', '__AbsentNamespace0_CTD_ANON_15_Capiversion', VersionType)
    __Capiversion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1252, 24)
    __Capiversion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1252, 24)
    
    Capiversion = property(__Capiversion.value, __Capiversion.set, None, None)

    
    # Attribute condition uses Python identifier condition
    __condition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'condition'), 'condition', '__AbsentNamespace0_CTD_ANON_15_condition', pyxb.binding.datatypes.string)
    __condition._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1254, 24)
    __condition._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1254, 24)
    
    condition = property(__condition.value, __condition.set, None, None)

    
    # Attribute maxInstances uses Python identifier maxInstances
    __maxInstances = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxInstances'), 'maxInstances', '__AbsentNamespace0_CTD_ANON_15_maxInstances', MaxInstancesType)
    __maxInstances._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1256, 24)
    __maxInstances._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1256, 24)
    
    maxInstances = property(__maxInstances.value, __maxInstances.set, None, None)

    
    # Attribute generator uses Python identifier generator
    __generator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'generator'), 'generator', '__AbsentNamespace0_CTD_ANON_15_generator', pyxb.binding.datatypes.string)
    __generator._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1258, 24)
    __generator._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1258, 24)
    
    generator = property(__generator.value, __generator.set, None, None)

    _ElementMap.update({
        __deprecated.name() : __deprecated,
        __description.name() : __description,
        __RTE_Components_h.name() : __RTE_Components_h,
        __files.name() : __files
    })
    _AttributeMap.update({
        __Cgroup.name() : __Cgroup,
        __Csub.name() : __Csub,
        __Cvariant.name() : __Cvariant,
        __Capiversion.name() : __Capiversion,
        __condition.name() : __condition,
        __maxInstances.name() : __maxInstances,
        __generator.name() : __generator
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1272, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element deprecated uses Python identifier deprecated
    __deprecated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deprecated'), 'deprecated', '__AbsentNamespace0_CTD_ANON_16_deprecated', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1275, 20), )

    
    deprecated = property(__deprecated.value, __deprecated.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_16_description', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1277, 20), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element RTE_Components_h uses Python identifier RTE_Components_h
    __RTE_Components_h = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RTE_Components_h'), 'RTE_Components_h', '__AbsentNamespace0_CTD_ANON_16_RTE_Components_h', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1279, 20), )

    
    RTE_Components_h = property(__RTE_Components_h.value, __RTE_Components_h.set, None, None)

    
    # Element files uses Python identifier files
    __files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'files'), 'files', '__AbsentNamespace0_CTD_ANON_16_files', False, pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1281, 20), )

    
    files = property(__files.value, __files.set, None, None)

    
    # Attribute Cvendor uses Python identifier Cvendor
    __Cvendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cvendor'), 'Cvendor', '__AbsentNamespace0_CTD_ANON_16_Cvendor', pyxb.binding.datatypes.string)
    __Cvendor._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1290, 18)
    __Cvendor._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1290, 18)
    
    Cvendor = property(__Cvendor.value, __Cvendor.set, None, None)

    
    # Attribute Cclass uses Python identifier Cclass
    __Cclass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cclass'), 'Cclass', '__AbsentNamespace0_CTD_ANON_16_Cclass', CclassType, required=True)
    __Cclass._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1291, 18)
    __Cclass._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1291, 18)
    
    Cclass = property(__Cclass.value, __Cclass.set, None, None)

    
    # Attribute Cgroup uses Python identifier Cgroup
    __Cgroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cgroup'), 'Cgroup', '__AbsentNamespace0_CTD_ANON_16_Cgroup', CgroupType, required=True)
    __Cgroup._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1292, 18)
    __Cgroup._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1292, 18)
    
    Cgroup = property(__Cgroup.value, __Cgroup.set, None, None)

    
    # Attribute Csub uses Python identifier Csub
    __Csub = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Csub'), 'Csub', '__AbsentNamespace0_CTD_ANON_16_Csub', CsubType)
    __Csub._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1293, 18)
    __Csub._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1293, 18)
    
    Csub = property(__Csub.value, __Csub.set, None, None)

    
    # Attribute Cvariant uses Python identifier Cvariant
    __Cvariant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cvariant'), 'Cvariant', '__AbsentNamespace0_CTD_ANON_16_Cvariant', CvariantType)
    __Cvariant._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1294, 18)
    __Cvariant._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1294, 18)
    
    Cvariant = property(__Cvariant.value, __Cvariant.set, None, None)

    
    # Attribute Cversion uses Python identifier Cversion
    __Cversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Cversion'), 'Cversion', '__AbsentNamespace0_CTD_ANON_16_Cversion', VersionType, required=True)
    __Cversion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1295, 18)
    __Cversion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1295, 18)
    
    Cversion = property(__Cversion.value, __Cversion.set, None, None)

    
    # Attribute Capiversion uses Python identifier Capiversion
    __Capiversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Capiversion'), 'Capiversion', '__AbsentNamespace0_CTD_ANON_16_Capiversion', VersionType)
    __Capiversion._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1297, 18)
    __Capiversion._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1297, 18)
    
    Capiversion = property(__Capiversion.value, __Capiversion.set, None, None)

    
    # Attribute condition uses Python identifier condition
    __condition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'condition'), 'condition', '__AbsentNamespace0_CTD_ANON_16_condition', pyxb.binding.datatypes.string)
    __condition._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1299, 18)
    __condition._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1299, 18)
    
    condition = property(__condition.value, __condition.set, None, None)

    
    # Attribute maxInstances uses Python identifier maxInstances
    __maxInstances = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxInstances'), 'maxInstances', '__AbsentNamespace0_CTD_ANON_16_maxInstances', MaxInstancesType)
    __maxInstances._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1301, 18)
    __maxInstances._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1301, 18)
    
    maxInstances = property(__maxInstances.value, __maxInstances.set, None, None)

    
    # Attribute generator uses Python identifier generator
    __generator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'generator'), 'generator', '__AbsentNamespace0_CTD_ANON_16_generator', pyxb.binding.datatypes.string)
    __generator._DeclarationLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1303, 18)
    __generator._UseLocation = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1303, 18)
    
    generator = property(__generator.value, __generator.set, None, None)

    _ElementMap.update({
        __deprecated.name() : __deprecated,
        __description.name() : __description,
        __RTE_Components_h.name() : __RTE_Components_h,
        __files.name() : __files
    })
    _AttributeMap.update({
        __Cvendor.name() : __Cvendor,
        __Cclass.name() : __Cclass,
        __Cgroup.name() : __Cgroup,
        __Csub.name() : __Csub,
        __Cvariant.name() : __Cvariant,
        __Cversion.name() : __Cversion,
        __Capiversion.name() : __Capiversion,
        __condition.name() : __condition,
        __maxInstances.name() : __maxInstances,
        __generator.name() : __generator
    })



package = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'package'), CTD_ANON_12, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1154, 2))
Namespace.addCategoryObject('elementBinding', package.name().localName(), package)



DebugPortType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'jtag'), JtagType, scope=DebugPortType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 228, 6)))

DebugPortType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'swd'), SwdType, scope=DebugPortType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 229, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 228, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 229, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DebugPortType._UseForTag(pyxb.namespace.ExpandedName(None, 'jtag')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 228, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DebugPortType._UseForTag(pyxb.namespace.ExpandedName(None, 'swd')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 229, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DebugPortType._Automaton = _BuildAutomaton()




SequencesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sequence'), SequenceType, scope=SequencesType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 308, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequencesType._UseForTag(pyxb.namespace.ExpandedName(None, 'sequence')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 308, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SequencesType._Automaton = _BuildAutomaton_()




DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'compile'), CompileType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'memory'), MemoryType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'algorithm'), AlgorithmType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'book'), BookType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), DescriptionType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'feature'), DeviceFeatureType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'environment'), EnvironmentType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugport'), DebugPortType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debug'), DebugType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trace'), TraceType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugvars'), DebugVarsType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sequences'), SequencesType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'processor'), ProcessorType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugconfig'), DebugConfigType, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6)))

DeviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'variant'), CTD_ANON_11, scope=DeviceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 476, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 468, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 476, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'processor')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'debugconfig')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'compile')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'memory')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'algorithm')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'book')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'feature')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'environment')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'debugport')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'debug')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'trace')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'debugvars')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'sequences')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DeviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'variant')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 476, 6))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DeviceType._Automaton = _BuildAutomaton_2()




TaxonomyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), TaxonomyDescriptionType, scope=TaxonomyType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 806, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxonomyType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 806, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaxonomyType._Automaton = _BuildAutomaton_3()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'file'), FileType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 818, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'file')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 818, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_4()




ApisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'api'), ApiType, scope=ApisType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 831, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ApisType._UseForTag(pyxb.namespace.ExpandedName(None, 'api')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 831, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ApisType._Automaton = _BuildAutomaton_5()




ConditionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=ConditionType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 837, 6)))

ConditionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'accept'), FilterType, scope=ConditionType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 839, 8)))

ConditionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'require'), FilterType, scope=ConditionType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 840, 8)))

ConditionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deny'), FilterType, scope=ConditionType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 841, 8)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 837, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConditionType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 837, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConditionType._UseForTag(pyxb.namespace.ExpandedName(None, 'accept')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 839, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConditionType._UseForTag(pyxb.namespace.ExpandedName(None, 'require')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 840, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConditionType._UseForTag(pyxb.namespace.ExpandedName(None, 'deny')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 841, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConditionType._Automaton = _BuildAutomaton_6()




ConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'condition'), ConditionType, scope=ConditionsType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 849, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConditionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'condition')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 849, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConditionsType._Automaton = _BuildAutomaton_7()




ExampleProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'environment'), CTD_ANON_, scope=ExampleProjectType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 866, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExampleProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'environment')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 866, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExampleProjectType._Automaton = _BuildAutomaton_8()




BoardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=BoardType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 923, 6)))

BoardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'feature'), BoardFeatureType, scope=BoardType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 924, 6)))

BoardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mountedDevice'), BoardsDeviceType, scope=BoardType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 925, 6)))

BoardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'compatibleDevice'), CompatibleDeviceType, scope=BoardType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 926, 6)))

BoardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'image'), CTD_ANON_2, scope=BoardType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 927, 6)))

BoardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugInterface'), DebugInterfaceType, scope=BoardType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 933, 6)))

BoardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'book'), BoardsBookType, scope=BoardType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 934, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoardType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 923, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoardType._UseForTag(pyxb.namespace.ExpandedName(None, 'feature')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 924, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoardType._UseForTag(pyxb.namespace.ExpandedName(None, 'mountedDevice')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 925, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoardType._UseForTag(pyxb.namespace.ExpandedName(None, 'compatibleDevice')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 926, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoardType._UseForTag(pyxb.namespace.ExpandedName(None, 'image')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 927, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoardType._UseForTag(pyxb.namespace.ExpandedName(None, 'debugInterface')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 933, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoardType._UseForTag(pyxb.namespace.ExpandedName(None, 'book')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 934, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BoardType._Automaton = _BuildAutomaton_9()




BoardsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'board'), BoardType, scope=BoardsType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 951, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoardsType._UseForTag(pyxb.namespace.ExpandedName(None, 'board')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 951, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BoardsType._Automaton = _BuildAutomaton_10()




ExampleAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'category'), pyxb.binding.datatypes.string, scope=ExampleAttributesType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 957, 6)))

ExampleAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'component'), ComponentCategoryType, scope=ExampleAttributesType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 958, 6)))

ExampleAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keyword'), pyxb.binding.datatypes.string, scope=ExampleAttributesType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 959, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 957, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 958, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 959, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExampleAttributesType._UseForTag(pyxb.namespace.ExpandedName(None, 'category')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 957, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ExampleAttributesType._UseForTag(pyxb.namespace.ExpandedName(None, 'component')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 958, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ExampleAttributesType._UseForTag(pyxb.namespace.ExpandedName(None, 'keyword')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 959, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExampleAttributesType._Automaton = _BuildAutomaton_11()




ExampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=ExampleType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 966, 6)))

ExampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'board'), BoardReferenceType, scope=ExampleType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 968, 6)))

ExampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'project'), ExampleProjectType, scope=ExampleType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 970, 6)))

ExampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'attributes'), ExampleAttributesType, scope=ExampleType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 972, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 966, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'board')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 968, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'project')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 970, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'attributes')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 972, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExampleType._Automaton = _BuildAutomaton_12()




ExamplesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'example'), ExampleType, scope=ExamplesType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 989, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExamplesType._UseForTag(pyxb.namespace.ExpandedName(None, 'example')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 989, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExamplesType._Automaton = _BuildAutomaton_13()




KeywordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keyword'), pyxb.binding.datatypes.string, scope=KeywordsType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 995, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(KeywordsType._UseForTag(pyxb.namespace.ExpandedName(None, 'keyword')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 995, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
KeywordsType._Automaton = _BuildAutomaton_14()




ReleasesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'release'), ReleaseType, scope=ReleasesType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1062, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReleasesType._UseForTag(pyxb.namespace.ExpandedName(None, 'release')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1062, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReleasesType._Automaton = _BuildAutomaton_15()




GeneratorCommandArgumentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'argument'), GeneratorCommandArgumentType, scope=GeneratorCommandArgumentsType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1096, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1096, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneratorCommandArgumentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'argument')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1096, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GeneratorCommandArgumentsType._Automaton = _BuildAutomaton_16()




GeneratorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=GeneratorType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1107, 6)))

GeneratorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'select'), GeneratorDeviceSelectType, scope=GeneratorType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1108, 6)))

GeneratorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'command'), pyxb.binding.datatypes.string, scope=GeneratorType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1109, 6)))

GeneratorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'workingDir'), pyxb.binding.datatypes.string, scope=GeneratorType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1110, 6)))

GeneratorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'arguments'), GeneratorCommandArgumentsType, scope=GeneratorType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1111, 6)))

GeneratorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gpdsc'), GpdscFileType, scope=GeneratorType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1112, 6)))

GeneratorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'project_files'), CTD_ANON_3, scope=GeneratorType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1114, 6)))

GeneratorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'files'), CTD_ANON_4, scope=GeneratorType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1122, 6)))

GeneratorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'extensions'), CTD_ANON_5, scope=GeneratorType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1131, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeneratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1107, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1108, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'select')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1108, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeneratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'command')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1109, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1110, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'workingDir')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1110, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1111, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'arguments')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1111, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1112, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'gpdsc')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1112, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1114, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'project_files')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1114, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1122, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'files')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1122, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1131, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'extensions')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1131, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1108, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1110, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1111, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1112, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1114, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1122, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1131, 6))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    sub_automata.append(_BuildAutomaton_21())
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    sub_automata.append(_BuildAutomaton_24())
    sub_automata.append(_BuildAutomaton_25())
    sub_automata.append(_BuildAutomaton_26())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1106, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeneratorType._Automaton = _BuildAutomaton_17()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'file'), FileType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1117, 12)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'file')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1117, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_27()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'file'), GeneratorFileType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1126, 12)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'file')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1126, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_28()




def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1134, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1134, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_29()




GeneratorsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'generator'), GeneratorType, scope=GeneratorsType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1149, 6)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeneratorsType._UseForTag(pyxb.namespace.ExpandedName(None, 'generator')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1149, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeneratorsType._Automaton = _BuildAutomaton_30()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'family'), CTD_ANON_13, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1180, 14)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'family')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1180, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_31()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'compile'), CompileType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'memory'), MemoryType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'algorithm'), AlgorithmType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'book'), BookType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), DescriptionType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'feature'), DeviceFeatureType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'environment'), EnvironmentType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugport'), DebugPortType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debug'), DebugType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trace'), TraceType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugvars'), DebugVarsType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sequences'), SequencesType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'processor'), ProcessorType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugconfig'), DebugConfigType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device'), DeviceType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1191, 26)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 468, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'processor')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'debugconfig')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'compile')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'memory')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'algorithm')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'book')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'feature')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'environment')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'debugport')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'debug')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'trace')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'debugvars')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'sequences')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'device')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1191, 26))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_32()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bundle'), CTD_ANON_14, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1224, 14)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'component'), CTD_ANON_16, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1271, 14)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'bundle')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1224, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'component')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1271, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_33()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'file'), FileType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1242, 32)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'file')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1242, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_34()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'file'), FileType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1284, 26)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'file')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1284, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_35()




SequenceControlType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'block'), SequenceBlockType, scope=SequenceControlType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 287, 6)))

SequenceControlType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'control'), SequenceControlType, scope=SequenceControlType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 288, 6)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 275, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SequenceControlType._UseForTag(pyxb.namespace.ExpandedName(None, 'block')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 287, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SequenceControlType._UseForTag(pyxb.namespace.ExpandedName(None, 'control')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 288, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SequenceControlType._Automaton = _BuildAutomaton_36()




SequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'block'), SequenceBlockType, scope=SequenceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 287, 6)))

SequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'control'), SequenceControlType, scope=SequenceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 288, 6)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 296, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SequenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'block')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 287, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SequenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'control')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 288, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SequenceType._Automaton = _BuildAutomaton_37()




DebugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'datapatch'), DataPatchType, scope=DebugType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 316, 6)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 316, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DebugType._UseForTag(pyxb.namespace.ExpandedName(None, 'datapatch')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 316, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DebugType._Automaton = _BuildAutomaton_38()




TraceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'serialwire'), SerialWireType, scope=TraceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 346, 6)))

TraceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'traceport'), TracePortType, scope=TraceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 347, 6)))

TraceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tracebuffer'), TraceBufferType, scope=TraceType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 348, 6)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 346, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 347, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 348, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TraceType._UseForTag(pyxb.namespace.ExpandedName(None, 'serialwire')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 346, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TraceType._UseForTag(pyxb.namespace.ExpandedName(None, 'traceport')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 347, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TraceType._UseForTag(pyxb.namespace.ExpandedName(None, 'tracebuffer')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 348, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TraceType._Automaton = _BuildAutomaton_39()




def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 434, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 434, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EnvironmentType._Automaton = _BuildAutomaton_40()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'compile'), CompileType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'memory'), MemoryType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'algorithm'), AlgorithmType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'book'), BookType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), DescriptionType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'feature'), DeviceFeatureType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'environment'), EnvironmentType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugport'), DebugPortType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debug'), DebugType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trace'), TraceType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugvars'), DebugVarsType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sequences'), SequencesType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'processor'), ProcessorType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugconfig'), DebugConfigType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 468, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'processor')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'debugconfig')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'compile')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'memory')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'algorithm')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'book')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'feature')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'environment')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'debugport')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'debug')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'trace')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'debugvars')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'sequences')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_41()




ApiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=ApiType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 813, 6)))

ApiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'files'), CTD_ANON, scope=ApiType, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 815, 6)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 813, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApiType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 813, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ApiType._UseForTag(pyxb.namespace.ExpandedName(None, 'files')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 815, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ApiType._Automaton = _BuildAutomaton_42()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), RestrictedString, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1158, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vendor'), RestrictedString, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1160, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1162, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'url'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1164, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'supportContact'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1166, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'license'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1168, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'releases'), ReleasesType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1169, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keywords'), KeywordsType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1171, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'generators'), GeneratorsType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1173, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'devices'), CTD_ANON_6, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1175, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boards'), BoardsType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1209, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'taxonomy'), TaxonomyType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1212, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'apis'), ApisType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1214, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'conditions'), ConditionsType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1216, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'examples'), ExamplesType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1218, 8)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'components'), CTD_ANON_8, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1220, 8)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1158, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'vendor')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1160, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1162, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'url')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1164, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1166, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'supportContact')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1166, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1168, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'license')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1168, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'releases')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1169, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1171, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'keywords')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1171, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1173, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'generators')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1173, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1175, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'devices')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1175, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1209, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'boards')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1209, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1212, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'taxonomy')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1212, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1214, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'apis')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1214, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1216, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'conditions')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1216, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1218, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'examples')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1218, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1220, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'components')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1220, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1166, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1168, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1171, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1173, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1175, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1209, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1212, 8))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1214, 8))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1216, 8))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1218, 8))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1220, 8))
    counters.add(cc_10)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_44())
    sub_automata.append(_BuildAutomaton_45())
    sub_automata.append(_BuildAutomaton_46())
    sub_automata.append(_BuildAutomaton_47())
    sub_automata.append(_BuildAutomaton_48())
    sub_automata.append(_BuildAutomaton_49())
    sub_automata.append(_BuildAutomaton_50())
    sub_automata.append(_BuildAutomaton_51())
    sub_automata.append(_BuildAutomaton_52())
    sub_automata.append(_BuildAutomaton_53())
    sub_automata.append(_BuildAutomaton_54())
    sub_automata.append(_BuildAutomaton_55())
    sub_automata.append(_BuildAutomaton_56())
    sub_automata.append(_BuildAutomaton_57())
    sub_automata.append(_BuildAutomaton_58())
    sub_automata.append(_BuildAutomaton_59())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1156, 6)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_43()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'compile'), CompileType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'memory'), MemoryType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'algorithm'), AlgorithmType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'book'), BookType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), DescriptionType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'feature'), DeviceFeatureType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'environment'), EnvironmentType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugport'), DebugPortType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debug'), DebugType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trace'), TraceType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugvars'), DebugVarsType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sequences'), SequencesType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'processor'), ProcessorType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'debugconfig'), DebugConfigType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device'), DeviceType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1184, 20)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'subFamily'), CTD_ANON_7, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1186, 20)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 468, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1184, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1186, 20))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'processor')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 466, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'debugconfig')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 467, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'compile')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 447, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'memory')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 448, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'algorithm')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 449, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'book')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 450, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 451, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'feature')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 452, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'environment')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 453, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'debugport')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 454, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'debug')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 455, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'trace')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 456, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'debugvars')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 457, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'sequences')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 458, 6))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'device')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1184, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'subFamily')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1186, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_60()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1227, 20)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'doc'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1228, 20)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'component'), CTD_ANON_15, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1229, 20)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1227, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'doc')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1228, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'component')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1229, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_61()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deprecated'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1233, 26), unicode_default='false'))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1235, 26)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RTE_Components_h'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1237, 26)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'files'), CTD_ANON_9, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1239, 26)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1233, 26))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1237, 26))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'deprecated')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1233, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1235, 26))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'RTE_Components_h')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1237, 26))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'files')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1239, 26))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_62()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deprecated'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1275, 20), unicode_default='false'))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1277, 20)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RTE_Components_h'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1279, 20)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'files'), CTD_ANON_10, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1281, 20)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1275, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1279, 20))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'deprecated')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1275, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1277, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'RTE_Components_h')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1279, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'files')), pyxb.utils.utility.Location('/home/badi/projekte/sw/python/gpdsc/PACK.xsd', 1281, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_63()

