import mapnik

# Create a map object with high resolution (e.g., 1920x1080)
m = mapnik.Map(1920, 1080)
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

#layer.datasource = mapnik.Shapefile(file='ne_10m_admin_0_countries_ind.shp')
layer.datasource = mapnik.Shapefile(file='india_shapefile.shp')
layer.styles.append('My Style')
m.layers.append(layer)

# Zoom to the extent of the layer
m.zoom_all()

# Render the map to a high-resolution image file
mapnik.render_to_file(m, 'india_map_high_res_2.png', 'png')

print("High-resolution India map rendered to 'india_map_high_res.png'")
