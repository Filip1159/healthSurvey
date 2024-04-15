PREXIX = 'Jaką Pana/Pani zdaniem wartość '
INFIX = ' można uznać za '

categories = ['ciśnienia tętniczego', 'tętna', 'saturacji', 'GCS']
levels = ['niską', 'średnią', 'wysoką']
result = []

for category in categories:
    for level in levels:
        result.append(PREXIX + category + INFIX + level + '?')

print(result)

example = 'Jeśli ciśnienie jest niskie, tętno średnie, saturacja wysoka a GCS niskie, to jaki jest stan pacjenta?'

levels2 = ['niskie', 'średnie', 'wysokie']

for pressureLevel in levels2:
    for pulseLevel in levels2:
        for saturationLevel in levels2:
            for gcsLevel in levels2:
                result.append(f'Jeśli ciśnienie tętnicze jest {pressureLevel}, tętno {pulseLevel}, saturacja {saturationLevel}, a GCS {gcsLevel}, to jaki jest stan pacjenta?')

f = open("survey.txt", "w", encoding="UTF-8")
for row in result:
    f.write(row + '\n')
f.close()
