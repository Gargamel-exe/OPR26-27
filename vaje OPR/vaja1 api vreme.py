def temperatura():
    import requests
    base_url = "https://api.open-meteo.com/v1/forecast?latitude=46.3686&longitude=14.1165&daily=temperature_2m_max,temperature_2m_min&current=temperature_2m"

    klic = requests.get(base_url).json()
    print(klic)

    #Izpiši trenutno temperaturo.
    print(klic["current"]["temperature_2m"])
    #Izpiši temperature za naslednjih 7 dni.
    print(klic["daily"]["temperature_2m_max"])
    print(klic["daily"]["temperature_2m_min"])
    #Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.
    temperature = klic["daily"]["temperature_2m_max"]

    index_max = temperature.index(max(temperature))

    temperature = klic["daily"]["temperature_2m_max"]
    time = klic["daily"]["time"]

    index_max = temperature.index(max(temperature))
    print(max(klic["daily"]["temperature_2m_max"]))
    print(time[index_max])

    


    #print(max(klic["daily"]["temperature_2m_max"]))
    #print(min(klic["daily"]["temperature_2m_min"]))

    #Ugotovi, kateri dan ima največjo razliko med dnevno in nočno temperaturo.

if __name__ == "__main__":
    temperatura()
