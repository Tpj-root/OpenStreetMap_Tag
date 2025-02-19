# OpenStreetMap_Tag
OpenStreetMap (OSM)


Sample_site
https://tpj-root.github.io/OpenStreetMap_Tag/






```
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
<script>

...
.. input code
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

Hexagon


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



Update info

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




Updated Code for Smooth Movement
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





Public_data


https://www.openstreetmap.org/traces
