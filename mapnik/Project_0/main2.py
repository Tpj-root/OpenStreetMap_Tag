import mapnik

# Create a map object
m = mapnik.Map(8000, 6000)

# Set the background color of the map
m.background = mapnik.Color('steelblue')

# Create a style for the map
s = mapnik.Style()
r = mapnik.Rule()

# Create a polygon symbolizer to fill the land with a color
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)

# Create a line symbolizer to draw the borders
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.stroke_width = 0.1
r.symbols.append(line_symbolizer)

# Add the rule to the style
s.rules.append(r)

# Add the style to the map
m.append_style('My Style', s)

# Create a layer and add it to the map
layer = mapnik.Layer('world')
layer.datasource = mapnik.Shapefile(file='ne_10m_admin_0_countries.shp')
layer.styles.append('My Style')
m.layers.append(layer)

# Zoom to the extent of the layer
m.zoom_all()

# Render the map to an image file
mapnik.render_to_file(m, 'world_map.png', 'png')

print("Map rendered to 'world_map.png'")
