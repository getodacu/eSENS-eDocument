#!/bin/bash
xbdir=xb_request
xbmodule=econfirmation

rm -fr $xbdir && mkdir $xbdir
cd $xbdir && touch __init__.py
pyxbgen -u ../xsd/request/ElectronicConfirmationRequest.xsd -m $xbmodule
mv _ccts-cct.py _ccts_cct.py
sed s/\_ccts\-cct/\_ccts\_cct/g _udt.py  > _udt_temp
mv -f _udt_temp _udt.py
