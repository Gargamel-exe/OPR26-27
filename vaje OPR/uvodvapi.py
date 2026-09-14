#slovarji (dictionary)

slovar = {"ključ" : "vrednost",
          "ključ2" : "vrednost2"}

print(slovar)
print(slovar["ključ"])  #dobimo vrednost od ključa

print("----------------")

# raznoliki slovar
razno = {"število" : 6,
         "ime" : "Rožle",
         "seznam" : [1,2,3,4],
         "slovar" : {"firma": "Audi", "moč" : "120konjev"}}

print(razno["število"]  + 10)
print(max (razno["seznam"])) 

print(razno["slovar"]) #{'firma': 'Audi', 'moč': '120konjev'}

print(razno["slovar"]["firma"]) #Izpiše  vrednost ključa "firma"
print(razno["slovar"]["moč"]) #Izpiše  vrednost ključa "firma"

#Open Meteo API
import requests
base_url = "https://api.open-meteo.com/v1/forecast?latitude=46.3686&longitude=14.1165&daily=rain_sum&forecast_days=1"

klic = requests.get(base_url).json()

#print(klic) #mora biti med 200 in 300 da se zagotovimo da stvar deluje pravilo

print(klic["daily"]["rain_sum"][0])
