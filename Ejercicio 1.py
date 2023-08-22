def calcula_promedio():    
    sum = 0  
    for i in range(1, 12): 
        if i <= 6:
            sum = sum + 300
        elif 7 <= i < 10:  
            sum = sum + 500
        else:
            sum = sum + 700
                    
    prom = sum // 12
    return prom
    
def sueldo():    
    promedio = calcula_promedio()  
    if promedio < 300:
        return "Sueldo bajo"
    elif 300 <= promedio <= 900:  
        return "Sueldo medio"
    else:
        return "Sueldo mejor de lo normal"  

print(sueldo())