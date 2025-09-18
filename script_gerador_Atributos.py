from qgis.core import QgsProject, QgsField, QgsFieldConstraints
from PyQt5.QtCore import QVariant

layer = iface.activeLayer()

if not layer:
    raise Exception("❌ Nenhuma camada ativa. Selecione um shapefile primeiro.")

# Iniciar edição
if not layer.startEditing():
    raise Exception("❌ Não foi possível iniciar a edição da camada.")

provider = layer.dataProvider()
provider.deleteAttributes([i for i in range(len(layer.fields()))])
layer.updateFields()

new_fields = {
    'MATRICULA': QVariant.String,
    'DAT_MAT': QVariant.String,
    'LIV_MAT': QVariant.Int,
    'FOL_MAT': QVariant.Int,
    'TRANSCRI': QVariant.String,
    'CNM': QVariant.String,
    'CNS': QVariant.String,
    'ENDERECO': QVariant.String,
    'NUMERO': QVariant.String,
    'CEP': QVariant.Int,
    'MUNICIPIO': QVariant.String,
    'UF': QVariant.String,
    'NOME_TIT': QVariant.String,
    'CPF_CNPJ': QVariant.String,
    'REL_JUR': QVariant.String,
    'DAT_INI': QVariant.String,
    'DAT_FIM': QVariant.String,
    'PER_REL': QVariant.Double,
    'NOME_IMO': QVariant.String,
    'AREA_HA': QVariant.Double,
    'AREA_M2': QVariant.Double,
    'PER_M': QVariant.Double,
    'PER_KM': QVariant.Double,
    'CONF_MAT': QVariant.String,
    'CONF_NOME': QVariant.String,
    'CCIR_SNCR': QVariant.String,
    'SIGEF': QVariant.String,
    'SNCI': QVariant.String,
    'CIB_NIRF': QVariant.String,
    'ITBI': QVariant.Double,
    'CAR': QVariant.String,
    'RIP': QVariant.Int,
    'CIF': QVariant.Int
}

fields_to_add = []
for name, ftype in new_fields.items():
    if ftype == QVariant.Double:
        # define double com 2 casas decimais (prec=2) e até 10 dígitos totais (len=10)
        fields_to_add.append(QgsField(name[:10], ftype, len=10, prec=2))
    elif ftype == QVariant.Int:
        # Inteiro com até 20 dígitos
        fields_to_add.append(QgsField(name[:10], ftype, len=20))
    else:
        fields_to_add.append(QgsField(name[:10], ftype))

provider.addAttributes(fields_to_add)
layer.updateFields()

if not layer.commitChanges():
    raise Exception("❌ Falha ao salvar alterações.")

print("✅ Campos adicionados com sucesso.")
