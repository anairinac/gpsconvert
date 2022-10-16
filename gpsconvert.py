
# Convert to Adobe Bridge GPS format: dd,mm.mmmm

# Example input: 9.905094602309601, -84.1772327028534

def getHemisphere( coordinate , degrees ):
    match coordinate:
        case "latitude":
            if degrees >= 0:
                return "N" # Positive latitude means North
            else: 
                return "S" # Negative latitude means South
        case "longitude":
            if degrees >= 0:
                return "E" # Positive longitude means East
            else: 
                return "W" # Negative longitude means West

def main():

    print("Enter your latitude: ")
    dd_latitude = float( input())
    print("Enter your longitude: ")
    dd_longitude = float( input())

    # Latitude calculations
    lat_degrees = int( dd_latitude )
    lat_minutes = ( dd_latitude%1 )*60
    lat_hemisphere = getHemisphere( "latitude" , dd_latitude )

    ddm_latitude = "{},{:.4f}{}".format( lat_degrees, lat_minutes, lat_hemisphere )

    # Longitude calculations
    long_degrees = int( abs( dd_longitude ))
    long_minutes = ( abs( dd_longitude )%1 )*60
    long_hemisphere = getHemisphere( "longitude" , dd_longitude )

    ddm_longitude = "{},{:.4f}{}".format( long_degrees, long_minutes, long_hemisphere )

    print("\nGoogle Maps Coordinates:\n")
    print("Latitude: {}\nLongitude: {}\n".format( dd_latitude , dd_longitude ))
    print("Adobe Bridge (DDM) Coordinates:\n")
    print("Latitude: {}\nLongitude: {}\n".format( ddm_latitude , ddm_longitude ))

if __name__ == "__main__":
    main()