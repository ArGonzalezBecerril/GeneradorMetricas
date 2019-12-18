import pyspark as pspk
import pyspark.sql as pysql
import sys
import getopt
#import findspark

'''
@Autor: Arturo Gonzalez
@Email: arturo.gonzalez@tusventasdigitales.com 
@Nota:  Eliminar el metodo [conf_modulos] una vez se instalen los modulos ibis_framework

@Funcionamiento:  El script necesita 3 Argumentos
-i     : Id del proceso
-e     : Nombre del esquema
-t     : Nombre de la tabla

'''

esquema = ''
nom_tabla = ''

try:
    parametros, args = getopt.getopt(sys.argv[1:], "e:t:", ["esquema=", "tabla="])
    if len(parametros) < 2:
        print("Argumentos incompletos")
        sys.exit(1)
except getopt.GetoptError:
    print("Error en los argumentos")
    sys.exit(2)

for opt, arg in parametros:
    if opt in ("-e", "--esquema"):
        esquema = str(arg).strip()
    elif opt in ("-t", "--tabla"):
        nom_tabla = str(arg).strip()
    else:
        print("Parametro '" + opt + "' no reconocido")


# import EstadisticoDeFtes.fuente.etl.EtlEstadisticaImpala as Etl
# import EstadisticoDeFtes.fuente.util.LoggerImpl as Log


reload(sys)
sys.setdefaultencoding('utf-8')
# sys.excepthook = Log.trace_error

# findspark.init("/home/arturo/Software/spark-2.2.3-bin-hadoop2.7")
context = pspk.SparkContext.getOrCreate()
sql_context = pysql.SQLContext(context)
# dto_logger = Log.Logger('', '', 'Generador_de_insumos', '', '')


print("hola mundo")
print(esquema)
print(nom_tabla)

# etl_impala = Etl.EtlEstadisticaImpala(context, esquema, nom_tabla)
# etl_impala.extrae()
# etl_impala.transforma()

