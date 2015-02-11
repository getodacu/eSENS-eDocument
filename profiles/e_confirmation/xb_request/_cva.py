# ./_cva.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0e147dec76d8c2b51297ad67e17a0cd03d4fe522
# Generated 2015-02-11 21:35:49.973888 by PyXB version 1.2.4 using Python 2.6.9.final.0
# Namespace http://www.w3.org/ns/corevocabulary/AggregateComponents [xmlns:cva]

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
import _cvc as _ImportedBinding__cvc
import _cbc as _ImportedBinding__cbc
import _cac as _ImportedBinding__cac

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/ns/corevocabulary/AggregateComponents', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cvc = _ImportedBinding__cvc.Namespace
_Namespace_cvc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cac = _ImportedBinding__cac.Namespace
_Namespace_cac.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cbc = _ImportedBinding__cbc.Namespace
_Namespace_cbc.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://www.w3.org/ns/corevocabulary/AggregateComponents}CompanyActivityType with content type ELEMENT_ONLY
class CompanyActivityType (pyxb.binding.basis.complexTypeDefinition):
    """
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompanyActivityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 42, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}ActivityCode uses Python identifier ActivityCode
    __ActivityCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'ActivityCode'), 'ActivityCode', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CompanyActivityType_httpwww_w3_orgnscorevocabularyBasicComponentsActivityCode', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 24, 3), )

    
    ActivityCode = property(__ActivityCode.value, __ActivityCode.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}ActivityDescription uses Python identifier ActivityDescription
    __ActivityDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'ActivityDescription'), 'ActivityDescription', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CompanyActivityType_httpwww_w3_orgnscorevocabularyBasicComponentsActivityDescription', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 25, 3), )

    
    ActivityDescription = property(__ActivityDescription.value, __ActivityDescription.set, None, None)

    _ElementMap.update({
        __ActivityCode.name() : __ActivityCode,
        __ActivityDescription.name() : __ActivityDescription
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CompanyActivityType', CompanyActivityType)


# Complex type {http://www.w3.org/ns/corevocabulary/AggregateComponents}CvaddressType with content type ELEMENT_ONLY
class CvaddressType (pyxb.binding.basis.complexTypeDefinition):
    """
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CvaddressType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 90, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}AdminunitFirstline uses Python identifier AdminunitFirstline
    __AdminunitFirstline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'AdminunitFirstline'), 'AdminunitFirstline', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvaddressType_httpwww_w3_orgnscorevocabularyBasicComponentsAdminunitFirstline', True, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 26, 3), )

    
    AdminunitFirstline = property(__AdminunitFirstline.value, __AdminunitFirstline.set, None, None)

    _ElementMap.update({
        __AdminunitFirstline.name() : __AdminunitFirstline
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CvaddressType', CvaddressType)


# Complex type {http://www.w3.org/ns/corevocabulary/AggregateComponents}CvbusinessType with content type ELEMENT_ONLY
class CvbusinessType (pyxb.binding.basis.complexTypeDefinition):
    """
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CvbusinessType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 120, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/corevocabulary/AggregateComponents}BusinessAddress uses Python identifier BusinessAddress
    __BusinessAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BusinessAddress'), 'BusinessAddress', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvbusinessType_httpwww_w3_orgnscorevocabularyAggregateComponentsBusinessAddress', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 27, 3), )

    
    BusinessAddress = property(__BusinessAddress.value, __BusinessAddress.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/AggregateComponents}CompanyActivity uses Python identifier CompanyActivity
    __CompanyActivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompanyActivity'), 'CompanyActivity', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvbusinessType_httpwww_w3_orgnscorevocabularyAggregateComponentsCompanyActivity', True, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 29, 3), )

    
    CompanyActivity = property(__CompanyActivity.value, __CompanyActivity.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}AlternativeName uses Python identifier AlternativeName
    __AlternativeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'AlternativeName'), 'AlternativeName', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvbusinessType_httpwww_w3_orgnscorevocabularyBasicComponentsAlternativeName', True, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 27, 3), )

    
    AlternativeName = property(__AlternativeName.value, __AlternativeName.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}CompanyStatusCode uses Python identifier CompanyStatusCode
    __CompanyStatusCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'CompanyStatusCode'), 'CompanyStatusCode', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvbusinessType_httpwww_w3_orgnscorevocabularyBasicComponentsCompanyStatusCode', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 28, 3), )

    
    CompanyStatusCode = property(__CompanyStatusCode.value, __CompanyStatusCode.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}CompanyTypeCode uses Python identifier CompanyTypeCode
    __CompanyTypeCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'CompanyTypeCode'), 'CompanyTypeCode', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvbusinessType_httpwww_w3_orgnscorevocabularyBasicComponentsCompanyTypeCode', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 29, 3), )

    
    CompanyTypeCode = property(__CompanyTypeCode.value, __CompanyTypeCode.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}LegalID uses Python identifier LegalID
    __LegalID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'LegalID'), 'LegalID', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvbusinessType_httpwww_w3_orgnscorevocabularyBasicComponentsLegalID', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 37, 3), )

    
    LegalID = property(__LegalID.value, __LegalID.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}LegalName uses Python identifier LegalName
    __LegalName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'LegalName'), 'LegalName', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvbusinessType_httpwww_w3_orgnscorevocabularyBasicComponentsLegalName', True, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 38, 3), )

    
    LegalName = property(__LegalName.value, __LegalName.set, None, None)

    _ElementMap.update({
        __BusinessAddress.name() : __BusinessAddress,
        __CompanyActivity.name() : __CompanyActivity,
        __AlternativeName.name() : __AlternativeName,
        __CompanyStatusCode.name() : __CompanyStatusCode,
        __CompanyTypeCode.name() : __CompanyTypeCode,
        __LegalID.name() : __LegalID,
        __LegalName.name() : __LegalName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CvbusinessType', CvbusinessType)


# Complex type {http://www.w3.org/ns/corevocabulary/AggregateComponents}CvlocationType with content type ELEMENT_ONLY
class CvlocationType (pyxb.binding.basis.complexTypeDefinition):
    """
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CvlocationType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 247, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'Address'), 'Address', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvlocationType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2Address', True, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 45, 3), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}GeographicID uses Python identifier GeographicID
    __GeographicID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'GeographicID'), 'GeographicID', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvlocationType_httpwww_w3_orgnscorevocabularyBasicComponentsGeographicID', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 31, 3), )

    
    GeographicID = property(__GeographicID.value, __GeographicID.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}GeographicName uses Python identifier GeographicName
    __GeographicName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'GeographicName'), 'GeographicName', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvlocationType_httpwww_w3_orgnscorevocabularyBasicComponentsGeographicName', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 32, 3), )

    
    GeographicName = property(__GeographicName.value, __GeographicName.set, None, None)

    _ElementMap.update({
        __Address.name() : __Address,
        __GeographicID.name() : __GeographicID,
        __GeographicName.name() : __GeographicName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CvlocationType', CvlocationType)


# Complex type {http://www.w3.org/ns/corevocabulary/AggregateComponents}CvpersonType with content type ELEMENT_ONLY
class CvpersonType (pyxb.binding.basis.complexTypeDefinition):
    """
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CvpersonType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 309, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'Person'), 'Person', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvpersonType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2Person', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 406, 3), )

    
    Person = property(__Person.value, __Person.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/AggregateComponents}BirthPlaceCvlocation uses Python identifier BirthPlaceCvlocation
    __BirthPlaceCvlocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BirthPlaceCvlocation'), 'BirthPlaceCvlocation', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvpersonType_httpwww_w3_orgnscorevocabularyAggregateComponentsBirthPlaceCvlocation', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 26, 3), )

    
    BirthPlaceCvlocation = property(__BirthPlaceCvlocation.value, __BirthPlaceCvlocation.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/AggregateComponents}CitizenshipJurisdiction uses Python identifier CitizenshipJurisdiction
    __CitizenshipJurisdiction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CitizenshipJurisdiction'), 'CitizenshipJurisdiction', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvpersonType_httpwww_w3_orgnscorevocabularyAggregateComponentsCitizenshipJurisdiction', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 28, 3), )

    
    CitizenshipJurisdiction = property(__CitizenshipJurisdiction.value, __CitizenshipJurisdiction.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/AggregateComponents}DeathPlaceCvlocation uses Python identifier DeathPlaceCvlocation
    __DeathPlaceCvlocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DeathPlaceCvlocation'), 'DeathPlaceCvlocation', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvpersonType_httpwww_w3_orgnscorevocabularyAggregateComponentsDeathPlaceCvlocation', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 34, 3), )

    
    DeathPlaceCvlocation = property(__DeathPlaceCvlocation.value, __DeathPlaceCvlocation.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/AggregateComponents}ResidencyJurisdiction uses Python identifier ResidencyJurisdiction
    __ResidencyJurisdiction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResidencyJurisdiction'), 'ResidencyJurisdiction', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvpersonType_httpwww_w3_orgnscorevocabularyAggregateComponentsResidencyJurisdiction', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 39, 3), )

    
    ResidencyJurisdiction = property(__ResidencyJurisdiction.value, __ResidencyJurisdiction.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}DeathDate uses Python identifier DeathDate
    __DeathDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'DeathDate'), 'DeathDate', '__httpwww_w3_orgnscorevocabularyAggregateComponents_CvpersonType_httpwww_w3_orgnscorevocabularyBasicComponentsDeathDate', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 30, 3), )

    
    DeathDate = property(__DeathDate.value, __DeathDate.set, None, None)

    _ElementMap.update({
        __Person.name() : __Person,
        __BirthPlaceCvlocation.name() : __BirthPlaceCvlocation,
        __CitizenshipJurisdiction.name() : __CitizenshipJurisdiction,
        __DeathPlaceCvlocation.name() : __DeathPlaceCvlocation,
        __ResidencyJurisdiction.name() : __ResidencyJurisdiction,
        __DeathDate.name() : __DeathDate
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CvpersonType', CvpersonType)


# Complex type {http://www.w3.org/ns/corevocabulary/AggregateComponents}JurisdictionType with content type ELEMENT_ONLY
class JurisdictionType (pyxb.binding.basis.complexTypeDefinition):
    """
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JurisdictionType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 423, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}JurisdictionID uses Python identifier JurisdictionID
    __JurisdictionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'JurisdictionID'), 'JurisdictionID', '__httpwww_w3_orgnscorevocabularyAggregateComponents_JurisdictionType_httpwww_w3_orgnscorevocabularyBasicComponentsJurisdictionID', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 36, 3), )

    
    JurisdictionID = property(__JurisdictionID.value, __JurisdictionID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'Name'), 'Name', '__httpwww_w3_orgnscorevocabularyAggregateComponents_JurisdictionType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2Name', False, pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 475, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    _ElementMap.update({
        __JurisdictionID.name() : __JurisdictionID,
        __Name.name() : __Name
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'JurisdictionType', JurisdictionType)


BirthPlaceCvlocation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BirthPlaceCvlocation'), CvlocationType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 26, 3))
Namespace.addCategoryObject('elementBinding', BirthPlaceCvlocation.name().localName(), BirthPlaceCvlocation)

BusinessAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BusinessAddress'), _ImportedBinding__cac.AddressType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 27, 3))
Namespace.addCategoryObject('elementBinding', BusinessAddress.name().localName(), BusinessAddress)

CitizenshipJurisdiction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CitizenshipJurisdiction'), JurisdictionType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 28, 3))
Namespace.addCategoryObject('elementBinding', CitizenshipJurisdiction.name().localName(), CitizenshipJurisdiction)

CompanyActivity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompanyActivity'), CompanyActivityType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 29, 3))
Namespace.addCategoryObject('elementBinding', CompanyActivity.name().localName(), CompanyActivity)

Cvaddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cvaddress'), CvaddressType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 30, 3))
Namespace.addCategoryObject('elementBinding', Cvaddress.name().localName(), Cvaddress)

Cvbusiness = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cvbusiness'), CvbusinessType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 31, 3))
Namespace.addCategoryObject('elementBinding', Cvbusiness.name().localName(), Cvbusiness)

Cvlocation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cvlocation'), CvlocationType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 32, 3))
Namespace.addCategoryObject('elementBinding', Cvlocation.name().localName(), Cvlocation)

Cvperson = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cvperson'), CvpersonType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 33, 3))
Namespace.addCategoryObject('elementBinding', Cvperson.name().localName(), Cvperson)

DeathPlaceCvlocation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeathPlaceCvlocation'), CvlocationType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 34, 3))
Namespace.addCategoryObject('elementBinding', DeathPlaceCvlocation.name().localName(), DeathPlaceCvlocation)

HealthCareProviderCvaddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HealthCareProviderCvaddress'), CvaddressType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 35, 3))
Namespace.addCategoryObject('elementBinding', HealthCareProviderCvaddress.name().localName(), HealthCareProviderCvaddress)

HealthInsuranceOrganizationCvaddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HealthInsuranceOrganizationCvaddress'), CvaddressType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 36, 3))
Namespace.addCategoryObject('elementBinding', HealthInsuranceOrganizationCvaddress.name().localName(), HealthInsuranceOrganizationCvaddress)

Jurisdiction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Jurisdiction'), JurisdictionType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 37, 3))
Namespace.addCategoryObject('elementBinding', Jurisdiction.name().localName(), Jurisdiction)

RequestingParty = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestingParty'), _ImportedBinding__cac.PartyType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 38, 3))
Namespace.addCategoryObject('elementBinding', RequestingParty.name().localName(), RequestingParty)

ResidencyJurisdiction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResidencyJurisdiction'), JurisdictionType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 39, 3))
Namespace.addCategoryObject('elementBinding', ResidencyJurisdiction.name().localName(), ResidencyJurisdiction)



CompanyActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'ActivityCode'), _ImportedBinding__cvc.ActivityCodeType, scope=CompanyActivityType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 24, 3)))

CompanyActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'ActivityDescription'), _ImportedBinding__cvc.ActivityDescriptionType, scope=CompanyActivityType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 25, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CompanyActivityType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'ActivityCode')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 54, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CompanyActivityType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'ActivityDescription')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 71, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CompanyActivityType._Automaton = _BuildAutomaton()




CvaddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'AdminunitFirstline'), _ImportedBinding__cvc.AdminunitFirstlineType, scope=CvaddressType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 26, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 102, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CvaddressType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'AdminunitFirstline')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 102, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CvaddressType._Automaton = _BuildAutomaton_()




CvbusinessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BusinessAddress'), _ImportedBinding__cac.AddressType, scope=CvbusinessType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 27, 3)))

CvbusinessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompanyActivity'), CompanyActivityType, scope=CvbusinessType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 29, 3)))

CvbusinessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'AlternativeName'), _ImportedBinding__cvc.AlternativeNameType, scope=CvbusinessType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 27, 3)))

CvbusinessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'CompanyStatusCode'), _ImportedBinding__cvc.CompanyStatusCodeType, scope=CvbusinessType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 28, 3)))

CvbusinessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'CompanyTypeCode'), _ImportedBinding__cvc.CompanyTypeCodeType, scope=CvbusinessType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 29, 3)))

CvbusinessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'LegalID'), _ImportedBinding__cvc.LegalIDType, scope=CvbusinessType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 37, 3)))

CvbusinessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'LegalName'), _ImportedBinding__cvc.LegalNameType, scope=CvbusinessType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 38, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 148, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 164, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 180, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 196, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 212, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 228, 9))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CvbusinessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'LegalID')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 132, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CvbusinessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'LegalName')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 148, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CvbusinessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'AlternativeName')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 164, 9))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CvbusinessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'CompanyStatusCode')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 180, 9))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CvbusinessType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'CompanyTypeCode')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 196, 9))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CvbusinessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompanyActivity')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 212, 9))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CvbusinessType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BusinessAddress')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 228, 9))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
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
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CvbusinessType._Automaton = _BuildAutomaton_2()




CvlocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'Address'), _ImportedBinding__cac.AddressType, scope=CvlocationType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 45, 3)))

CvlocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'GeographicID'), _ImportedBinding__cvc.GeographicIDType, scope=CvlocationType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 31, 3)))

CvlocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'GeographicName'), _ImportedBinding__cvc.GeographicNameType, scope=CvlocationType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 32, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 259, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 275, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 291, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CvlocationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'GeographicID')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 259, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CvlocationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'GeographicName')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 275, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CvlocationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'Address')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 291, 9))
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
CvlocationType._Automaton = _BuildAutomaton_3()




CvpersonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'Person'), _ImportedBinding__cac.PersonType, scope=CvpersonType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 406, 3)))

CvpersonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BirthPlaceCvlocation'), CvlocationType, scope=CvpersonType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 26, 3)))

CvpersonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CitizenshipJurisdiction'), JurisdictionType, scope=CvpersonType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 28, 3)))

CvpersonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeathPlaceCvlocation'), CvlocationType, scope=CvpersonType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 34, 3)))

CvpersonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResidencyJurisdiction'), JurisdictionType, scope=CvpersonType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 39, 3)))

CvpersonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'DeathDate'), _ImportedBinding__cvc.DeathDateType, scope=CvpersonType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 30, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 321, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 337, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 354, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 371, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 388, 9))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CvpersonType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'DeathDate')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 321, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CvpersonType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResidencyJurisdiction')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 337, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CvpersonType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CitizenshipJurisdiction')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 354, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CvpersonType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DeathPlaceCvlocation')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 371, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CvpersonType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BirthPlaceCvlocation')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 388, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CvpersonType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'Person')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 405, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CvpersonType._Automaton = _BuildAutomaton_4()




JurisdictionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'JurisdictionID'), _ImportedBinding__cvc.JurisdictionIDType, scope=JurisdictionType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 36, 3)))

JurisdictionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'Name'), _ImportedBinding__cbc.NameType, scope=JurisdictionType, location=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 475, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 451, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(JurisdictionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'JurisdictionID')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 435, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JurisdictionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'Name')), pyxb.utils.utility.Location('/Users/radu/Projects/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 451, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
JurisdictionType._Automaton = _BuildAutomaton_5()

