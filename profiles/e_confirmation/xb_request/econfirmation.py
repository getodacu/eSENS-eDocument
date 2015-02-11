# ./econfirmation.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ea6fc53702d74154a12297ea3787ddddc34f5684
# Generated 2015-02-11 21:35:49.977166 by PyXB version 1.2.4 using Python 2.6.9.final.0
# Namespace urn:eSENS:xsd:ElectronicConfirmationRequest

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
import _cva as _ImportedBinding__cva
import _ext as _ImportedBinding__ext
import _cac as _ImportedBinding__cac
import pyxb.binding.datatypes
import _cvc as _ImportedBinding__cvc
import _cbc as _ImportedBinding__cbc

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:eSENS:xsd:ElectronicConfirmationRequest', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cva = _ImportedBinding__cva.Namespace
_Namespace_cva.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cvc = _ImportedBinding__cvc.Namespace
_Namespace_cvc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cbc = _ImportedBinding__cbc.Namespace
_Namespace_cbc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ext = _ImportedBinding__ext.Namespace
_Namespace_ext.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {urn:eSENS:xsd:ElectronicConfirmationRequest}ElectronicConfirmationRequestType with content type ELEMENT_ONLY
class ElectronicConfirmationRequestType (pyxb.binding.basis.complexTypeDefinition):
    """
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElectronicConfirmationRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 35, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/corevocabulary/AggregateComponents}CompanyActivity uses Python identifier CompanyActivity
    __CompanyActivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cva, 'CompanyActivity'), 'CompanyActivity', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_httpwww_w3_orgnscorevocabularyAggregateComponentsCompanyActivity', True, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 29, 3), )

    
    CompanyActivity = property(__CompanyActivity.value, __CompanyActivity.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/AggregateComponents}HealthCareProviderCvaddress uses Python identifier HealthCareProviderCvaddress
    __HealthCareProviderCvaddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cva, 'HealthCareProviderCvaddress'), 'HealthCareProviderCvaddress', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_httpwww_w3_orgnscorevocabularyAggregateComponentsHealthCareProviderCvaddress', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 35, 3), )

    
    HealthCareProviderCvaddress = property(__HealthCareProviderCvaddress.value, __HealthCareProviderCvaddress.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/AggregateComponents}HealthInsuranceOrganizationCvaddress uses Python identifier HealthInsuranceOrganizationCvaddress
    __HealthInsuranceOrganizationCvaddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cva, 'HealthInsuranceOrganizationCvaddress'), 'HealthInsuranceOrganizationCvaddress', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_httpwww_w3_orgnscorevocabularyAggregateComponentsHealthInsuranceOrganizationCvaddress', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 36, 3), )

    
    HealthInsuranceOrganizationCvaddress = property(__HealthInsuranceOrganizationCvaddress.value, __HealthInsuranceOrganizationCvaddress.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/AggregateComponents}RequestingParty uses Python identifier RequestingParty
    __RequestingParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cva, 'RequestingParty'), 'RequestingParty', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_httpwww_w3_orgnscorevocabularyAggregateComponentsRequestingParty', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 38, 3), )

    
    RequestingParty = property(__RequestingParty.value, __RequestingParty.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}HealthCareProviderID uses Python identifier HealthCareProviderID
    __HealthCareProviderID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'HealthCareProviderID'), 'HealthCareProviderID', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_httpwww_w3_orgnscorevocabularyBasicComponentsHealthCareProviderID', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 33, 3), )

    
    HealthCareProviderID = property(__HealthCareProviderID.value, __HealthCareProviderID.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}HealthInsuranceOrganizationID uses Python identifier HealthInsuranceOrganizationID
    __HealthInsuranceOrganizationID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'HealthInsuranceOrganizationID'), 'HealthInsuranceOrganizationID', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_httpwww_w3_orgnscorevocabularyBasicComponentsHealthInsuranceOrganizationID', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 34, 3), )

    
    HealthInsuranceOrganizationID = property(__HealthInsuranceOrganizationID.value, __HealthInsuranceOrganizationID.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}RequestDate uses Python identifier RequestDate
    __RequestDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'RequestDate'), 'RequestDate', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_httpwww_w3_orgnscorevocabularyBasicComponentsRequestDate', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 39, 3), )

    
    RequestDate = property(__RequestDate.value, __RequestDate.set, None, None)

    
    # Element {http://www.w3.org/ns/corevocabulary/BasicComponents}RequestID uses Python identifier RequestID
    __RequestID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cvc, 'RequestID'), 'RequestID', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_httpwww_w3_orgnscorevocabularyBasicComponentsRequestID', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 40, 3), )

    
    RequestID = property(__RequestID.value, __RequestID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CustomizationID uses Python identifier CustomizationID
    __CustomizationID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'CustomizationID'), 'CustomizationID', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2CustomizationID', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 206, 3), )

    
    CustomizationID = property(__CustomizationID.value, __CustomizationID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ProfileExecutionID uses Python identifier ProfileExecutionID
    __ProfileExecutionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileExecutionID'), 'ProfileExecutionID', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2ProfileExecutionID', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 604, 3), )

    
    ProfileExecutionID = property(__ProfileExecutionID.value, __ProfileExecutionID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ProfileID uses Python identifier ProfileID
    __ProfileID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileID'), 'ProfileID', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2ProfileID', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 605, 3), )

    
    ProfileID = property(__ProfileID.value, __ProfileID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UBLVersionID uses Python identifier UBLVersionID
    __UBLVersionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'UBLVersionID'), 'UBLVersionID', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2UBLVersionID', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 862, 3), )

    
    UBLVersionID = property(__UBLVersionID.value, __UBLVersionID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}UBLExtensions uses Python identifier UBLExtensions
    __UBLExtensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ext, 'UBLExtensions'), 'UBLExtensions', '__urneSENSxsdElectronicConfirmationRequest_ElectronicConfirmationRequestType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2UBLExtensions', False, pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 21, 2), )

    
    UBLExtensions = property(__UBLExtensions.value, __UBLExtensions.set, None, '\n        A container for all extensions present in the document.\n      ')

    _ElementMap.update({
        __CompanyActivity.name() : __CompanyActivity,
        __HealthCareProviderCvaddress.name() : __HealthCareProviderCvaddress,
        __HealthInsuranceOrganizationCvaddress.name() : __HealthInsuranceOrganizationCvaddress,
        __RequestingParty.name() : __RequestingParty,
        __HealthCareProviderID.name() : __HealthCareProviderID,
        __HealthInsuranceOrganizationID.name() : __HealthInsuranceOrganizationID,
        __RequestDate.name() : __RequestDate,
        __RequestID.name() : __RequestID,
        __CustomizationID.name() : __CustomizationID,
        __ProfileExecutionID.name() : __ProfileExecutionID,
        __ProfileID.name() : __ProfileID,
        __UBLVersionID.name() : __UBLVersionID,
        __UBLExtensions.name() : __UBLExtensions
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ElectronicConfirmationRequestType', ElectronicConfirmationRequestType)


ElectronicConfirmationRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ElectronicConfirmationRequest'), ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 31, 3))
Namespace.addCategoryObject('elementBinding', ElectronicConfirmationRequest.name().localName(), ElectronicConfirmationRequest)



ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cva, 'CompanyActivity'), _ImportedBinding__cva.CompanyActivityType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 29, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cva, 'HealthCareProviderCvaddress'), _ImportedBinding__cva.CvaddressType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 35, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cva, 'HealthInsuranceOrganizationCvaddress'), _ImportedBinding__cva.CvaddressType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 36, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cva, 'RequestingParty'), _ImportedBinding__cac.PartyType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyAggregateComponents.xsd', 38, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'HealthCareProviderID'), _ImportedBinding__cvc.HealthCareProviderIDType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 33, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'HealthInsuranceOrganizationID'), _ImportedBinding__cvc.HealthInsuranceOrganizationIDType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 34, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'RequestDate'), _ImportedBinding__cvc.RequestDateType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 39, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cvc, 'RequestID'), _ImportedBinding__cvc.RequestIDType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/CoreVocabularyBasicComponents.xsd', 40, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'CustomizationID'), _ImportedBinding__cbc.CustomizationIDType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 206, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileExecutionID'), _ImportedBinding__cbc.ProfileExecutionIDType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 604, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileID'), _ImportedBinding__cbc.ProfileIDType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 605, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'UBLVersionID'), _ImportedBinding__cbc.UBLVersionIDType, scope=ElectronicConfirmationRequestType, location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 862, 3)))

ElectronicConfirmationRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ext, 'UBLExtensions'), _ImportedBinding__ext.UBLExtensionsType, scope=ElectronicConfirmationRequestType, documentation='\n        A container for all extensions present in the document.\n      ', location=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 21, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 47, 11))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 52, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 69, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 85, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 101, 9))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ext, 'UBLExtensions')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 47, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'UBLVersionID')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 52, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'CustomizationID')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 69, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileID')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 85, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileExecutionID')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 101, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'RequestDate')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 117, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'RequestID')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 133, 9))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'HealthCareProviderID')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 149, 9))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cvc, 'HealthInsuranceOrganizationID')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 165, 9))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cva, 'HealthCareProviderCvaddress')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 181, 9))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cva, 'HealthInsuranceOrganizationCvaddress')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 198, 9))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cva, 'CompanyActivity')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 215, 9))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ElectronicConfirmationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cva, 'RequestingParty')), pyxb.utils.utility.Location('/home/esens/edocument/profiles/e_confirmation/xsd/request/ElectronicConfirmationRequest.xsd', 231, 9))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ElectronicConfirmationRequestType._Automaton = _BuildAutomaton()

