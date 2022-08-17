def get_horizon_data(nasaids, names, colors, sizes, start_date="2022-01-01"):
    from astropy.time import Time
    from astroquery.jplhorizons import Horizons
    from numpy import double

    data = {"info": "Database with the positions and speed of the planets on a specific day",
            "date": start_date}

    for i, nasaid in enumerate(nasaids):
        obj = Horizons(id=nasaid, location="@sun", epochs=Time(start_date).jd, id_type="id").vectors()
        print("-"*100)
        print(f"Downloading data for {names[i]}: ")
        print(obj)

        data[nasaid] = {
            "name": names[i],
            "size": sizes[i],
            "color": colors[i],
            "r": [double(obj[xi]) for xi in ["x", "y", "z"]],
            "v": [double(obj[vxi]) for vxi in ["vx", "vy", "vz"]]
        }
    return data
