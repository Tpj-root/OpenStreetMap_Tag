import mapnik

# Create a map object
m = mapnik.Map(800, 600)
m.background = mapnik.Color('steelblue')  # Set background color

# Create a style for the map (for the country polygons)
s = mapnik.Style()
r = mapnik.Rule()

# Polygon symbolizer for filling the country
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')  # Light gray color for land
r.symbols.append(polygon_symbolizer)

# Line symbolizer for borders
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')  # Gray color for borders
line_symbolizer.stroke_width = 0.5
r.symbols.append(line_symbolizer)

# Add the rule to the style
s.rules.append(r)

# Add the style to the map
m.append_style('My Style', s)

# Create a layer for the India map
layer = mapnik.Layer('India')
#layer.datasource = mapnik.Shapefile(file='/home/cnc/Downloads/ne_10m_admin_0_countries_ind/ne_10m_admin_0_countries_ind.shp')
layer.datasource = mapnik.Shapefile(file='ne_10m_admin_0_countries_ind.shp')
layer.styles.append('My Style')
m.layers.append(layer)

# Zoom to the extent of the layer
m.zoom_all()

# Add a marker at the specified coordinates (10.794599, 78.685107)
marker_style = mapnik.Style()
marker_rule = mapnik.Rule()

# Create a point symbolizer for the marker
point_symbolizer = mapnik.PointSymbolizer()
#point_symbolizer.file = 'path/to/marker.png'  # Path to your marker image
point_symbolizer.file = 'MapMarker_Ball_Right_Pink.png'  # Path to your marker image
point_symbolizer.allow_overlap = True
marker_rule.symbols.append(point_symbolizer)

# Add the rule to the marker style
marker_style.rules.append(marker_rule)

# Add the marker style to the map
m.append_style('Marker Style', marker_style)

# Create a layer for the marker
marker_layer = mapnik.Layer('Marker Layer')
marker_layer.datasource = mapnik.MemoryDatasource()

# Create a point geometry
point = mapnik.Geometry.from_wkt('POINT (10.794599 78.685107)')  # Create a point from WKT

# Create a feature and add the point geometry
feature = mapnik.Feature(mapnik.Context(), 1)
feature.geometry = point  # Add the point geometry to the feature
marker_layer.datasource.add_feature(feature)

# Add the marker layer to the map
marker_layer.styles.append('Marker Style')
m.layers.append(marker_layer)

# Render the map to an image file
mapnik.render_to_file(m, 'india_map_with_marker_1.png', 'png')

print("Map rendered to 'india_map_with_marker.png'")
