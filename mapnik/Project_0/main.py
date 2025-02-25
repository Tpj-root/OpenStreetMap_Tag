import mapnik

# Create a Map object
m = mapnik.Map(800, 600)
m.background = mapnik.Color('lightblue')

# Create a Style
style = mapnik.Style()
rule = mapnik.Rule()
point_symbolizer = mapnik.PointSymbolizer()
rule.symbols.append(point_symbolizer)
style.rules.append(rule)
m.append_style('PointStyle', style)

# Create a Layer
layer = mapnik.Layer('Points')
layer.datasource = mapnik.MemoryDatasource()
layer.styles.append('PointStyle')

# Create a Point Feature
ctx = mapnik.Context()
feature = mapnik.Feature(ctx, 1)
feature['name'] = 'Delhi'
feature.geometry = mapnik.Geometry.from_wkt("POINT(77.1025 28.7041)")  # Delhi coordinates
layer.datasource.add_feature(feature)

# Add the layer to the map
m.layers.append(layer)

# Zoom to the extent and render the map
m.zoom_all()
mapnik.render_to_file(m, 'map.png', 'png')

print("Map rendered to map.png")

