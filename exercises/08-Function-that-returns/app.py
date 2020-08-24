def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

####### ↓ YOUR CODE BELOW ↓ #######

def cambio(dolar):
    euro = dollar_to_euro(dolar)
    return euro_to_yen(euro)
    
print(cambio(137))    

euro = dollar_to_euro(137)
yen = euro_to_yen(euro)

print(yen)