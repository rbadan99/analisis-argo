# analisis_argo.py

import pandas as pd

G = 9.8

def cargar_datos(ruta: str) -> pd.DataFrame:
    """
    Carga un archivo CSV en un DataFrame de Pandas.

    :param ruta: Ruta al archivo CSV.
    :return: DataFrame con los datos cargados.
    """
    df = pd.read_csv(ruta)
    return df


def explorar_datos(df: pd.DataFrame) -> None:
    """
    Muestra información básica del DataFrame:
    número de filas, columnas y valores nulos por columna.

    :param df: DataFrame a explorar.
    """
    print("Dimensiones del dataset:")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}\n")

    print("Valores nulos por columna:")
    print(df.isnull().sum())
    print()


def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina filas con valores nulos en temperature o salinity.

    :param df: DataFrame original.
    :return: DataFrame limpio.
    """
    df_limpio = df.dropna(subset=["temperature", "salinity", "depth"])
    return df_limpio


def crear_columna_superficie(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea una nueva columna 'is_surface' que indica si la profundidad
    es menor a 50 metros.

    :param df: DataFrame.
    :return: DataFrame con la nueva columna.
    """
    df["is_surface"] = df["depth"] < 50
    return df


def calcular_medias_por_cuenca(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula la temperatura media y salinidad media agrupadas por cuenca.

    :param df: DataFrame limpio.
    :return: DataFrame con estadísticas por cuenca.
    """
    resumen = df.groupby("basin")[["temperature", "salinity"]].mean()
    return resumen


def guardar_datos(df: pd.DataFrame, ruta: str) -> None:
    """
    Guarda el DataFrame en un archivo CSV.

    :param df: DataFrame a guardar.
    :param ruta: Ruta del archivo de salida.
    """
    df.to_csv(ruta, index=False)
    print(f"Archivo guardado en: {ruta}")


if __name__ == "__main__":
    # 1. Cargar datos
    ruta_entrada = "data/argo_mediterraneo.csv"
    df = cargar_datos(ruta_entrada)

    # 2. Explorar datos
    explorar_datos(df)

    # 3. Limpiar datos
    df = limpiar_datos(df)

    # 4. Crear columna de superficie
    df = crear_columna_superficie(df)

    # 5. Calcular medias por cuenca
    resumen = calcular_medias_por_cuenca(df)
    print("Medias por cuenca:")
    print(resumen)
    print()

    # 6. Guardar datos limpios
    ruta_salida = "data/argo_limpio.csv"
    guardar_datos(df, ruta_salida)
