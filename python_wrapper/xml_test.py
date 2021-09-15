from xml.etree.ElementTree import Element, SubElement, Comment, tostring


xmlRequest=Element('s:Envelope',{'xmlns:s':'https://schemas.xmlsoap.org/soap/envelope/'})
header=SubElement(xmlRequest,'s:Header')
#This will print "b'<s:Envelope><s:Header /></s:Envelope>'"
print(tostring(xmlRequest))


