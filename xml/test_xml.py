import  xml.dom.minidom
impl  =  xml.dom.minidom.getDOMImplementation()
dom  =  impl.createDocument(None,  ' employees ' , None)
root  =  dom.documentElement  
employee  =  dom.createElement( ' employee ' )
employee.setAttribute('id', '12')
root.appendChild(employee)
  
nameE = dom.createElement( ' name ' )
nameT = dom.createTextNode( ' linux ' )
nameE.appendChild(nameT)
employee.appendChild(nameE)
  
ageE = dom.createElement( ' age ' )
ageT = dom.createTextNode( ' 30 ' )
ageE.appendChild(ageT)
employee.appendChild(ageE)
  

f =  open( ' employees2.xml ' ,  'w') #  , encoding = 'utf-8' )
dom.writexml(f,  addindent = '    ' , newl = '\n' ,encoding = 'utf-8' )
f.close()
