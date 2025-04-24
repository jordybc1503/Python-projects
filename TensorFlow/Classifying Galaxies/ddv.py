grupo1 = {
    "idregistro", "identidad", "apellidopaterno", "apellidomaterno", "nombre", "dni", "fechanacimiento", "telefono", "celular", "email", "zona", "via", "numero", "referencia", "Ubicación de la dirección que figura en su DNI", "Departamento3", "Provincia4", "Distrito5", "7. Nacionalidad", "Especifique Otra Nacionalidad6", "8. Sexo", "9. Estado civil", "Especifique Otro estado Civil7", "11. Edad en años cumplidos", "12. Lugar de nacimiento", "Departamento8", "Provincia9", "Distrito10", "13. Dirección actual de residencia, ¿es la misma que se detalla en su DNI?", "14. Dirección actual de residencia - Tipo de Vía:", "Especificar Otro tipo de vía", "15. Nombre de la vía", "16. Referencia", "17. Ubicación de su dirección actual", "Departamento11", "Provincia12", "Distrito13", "En relación a ${nombre_pcd}:", "1. ¿Tiene el certificado por discapacidad?", "2. ¿Se encuentra registrado en el CONADIS (Consejo Nacional para la Integración de las Personas con Discapacidad)?", "2.1. ¿Conoce o tiene a la mano su número RUI de CONADIS?", "Registre el número RUI (CONADIS)", "3. ¿Por qué no ha realizado el trámite aún?", "Especifique Otros motivos por los que no se ha realizado el trámite", "4. Grado de instrucción", "5. Grado académico", "6. ¿Pertenece a alguna asociación vinculada a PcD?", "Seleccione la asociación a la que pertenece", "Especificar Otra Asociación a la que pertenece", "7. ¿Con qué frecuencia se reúnen?", "8. Tipo de vivienda", "Especifique Otro tipo de vivienda", "Número de piso", "¿Cuenta con ascensor?", "idsexo", "idestadocivil", "idtipodocumentoregistro", "otrotipodocumentoregistro", "idtipozona", "idtipovia", "otravia", "idcentropoblado", "idlugarresidencia", "idlugarnacimiento", "idnacionalidad", "idtipoentidad"
}

grupo2 = {
    "idregistro", "identidad", "apellidopaterno", "apellidomaterno", "nombre", "dni", "fechanacimiento", "telefono", "celular", "email", "zona", "via", "numero", "referencia", "latitud", "longitud", "idsexo", "idestadocivil", "idtipodocumentoregistro", "otrotipodocumentoregistro", "idtipozona", "otrazona", "idtipovia", "otravia", "idcentropoblado", "idlugarresidencia", "idlugarnacimiento", "idnacionalidad", "idtipoentidad"
}

diferencia = grupo1.difference(grupo2)

# Guardar en un archivo de texto
with open('diferencia.txt', 'w') as archivo:
    for palabra in diferencia:
        archivo.write('"' + palabra + '", ')

print(diferencia)