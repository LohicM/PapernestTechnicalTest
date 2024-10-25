from fastapi import FastAPI
import pyproj
import requests
import pandas

app = FastAPI()

df = pandas.read_csv("./csv/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv", delimiter=";")

@app.get("/")
def search_coverage(q = None):
    
    GPS = get_GPS_coordinates(q)
    lambert = convert_GPS_to_lambert(GPS)
    operator_infos = get_operator_infos(lambert)
    
    return operator_infos
    
    
def get_GPS_coordinates(q):
    geocode = requests.get(f"https://api-adresse.data.gouv.fr/search/?q={q}")
    if geocode.status_code == 200:
        data = geocode.json()
        if data['features']:
            coords = data['features'][0]['geometry']['coordinates']
            return coords[0], coords[1]
    return None, None


def convert_GPS_to_lambert(GPS):
    lambert = pyproj.Proj('+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
    wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
    lambert = pyproj.transform(wgs84, lambert, GPS[0], GPS[1])
    return lambert


def get_operator_infos(lambert):
    tolerance = 1000
    x, y = lambert

    result = df[(df['x'].between(x - tolerance, x + tolerance)) &
                (df['y'].between(y - tolerance, y + tolerance))]

    operator_dict = {
        20801: "orange",
        20810: "SFR",
        20815: "Free",
        20820: "Bouygues"
    }

    coverage_info = {}

    for _, row in result.iterrows():
        operator_name = operator_dict.get(row['Operateur'])
        if operator_name:
            coverage = {"2G": bool(row['2G']), "3G": bool(row['3G']), "4G": bool(row['4G'])}
            if any(coverage.values()):
                coverage_info[operator_name] = coverage
    
    return coverage_info