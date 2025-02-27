#include <mapnik/map.hpp>
#include <mapnik/load_map.hpp>
#include <mapnik/image.hpp>
#include <mapnik/agg_renderer.hpp>
#include <mapnik/image_util.hpp>
#include <mapnik/datasource_cache.hpp>
#include <mapnik/font_engine_freetype.hpp>
#include <iostream>

int main() {
    try {
        // Initialize Mapnik
        mapnik::datasource_cache::instance().register_datasources("/usr/lib/mapnik/input");
        mapnik::freetype_engine::register_fonts("/usr/share/fonts", true);

        // Create a Map object
        mapnik::Map map(800, 600);
        
        // Load a Mapnik XML style file
        mapnik::load_map(map, "india.xml");

        // Zoom to map extent
        map.zoom_all();

        // Create an image to render the map
        mapnik::image_rgba8 image(800, 600);
        mapnik::agg_renderer<mapnik::image_rgba8> renderer(map, image);
        renderer.apply();

        // Save the rendered map
        mapnik::save_to_file(image, "output.png", "png");
        std::cout << "Map rendered successfully: output.png" << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
