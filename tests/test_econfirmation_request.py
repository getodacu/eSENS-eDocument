from __future__ import print_function
import os
import sys
import pyxb.binding.datatypes as xs

PATH_PROFILES = os.path.dirname(os.path.realpath(__file__))+os.path.sep+".."+os.path.sep+"profiles"
sys.path.append(PATH_PROFILES)

from e_confirmation.xb_request.econfirmation import *
from e_confirmation.xb_request._cva import *
from e_confirmation.xb_request._cac import *


ecr                                                 = ElectronicConfirmationRequest()

ecr.RequestDate                                     = xs.date(2015, 1, 31)
ecr.RequestID                                       = '123456789'
ecr.HealthCareProviderID                            = 'ABC123'
ecr.HealthInsuranceOrganizationID                   = 'DEF456'
ecr.HealthCareProviderCvaddress                     = 'Health Care Provider Address'
ecr.HealthInsuranceOrganizationCvaddress            = 'Health Insurance Organization Address'

#Add company activity
CompanyActivity                                     = CompanyActivity()
CompanyActivity.ActivityCode                        = 'ActivityCode'
CompanyActivity.ActivityDescription                 = 'ActivityDescription'
ecr.CompanyActivity.append(CompanyActivity)

#Add requesting party
RequestingParty                                     = PartyType()
RequestingParty.EndpointID                          = 'Some EAN Location Number or GLN'
RequestingParty.PartyIdentification.append('Hospital identification')
RequestingParty.PartyName.extend(['Hospital name','Hospital alias'])
#adding a person to the party
RequestingPartyPerson                               = Person()
RequestingPartyPerson.FirstName                     = 'John'
RequestingPartyPerson.FamilyNmae                    = 'Smith'
RequestingPartyPerson.Title                         = 'Mr'
RequestingPartyPerson.JobTitle                      = 'Doctor'
RequestingParty.Person.append(RequestingPartyPerson)
#adding postal address to the party
RequestingPartyPostalAddress                        = PostalAddress()
RequestingPartyPostalAddress.StreetName             = 'Strada 9 Mai'
RequestingPartyPostalAddress.CityName               = 'Bucharest'
RequestingPartyPostalAddress.PostalZone             = '063122'
RequestingPartyCountry                              = Country()
RequestingPartyCountry.IdentificationCode           = 'RO'
RequestingPartyCountry.Name                         = 'Romania'
RequestingPartyPostalAddress.Country                = RequestingPartyCountry
RequestingParty.PostalAddress                       = RequestingPartyPostalAddress


#Add Cvbusiness 
Cvbusiness                                          = Cvbusiness()
Cvbusiness.LegalID                                  = 'RO23763654'
# Cvbusiness.LegalName.append('Company Name')
# CvbusinessBusinessAddress                           = 'Adress'
# CvbusinessBusinessAddress.StreetName                = 'Maresal Averescu'
# CvbusinessBusinessAddress.CityName                  = 'Bucharest'
# CvbusinessBusinessAddress.PostalZone                = '063122'
# CvbusinessBusinessAddressCountry                    = Country()
# CvbusinessBusinessAddressCountry.IdentificationCode = 'RO'
# CvbusinessBusinessAddressCountry.Name               = 'Romania'
# CvbusinessBusinessAddress.Country                   = CvbusinessBusinessAddressCountry
# Cvbusiness.BusinessAddress                          = CvbusinessBusinessAddress
RequestingParty.Cvbusiness                          = Cvbusiness


ecr.RequestingParty                                 = RequestingParty

print(ecr.toxml("utf-8"))