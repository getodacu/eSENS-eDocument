# ./_cvc.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2590ac6675f7dc6a1ef34beec1fcf361b1df306e
# Generated 2015-02-11 21:35:49.973647 by PyXB version 1.2.4 using Python 2.6.9.final.0
# Namespace http://www.w3.org/ns/corevocabulary/BasicComponents [xmlns:cvc]

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
import _udt as _ImportedBinding__udt
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/ns/corevocabulary/BasicComponents', create_if_missing=True)
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


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}DeathDateType with content type SIMPLE
class DeathDateType (_ImportedBinding__udt.DateType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}DeathDateType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.date
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeathDateType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 73, 3)
    _ElementMap = _ImportedBinding__udt.DateType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.DateType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.DateType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DeathDateType', DeathDateType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}RequestDateType with content type SIMPLE
class RequestDateType (_ImportedBinding__udt.DateType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}RequestDateType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.date
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestDateType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 113, 3)
    _ElementMap = _ImportedBinding__udt.DateType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.DateType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.DateType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RequestDateType', RequestDateType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}ActivityCodeType with content type SIMPLE
class ActivityCodeType (_ImportedBinding__udt.CodeType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}ActivityCodeType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActivityCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 43, 3)
    _ElementMap = _ImportedBinding__udt.CodeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.CodeType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.CodeType
    
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
Namespace.addCategoryObject('typeBinding', 'ActivityCodeType', ActivityCodeType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}ActivityDescriptionType with content type SIMPLE
class ActivityDescriptionType (_ImportedBinding__udt.TextType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}ActivityDescriptionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActivityDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 48, 3)
    _ElementMap = _ImportedBinding__udt.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ActivityDescriptionType', ActivityDescriptionType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}AdminunitFirstlineType with content type SIMPLE
class AdminunitFirstlineType (_ImportedBinding__udt.TextType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}AdminunitFirstlineType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdminunitFirstlineType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 53, 3)
    _ElementMap = _ImportedBinding__udt.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AdminunitFirstlineType', AdminunitFirstlineType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}AlternativeNameType with content type SIMPLE
class AlternativeNameType (_ImportedBinding__udt.TextType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}AlternativeNameType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlternativeNameType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 58, 3)
    _ElementMap = _ImportedBinding__udt.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AlternativeNameType', AlternativeNameType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}CompanyStatusCodeType with content type SIMPLE
class CompanyStatusCodeType (_ImportedBinding__udt.CodeType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}CompanyStatusCodeType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompanyStatusCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 63, 3)
    _ElementMap = _ImportedBinding__udt.CodeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.CodeType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.CodeType
    
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
Namespace.addCategoryObject('typeBinding', 'CompanyStatusCodeType', CompanyStatusCodeType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}CompanyTypeCodeType with content type SIMPLE
class CompanyTypeCodeType (_ImportedBinding__udt.CodeType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}CompanyTypeCodeType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompanyTypeCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 68, 3)
    _ElementMap = _ImportedBinding__udt.CodeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.CodeType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.CodeType
    
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
Namespace.addCategoryObject('typeBinding', 'CompanyTypeCodeType', CompanyTypeCodeType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}GeographicIDType with content type SIMPLE
class GeographicIDType (_ImportedBinding__udt.IdentifierType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}GeographicIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeographicIDType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 78, 3)
    _ElementMap = _ImportedBinding__udt.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.IdentifierType
    
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
Namespace.addCategoryObject('typeBinding', 'GeographicIDType', GeographicIDType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}GeographicNameType with content type SIMPLE
class GeographicNameType (_ImportedBinding__udt.TextType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}GeographicNameType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeographicNameType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 83, 3)
    _ElementMap = _ImportedBinding__udt.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GeographicNameType', GeographicNameType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}HealthCareProviderIDType with content type SIMPLE
class HealthCareProviderIDType (_ImportedBinding__udt.IdentifierType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}HealthCareProviderIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HealthCareProviderIDType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 88, 3)
    _ElementMap = _ImportedBinding__udt.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.IdentifierType
    
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
Namespace.addCategoryObject('typeBinding', 'HealthCareProviderIDType', HealthCareProviderIDType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}HealthInsuranceOrganizationIDType with content type SIMPLE
class HealthInsuranceOrganizationIDType (_ImportedBinding__udt.IdentifierType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}HealthInsuranceOrganizationIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HealthInsuranceOrganizationIDType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 93, 3)
    _ElementMap = _ImportedBinding__udt.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.IdentifierType
    
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
Namespace.addCategoryObject('typeBinding', 'HealthInsuranceOrganizationIDType', HealthInsuranceOrganizationIDType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}JurisdictionIDType with content type SIMPLE
class JurisdictionIDType (_ImportedBinding__udt.IdentifierType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}JurisdictionIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JurisdictionIDType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 98, 3)
    _ElementMap = _ImportedBinding__udt.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.IdentifierType
    
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
Namespace.addCategoryObject('typeBinding', 'JurisdictionIDType', JurisdictionIDType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}LegalIDType with content type SIMPLE
class LegalIDType (_ImportedBinding__udt.IdentifierType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}LegalIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LegalIDType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 103, 3)
    _ElementMap = _ImportedBinding__udt.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.IdentifierType
    
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
Namespace.addCategoryObject('typeBinding', 'LegalIDType', LegalIDType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}LegalNameType with content type SIMPLE
class LegalNameType (_ImportedBinding__udt.TextType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}LegalNameType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LegalNameType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 108, 3)
    _ElementMap = _ImportedBinding__udt.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'LegalNameType', LegalNameType)


# Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}RequestIDType with content type SIMPLE
class RequestIDType (_ImportedBinding__udt.IdentifierType):
    """Complex type {http://www.w3.org/ns/corevocabulary/BasicComponents}RequestIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestIDType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 118, 3)
    _ElementMap = _ImportedBinding__udt.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.IdentifierType
    
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
Namespace.addCategoryObject('typeBinding', 'RequestIDType', RequestIDType)


DeathDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeathDate'), DeathDateType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 30, 3))
Namespace.addCategoryObject('elementBinding', DeathDate.name().localName(), DeathDate)

RequestDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestDate'), RequestDateType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 39, 3))
Namespace.addCategoryObject('elementBinding', RequestDate.name().localName(), RequestDate)

ActivityCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ActivityCode'), ActivityCodeType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 24, 3))
Namespace.addCategoryObject('elementBinding', ActivityCode.name().localName(), ActivityCode)

ActivityDescription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ActivityDescription'), ActivityDescriptionType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 25, 3))
Namespace.addCategoryObject('elementBinding', ActivityDescription.name().localName(), ActivityDescription)

AdminunitFirstline = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdminunitFirstline'), AdminunitFirstlineType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 26, 3))
Namespace.addCategoryObject('elementBinding', AdminunitFirstline.name().localName(), AdminunitFirstline)

AlternativeName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AlternativeName'), AlternativeNameType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 27, 3))
Namespace.addCategoryObject('elementBinding', AlternativeName.name().localName(), AlternativeName)

CompanyStatusCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompanyStatusCode'), CompanyStatusCodeType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 28, 3))
Namespace.addCategoryObject('elementBinding', CompanyStatusCode.name().localName(), CompanyStatusCode)

CompanyTypeCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompanyTypeCode'), CompanyTypeCodeType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 29, 3))
Namespace.addCategoryObject('elementBinding', CompanyTypeCode.name().localName(), CompanyTypeCode)

GeographicID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeographicID'), GeographicIDType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 31, 3))
Namespace.addCategoryObject('elementBinding', GeographicID.name().localName(), GeographicID)

GeographicName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeographicName'), GeographicNameType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 32, 3))
Namespace.addCategoryObject('elementBinding', GeographicName.name().localName(), GeographicName)

HealthCareProviderID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HealthCareProviderID'), HealthCareProviderIDType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 33, 3))
Namespace.addCategoryObject('elementBinding', HealthCareProviderID.name().localName(), HealthCareProviderID)

HealthInsuranceOrganizationID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HealthInsuranceOrganizationID'), HealthInsuranceOrganizationIDType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 34, 3))
Namespace.addCategoryObject('elementBinding', HealthInsuranceOrganizationID.name().localName(), HealthInsuranceOrganizationID)

JurisdictionID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JurisdictionID'), JurisdictionIDType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 36, 3))
Namespace.addCategoryObject('elementBinding', JurisdictionID.name().localName(), JurisdictionID)

LegalID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LegalID'), LegalIDType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 37, 3))
Namespace.addCategoryObject('elementBinding', LegalID.name().localName(), LegalID)

LegalName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LegalName'), LegalNameType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 38, 3))
Namespace.addCategoryObject('elementBinding', LegalName.name().localName(), LegalName)

RequestID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestID'), RequestIDType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 40, 3))
Namespace.addCategoryObject('elementBinding', RequestID.name().localName(), RequestID)
