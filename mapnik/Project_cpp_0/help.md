sudo apt install mapnik-utils libmapnik-dev python3-mapnik



Checking the Correct Path

find /usr -type d -name "input"


mapnik::datasource_cache::instance().register_datasources("/usr/lib/mapnik/3.1/input");

cnc@debian:/usr/lib/mapnik/3.1/input$ mapnik-config --input-plugins
/usr/lib/mapnik/3.1/input







wget https://download.geofabrik.de/asia/india-latest.osm.bz2
bunzip2 india-latest.osm.bz2  # Extract the OSM file




g++ -std=c++11 -I/usr/include/mapnik -o mapnik_test main.cpp \
    -L/usr/lib/mapnik -lmapnik -licuuc -licudata -licui18n -lfreetype -lpng



export MAPNIK_INPUT_PLUGINS=/usr/lib/mapnik/3.1/input



sudo apt update
sudo apt install osm2pgsql
sudo apt install osmctools
sudo apt install gdal-bin


mapnik-config --version

cnc@debian:~$ pkg-config --modversion icu-uc
72.1
cnc@debian:~$ 





g++ -std=c++11 -o render_map main.cpp $(mapnik-config --cflags --libs)




https://github.com/mapnik/mapnik/wiki/gettingstartedinpython



https://github.com/mapnik/mapnik/wiki/SQLite
https://github.com/mapnik/mapnik/wiki/ExampleCode



Server_side ** Best start

https://github.com/openstreetmap/mod_tile/
https://github.com/openstreetmap/tirex
https://www.lucadelu.org/



apt install libapache2-mod-tile renderd



------------



sudo apt install nodejs npm -y
npm install -g carto
