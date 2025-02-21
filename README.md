# OpenStreetMap_Tag
OpenStreetMap (OSM)


**Sample_site**

https://tpj-root.github.io/OpenStreetMap_Tag/


```
https://github.com/mapnik/mapnik
https://github.com/Leaflet/Leaflet

```




API


```
getRoadName 
https://nominatim.openstreetmap.org/reverse?format=json&lat=10.803017&lon=78.687915

https://nominatim.openstreetmap.org/reverse?format=json&lat=10.802037&lon=78.691579

```


 

 ```
import requests

lat, lon = 47.6097, -122.3331  # Example coordinates (Seattle)
url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
data = response.json()

if "address" in data:
    print("Road Name:", data["address"].get("road", "Unknown"))


 ```



class   "amenity"
type    "hospital"

class   "highway"
type    "primary"


https://nominatim.openstreetmap.org/reverse?format=json&lat=10.802527&lon=78.691453&addressdetails=1




```
curl -X POST "http://overpass-api.de/api/interpreter" --data-urlencode 'data=
[out:json];
(
  node(around:1000,10.802527,78.691453);
  way(around:1000,10.802527,78.691453);
  relation(around:1000,10.802527,78.691453);
);
out center tags;
' >>OUTPUT.json


```





### To-Do List

- [ x ]      Start the project  
- [ x ]      Design an icon  
- [ x ]      Place the icon at the desired location  
- [ x ]      Add detailed information  
- [ x ]      Implement road trace colors  
- [ x ]      Overlay two colors for better visibility  
- [ x ]      Enable GPS location tracking with movement loop  
- [    ]       Add a login box  
- [    ]       Implement a chat box  
- [    ]       Create family tree tables  
- [    ]       Connect the database with MySQL  
- [    ]       Establish UDP port connection  
- [    ]       Test ping requests  
- [    ]       Test chat functionality with other users  



Explanation:

    HTML Structure:

        Added a sidebar div to hold the checkboxes.

        The map div is now flexed to take up the remaining space.

    CSS:

        The body is set to display: flex to split the screen horizontally.

        The sidebar has a fixed width and a background color.

        The map takes up the remaining space.

    JavaScript:

        Added event listeners to the checkboxes to toggle the visibility of the corresponding map elements.

        Each checkbox controls the visibility of its associated layers (markers, circles, rectangles, polygons, and polylines).


        









```
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
<script>

...
...input code
...

</script>

```




**Update icon url**



```

    var carIcon = L.icon({
        iconUrl: 'https://raw.githubusercontent.com/google/material-design-icons/refs/heads/master/src/alert/add_alert/materialicons/24px.svg',  // URL to car icon
        iconSize: [32, 32], // Size of the icon
        iconAnchor: [16, 32], // Bottom center anchor point
        popupAnchor: [0, -32] // Popup offset
    });

```



**Update the circle**


```
    // Add markers with custom icons and colored circles
    L.circle([10.803957, 78.686576], {
        color: 'blue',        // Border color
        fillColor: 'lightblue', // Fill color
        fillOpacity: 0.5,
        radius: 20 // Adjust size
    }).addTo(map);

    L.marker([10.803957, 78.686576], { icon: bikeIcon }).addTo(map)
        .bindPopup("<b>Bike Location</b><br>Name: SSSSYYY");
```


**Rectangle (or Square)**


 ```
L.rectangle([
    [10.774, 78.685],  // Bottom-left corner
    [10.776, 78.687]   // Top-right corner
], {
    color: "blue",
    fillColor: "lightblue",
    fillOpacity: 0.5
}).addTo(map);

```

**Pentagon**

```
L.polygon([
    [10.775, 78.686],
    [10.776, 78.687],
    [10.777, 78.6865],
    [10.7765, 78.6855],
    [10.7755, 78.685]
], {
    color: "green",
    fillColor: "lightgreen",
    fillOpacity: 0.5
}).addTo(map);


```

**Hexagon**

```
    L.polygon([
        [10.775, 78.686],
        [10.776, 78.687],
        [10.777, 78.6865],
        [10.777, 78.6855],
        [10.776, 78.685],
        [10.775, 78.6855]
    ], {
        color: "orange",
        fillColor: "yellow",
        fillOpacity: 0.5
    }).addTo(map);

    L.marker([10.775159, 78.686096], { icon: carIcon }).addTo(map)
        .bindPopup("<b>Car Location</b><br>Name: SAAAII");

```



**Update info**

```
L.marker([10.803957, 78.686576], { icon: bikeIcon }).addTo(map)
    .bindPopup(`
        <b>Bike Location</b><br>
        <b>Name:</b> SSSSYYY<br>
        <b>Sex:</b> Male/Female<br>
        <b>DOB:</b> YYYY-MM-DD<br>
        <b>School:</b> Your School Name<br>
        <b>College:</b> Your College Name<br>
        <b>Phone:</b> +91XXXXXXXXXX
    `);

```



A .gpx file is a GPS Exchange Format file used to store GPS data, such as waypoints, tracks, and routes. It is an XML-based format and can be opened with mapping software like Google Earth, Garmin BaseCamp, or even a simple text editor.



Head
```
<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<gpx version="1.1" creator="OsmAnd~ 4.1.11" xmlns="http://www.topografix.com/GPX/1/1" xmlns:osmand="https://osmand.net" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
```


```
   <metadata>
    <name>2025-02-19_10-17_Wed</name>
  </metadata>
  <trk>
    <trkseg>
      <trkpt lat="49.0703109" lon="11.8834506">
        <ele>445.1</ele>
        <time>2025-02-19T09:17:29Z</time>
        <hdop>3.8</hdop>
        <extensions>
          <osmand:speed>1.4</osmand:speed>
        </extensions>
      </trkpt>
 ```



point_1
```
      <trkpt lat="49.0703051" lon="11.8835398">
        <ele>441.4</ele>
        <time>2025-02-19T09:17:34Z</time>
        <hdop>3.8</hdop>
        <extensions>
          <osmand:speed>1.6</osmand:speed>
        </extensions>
      </trkpt>
```




Last_point
```
      <trkpt lat="49.0936015" lon="11.8104085">
        <ele>447</ele>
        <time>2025-02-19T11:45:16Z</time>
        <hdop>5.1</hdop>
      </trkpt>
      <trkpt lat="49.0935669" lon="11.8104052">
        <ele>447.8</ele>
        <time>2025-02-19T11:45:21Z</time>
        <hdop>4.5</hdop>
      </trkpt>
    </trkseg>
  </trk>
  <extensions>
    <osmand:show_arrows>false</osmand:show_arrows>
    <osmand:show_start_finish>true</osmand:show_start_finish>
    <osmand:split_interval>0.0</osmand:split_interval>
    <osmand:split_type>no_split</osmand:split_type>
    <osmand:smoothing_threshold>0.0</osmand:smoothing_threshold>
    <osmand:min_filter_speed>0.0</osmand:min_filter_speed>
    <osmand:max_filter_speed>0.0</osmand:max_filter_speed>
    <osmand:min_filter_altitude>0.0</osmand:min_filter_altitude>
    <osmand:max_filter_altitude>0.0</osmand:max_filter_altitude>
    <osmand:max_filter_hdop>0.0</osmand:max_filter_hdop>
  </extensions>
</gpx>

```


**Updated Code for Jumping Effect**


```
    // Define road coordinates (latitude, longitude)
    var roadCoordinates = [
        [10.809237, 78.695894],  // Start point
        [10.809063, 78.695304],  
        [10.808831, 78.694655],  
        [10.808810, 78.693717],  
        [10.808810, 78.693717],  
        [10.808805, 78.691061]   // Endpoint
    ];
    

    // Create the polyline (road)
    L.polyline(roadCoordinates, {
        color: 'red',
        weight: 5,
        opacity: 0.7
    }).addTo(map);
    
    // Define moving icon
    var User_0 = L.icon({
        iconUrl: 'https://raw.githubusercontent.com/google/material-design-icons/refs/heads/master/src/hardware/cast/materialicons/24px.svg',  
        iconSize: [32, 32],
        iconAnchor: [16, 32],
        popupAnchor: [0, -32]
    });
    
    // Add moving marker to the map
    var marker = L.marker(roadCoordinates[0], { icon: User_0 }).addTo(map);
    
    //  jumping effect
    // Function to move marker along the road
    function moveMarker(marker, coords, speed) {
        let index = 0;
        function animate() {
            if (index < coords.length) {
                marker.setLatLng(coords[index]);
                index++;
                setTimeout(animate, speed); // Adjust speed (milliseconds)
            }
        }
        animate();
    }
    // If You Want Smoother Movement:
    // Start moving the marker
    moveMarker(marker, roadCoordinates, 500);  // Moves every 500ms

```













**Updated Code for Smooth Movement**

```

function moveMarkerSmoothly(marker, coords, speed, steps) {
    let index = 0;
    
    function interpolate(lat1, lon1, lat2, lon2, factor) {
        return [
            lat1 + (lat2 - lat1) * factor,
            lon1 + (lon2 - lon1) * factor
        ];
    }

    function animate() {
        if (index < coords.length - 1) {
            let [lat1, lon1] = coords[index];
            let [lat2, lon2] = coords[index + 1];
            let step = 0;

            function stepMove() {
                if (step <= steps) {
                    let newPos = interpolate(lat1, lon1, lat2, lon2, step / steps);
                    marker.setLatLng(newPos);
                    step++;
                    setTimeout(stepMove, speed / steps);
                } else {
                    index++;
                    setTimeout(animate, speed); // Move to next point
                }
            }
            stepMove();
        }
    }
    animate();
}

// Start smoothly moving the marker
moveMarkerSmoothly(marker, roadCoordinates, 1000, 50);  // 1000ms per point, 50 small steps

```



**Updated Code (Loop 5 Times)**

```

function moveMarkerSmoothlyLoop(marker, coords, speed, steps, loopCount) {
    let index = 0;
    let count = 0;

    function interpolate(lat1, lon1, lat2, lon2, factor) {
        return [
            lat1 + (lat2 - lat1) * factor,
            lon1 + (lon2 - lon1) * factor
        ];
    }

    function animate() {
        if (index < coords.length - 1) {
            let [lat1, lon1] = coords[index];
            let [lat2, lon2] = coords[index + 1];
            let step = 0;

            function stepMove() {
                if (step <= steps) {
                    let newPos = interpolate(lat1, lon1, lat2, lon2, step / steps);
                    marker.setLatLng(newPos);
                    step++;
                    setTimeout(stepMove, speed / steps);
                } else {
                    index++;
                    setTimeout(animate, speed); // Move to next point
                }
            }
            stepMove();
        } else {
            count++; // Increment loop count
            if (count < loopCount) {
                index = 0; // Restart movement from the beginning
                setTimeout(animate, speed);
            }
        }
    }
    animate();
}

// Start moving smoothly with loop (5 times)
moveMarkerSmoothlyLoop(marker, roadCoordinates, 1000, 50, 5);



```

















**Public_data**

```
https://www.openstreetmap.org/traces
```