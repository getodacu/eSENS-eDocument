# ./_udt.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3b8316427b9d04ab971fa43e6eb74533d8e2824e
# Generated 2015-02-11 21:35:49.972873 by PyXB version 1.2.4 using Python 2.6.9.final.0
# Namespace urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2 [xmlns:udt]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2b2e2fd1-b225-11e4-b26c-14109fe53921')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _ccts_cct as _ImportedBinding__ccts_cct

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2', create_if_missing=True)
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


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}DateTimeType with content type SIMPLE
class DateTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
        
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.dateTime
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateTimeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 165, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.dateTime
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DateTimeType', DateTimeType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}DateType with content type SIMPLE
class DateType (pyxb.binding.basis.complexTypeDefinition):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.date
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 183, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.date
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DateType', DateType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}TimeType with content type SIMPLE
class TimeType (pyxb.binding.basis.complexTypeDefinition):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.time
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 200, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.time
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TimeType', TimeType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}IndicatorType with content type SIMPLE
class IndicatorType (pyxb.binding.basis.complexTypeDefinition):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 235, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'IndicatorType', IndicatorType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}AmountType with content type SIMPLE
class AmountType (_ImportedBinding__ccts_cct.AmountType):
    """
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AmountType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 46, 2)
    _ElementMap = _ImportedBinding__ccts_cct.AmountType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.AmountType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.AmountType
    
    # Attribute currencyID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}AmountType
    
    # Attribute currencyCodeListVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}AmountType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AmountType', AmountType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}BinaryObjectType with content type SIMPLE
class BinaryObjectType (_ImportedBinding__ccts_cct.BinaryObjectType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 62, 2)
    _ElementMap = _ImportedBinding__ccts_cct.BinaryObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.BinaryObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.BinaryObjectType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute mimeCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute encodingCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute characterSetCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute uri inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute filename inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BinaryObjectType', BinaryObjectType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}GraphicType with content type SIMPLE
class GraphicType (_ImportedBinding__ccts_cct.BinaryObjectType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GraphicType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 79, 2)
    _ElementMap = _ImportedBinding__ccts_cct.BinaryObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.BinaryObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.BinaryObjectType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute mimeCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute encodingCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute characterSetCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute uri inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute filename inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GraphicType', GraphicType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}PictureType with content type SIMPLE
class PictureType (_ImportedBinding__ccts_cct.BinaryObjectType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PictureType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 96, 2)
    _ElementMap = _ImportedBinding__ccts_cct.BinaryObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.BinaryObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.BinaryObjectType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute mimeCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute encodingCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute characterSetCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute uri inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute filename inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'PictureType', PictureType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}SoundType with content type SIMPLE
class SoundType (_ImportedBinding__ccts_cct.BinaryObjectType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoundType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 113, 2)
    _ElementMap = _ImportedBinding__ccts_cct.BinaryObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.BinaryObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.BinaryObjectType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute mimeCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute encodingCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute characterSetCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute uri inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute filename inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SoundType', SoundType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}VideoType with content type SIMPLE
class VideoType (_ImportedBinding__ccts_cct.BinaryObjectType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 130, 2)
    _ElementMap = _ImportedBinding__ccts_cct.BinaryObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.BinaryObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.BinaryObjectType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute mimeCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute encodingCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute characterSetCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute uri inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute filename inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'VideoType', VideoType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}CodeType with content type SIMPLE
class CodeType (_ImportedBinding__ccts_cct.CodeType):
    """
        
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 147, 2)
    _ElementMap = _ImportedBinding__ccts_cct.CodeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.CodeType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.CodeType
    
    # Attribute listID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listAgencyID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listAgencyName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute name inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listSchemeURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CodeType', CodeType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}IdentifierType with content type SIMPLE
class IdentifierType (_ImportedBinding__ccts_cct.IdentifierType):
    """
        
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 217, 2)
    _ElementMap = _ImportedBinding__ccts_cct.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.IdentifierType
    
    # Attribute schemeID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeAgencyID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeAgencyName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeDataURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'IdentifierType', IdentifierType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}MeasureType with content type SIMPLE
class MeasureType (_ImportedBinding__ccts_cct.MeasureType):
    """
        
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 252, 2)
    _ElementMap = _ImportedBinding__ccts_cct.MeasureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.MeasureType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.MeasureType
    
    # Attribute unitCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}MeasureType
    
    # Attribute unitCodeListVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}MeasureType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'MeasureType', MeasureType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}NumericType with content type SIMPLE
class NumericType (_ImportedBinding__ccts_cct.NumericType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NumericType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 270, 2)
    _ElementMap = _ImportedBinding__ccts_cct.NumericType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.NumericType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.NumericType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}NumericType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'NumericType', NumericType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}ValueType with content type SIMPLE
class ValueType (_ImportedBinding__ccts_cct.NumericType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 287, 2)
    _ElementMap = _ImportedBinding__ccts_cct.NumericType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.NumericType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.NumericType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}NumericType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ValueType', ValueType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}PercentType with content type SIMPLE
class PercentType (_ImportedBinding__ccts_cct.NumericType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 304, 2)
    _ElementMap = _ImportedBinding__ccts_cct.NumericType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.NumericType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.NumericType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}NumericType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'PercentType', PercentType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}RateType with content type SIMPLE
class RateType (_ImportedBinding__ccts_cct.NumericType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RateType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 321, 2)
    _ElementMap = _ImportedBinding__ccts_cct.NumericType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.NumericType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.NumericType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}NumericType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RateType', RateType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}QuantityType with content type SIMPLE
class QuantityType (_ImportedBinding__ccts_cct.QuantityType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QuantityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 338, 2)
    _ElementMap = _ImportedBinding__ccts_cct.QuantityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.QuantityType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.QuantityType
    
    # Attribute unitCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}QuantityType
    
    # Attribute unitCodeListID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}QuantityType
    
    # Attribute unitCodeListAgencyID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}QuantityType
    
    # Attribute unitCodeListAgencyName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}QuantityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'QuantityType', QuantityType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}TextType with content type SIMPLE
class TextType (_ImportedBinding__ccts_cct.TextType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 355, 2)
    _ElementMap = _ImportedBinding__ccts_cct.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TextType', TextType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}NameType with content type SIMPLE
class NameType (_ImportedBinding__ccts_cct.TextType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 372, 2)
    _ElementMap = _ImportedBinding__ccts_cct.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'NameType', NameType)

