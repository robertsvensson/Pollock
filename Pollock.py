import requests

### DEFINE FUNCTIONS
# Get geo data on all the ip address
def getGeoInfo(ipAddress):
    r = requests.get('http://ip-api.com/json/'+ipAddress)
    geoData = r.json()
    return geoData

# Iterate the data and grab the things we need
def filterGeoData(geoData):
    lon =''
    lat =''
    ipAddress =''
    country =''
    city =''
    isp =''
#   print geoData
    for key,value in geoData.iteritems():
        if key == 'lon':
            lon = value
        if key == 'lat':
            lat = value
        if key == 'query':
            ipAddress = value
        if key == 'country':
            country = value
        if key == 'city':
            city = value
        if key == 'isp':
            isp = value


    return lon, lat, ipAddress, country, city, isp


###
# Open file of IP addresses from ip.txt in the local directory

try:
    fh = open('ip.txt','r')
except IOError as e:
    print e
    raise


for x in fh:
    x = x.rstrip()

    # Send the IP addresses to the API at ip-api.com to get a JSON object back
    geoData = getGeoInfo(x)

    # Parse the JSON object to grab only what we need
    lon, lat, ipAddress, country, city, isp = filterGeoData(geoData)

    # ...and print the results
    print ' IP Address: '+str(ipAddress)+'\t Country: '+str(country)+'\t City: '+str(city)+'\t Lon: '+str(lon)+'\t Lat: '+str(lat)+'\t ISP: '+str(isp)
