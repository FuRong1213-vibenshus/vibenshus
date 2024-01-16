import datetime 
def whenischristmas(dt):

    difference =  (datetime.datetime(2023, 12, 24) - dt).days
    if difference >= 1:
        thedayafter = dt + datetime.timedelta(days=1)
        
        whenischristmas(thedayafter)
        print(f"der er dagen efter {thedayafter.strftime('%d %b')},")
print("Hvornår er julen?")
whenischristmas(datetime.datetime.now())
