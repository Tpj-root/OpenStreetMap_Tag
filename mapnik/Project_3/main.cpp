#include <mapnik/map.hpp>
#include <mapnik/layer.hpp>
#include <mapnik/rule.hpp>
#include <mapnik/feature_type_style.hpp>
#include <mapnik/datasource_cache.hpp>
#include <mapnik/agg_renderer.hpp>
#include <mapnik/load_map.hpp>
#include <mapnik/image.hpp>
#include <mapnik/image_util.hpp>
#include <mapnik/symbolizer.hpp>
#include <mapnik/color.hpp>
#include <mapnik/expression.hpp> // Include for parse_expression
#include <iostream>

int main() {
    // Create a map object
    mapnik::Map map(800, 600);

    // Register datasources
    mapnik::datasource_cache::instance().register_datasources("/usr/lib/mapnik/3.1/input");

    // Create a layer
    mapnik::layer lyr("countries");
    mapnik::parameters params;
    params["type"] = "shape";
    params["file"] = "ne_10m_admin_0_countries.shp";
    lyr.set_datasource(mapnik::datasource_cache::instance().create(params));

    // Create a style and rule
    mapnik::feature_type_style style;
    mapnik::rule rule;

    // Create a filter expression
    mapnik::expression_ptr filter = mapnik::parse_expression("[NAME] = 'Canada'");
    rule.set_filter(filter); // Set the filter

    // Create a polygon symbolizer and set its fill color
    mapnik::polygon_symbolizer poly_sym;
    mapnik::put(poly_sym, mapnik::keys::fill, mapnik::color("blue"));
    rule.append(poly_sym);

    // Add the rule to the style
    style.add_rule(std::move(rule));

    // Add the style to the map
    map.insert_style("countries_style", style);

    // Add the layer to the map
    map.add_layer(lyr);

    // Set the map's background color
    map.set_background(mapnik::color("white"));

    // Zoom to the extent of the layer
    map.zoom_all();

    // Render the map to an image
    mapnik::image_rgba8 image(map.width(), map.height());
    mapnik::agg_renderer<mapnik::image_rgba8> renderer(map, image);
    renderer.apply();

    // Save the image to a file
    mapnik::save_to_file(image, "output.png");

    std::cout << "Map rendered to output.png" << std::endl;

    return 0;
}