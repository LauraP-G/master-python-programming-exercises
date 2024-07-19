def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    horas_a_segundos_primer=hr1 * 3600
    horas_a_segundor_segun=hr2 * 3600
    minutos_a_segundos_primer = min1 * 60
    minutos_a_segundos_segun = min2 * 60
    suma_primer= horas_a_segundos_primer+minutos_a_segundos_primer +sec1
    suma_segun = horas_a_segundor_segun+minutos_a_segundos_segun +sec2
    return suma_segun - suma_primer  



    # Your code here   
    return None


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,1,1,2,2,2))
