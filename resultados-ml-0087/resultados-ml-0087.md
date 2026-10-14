# Reporte de Análisis de Datos - Pandas

`Alonso Lopez Garcia Machine Learning pandas, NC 0087`

## 1. DataFrame Convertido
```text
       Juego Plataforma  Precio
0      Mario   Nintendo    1200
1      Zelda   Nintendo    1300
2       FIFA      Multi    1000
3  Minecraft      Multi     300
4   Fortnite      Multi       0
5        GTA      Multi       0
```

## 2.1 Primeras Filas (head)
```text
   Juego Plataforma  Precio
0  Mario   Nintendo    1200
1  Zelda   Nintendo    1300
```

## 2.2 Últimas Filas (tail)
```text
      Juego Plataforma  Precio
4  Fortnite      Multi       0
5       GTA      Multi       0
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Juego           str
Plataforma      str
Precio        int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Juego       6 non-null      str  
 1   Plataforma  6 non-null      str  
 2   Precio      6 non-null      int64
dtypes: int64(1), str(2)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Precio'
```text
count       6.000000
mean      633.333333
std       602.218122
min         0.000000
25%        75.000000
50%       650.000000
75%      1150.000000
max      1300.000000
Name: Precio, dtype: float64
```

## 4. Ordenar Ascendente por Precio
```text
       Juego Plataforma  Precio
5        GTA      Multi       0
4   Fortnite      Multi       0
3  Minecraft      Multi     300
2       FIFA      Multi    1000
0      Mario   Nintendo    1200
1      Zelda   Nintendo    1300
```

## 5. Ordenar Descendente por Precio
```text
       Juego Plataforma  Precio
1      Zelda   Nintendo    1300
0      Mario   Nintendo    1200
2       FIFA      Multi    1000
3  Minecraft      Multi     300
4   Fortnite      Multi       0
5        GTA      Multi       0
```

`Alonso Lopez Garcia Machine Learning pandas, NC 0087`