
**mapnik_build**

```
https://mapnik.org/pages/downloads.html


git clone https://github.com/mapnik/mapnik.git
cd mapnik
git checkout v4.0.5
git submodule update --init
python3 ./scons/scons.py configure
python3 ./scons/scons.py install -j4


Mapnik for a Static Build
python3 ./scons/scons.py configure STATIC_LIBS=1
python3 ./scons/scons.py -j$(nproc)

python3 ./scons/scons.py -j2



```


```
cat /usr/include/boost/version.hpp | grep "BOOST_LIB_VERSION"
#define BOOST_LIB_VERSION "1_74"
dpkg -s libboost-dev | grep Version
apt list --installed | grep boost
```





**You need to modify SConstruct directly**
```
nano SConstruct


#line : 46

Change -std=c++20 to -std=c++17

#line : 46

Change  BOOST_MIN_VERSION = '1.83' to 1.74



```




```
sudo apt install -y libproj-dev libwebp-dev libtiff-dev libgdal-dev libsqlite3-dev libpq-dev
export PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
python3 ./scons/scons.py configure STATIC_LIBS=1

```



 Enable Testing Repo Temporarily


 ```
 sudo nano /etc/apt/sources.list
deb http://deb.debian.org/debian testing main
sudo apt update
sudo apt install -t testing libharfbuzz-dev libproj-dev


try build own
https://github.com/harfbuzz/harfbuzz
https://github.com/OSGeo/PROJ.git

```



```

Without HarfBuzz 8.3.0+, you can't use advanced OpenType features like:

    Ligatures (e.g., "fi" turning into a single glyph)
    Stylistic alternates (different character shapes)
    Kerning (fine-tuned spacing between letters)
    Variable fonts (adjustable weight, width, etc.)

Basic text rendering will still work, but some font features might not render as expected.







```

c++
 -o src/projection.os
 -c 

-std=c++17 
-DU_USING_ICU_NAMESPACE=0 
-fvisibility=hidden
 -fvisibility-inlines-hidden
 -Wall
 -pthread
 -ftemplate-depth-300
 -Wsign-compare
 -O3
 -fPIC
 -DMAPNIK_MEMORY_MAPPED_FILE
 -DMAPNIK_HAS_DLCFN
 -DBIGINT
 -DBOOST_REGEX_HAS_ICU
 -DHAVE_JPEG
 -DHAVE_PNG
 -DHAVE_WEBP
 -DHAVE_TIFF
 -DLINUX
 -DMAPNIK_THREADSAFE
 -DBOOST_SPIRIT_NO_PREDEFINED_TERMINALS=1
 -DBOOST_PHOENIX_NO_PREDEFINED_TERMINALS=1
 -DBOOST_SPIRIT_USE_PHOENIX_V3=1
 -DNDEBUG
 -DHAVE_CAIRO
 -DGRID_RENDERER
 -Ideps
 -Ideps/mapbox/polylabel/include
 -Ideps/mapbox/protozero/include
 -Ideps/mapbox/geometry/include
 -Ideps/mapbox/variant/include
 -Ideps/agg/include
 -Iinclude
 -I/usr/include
 -I/usr/include/freetype2
 -I/usr/include/libpng16
 -I/usr/include/gdal
 -I/usr/include/postgresql
 -I/usr/include/cairo
 -I/usr/include/glib-2.0
 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include
 -I/usr/include/pixman-1
 -I/usr/include/uuid src/projection.cpp
 

```


