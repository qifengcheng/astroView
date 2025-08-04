AstroView
AstroView is a Python toolkit for high-precision astronomy calculations, focused on asteroid positions and orbit visualization. With AstroView, you can compute where an asteroid is in the sky at any given time (using data accurate to within milliarcseconds, find out its distance from Earth, and even plot its orbital path in 3D. 

The toolkit leverages the powerful Skyfield library for its astronomy calculations, ensuring that results match official ephemerides to very high precision. AstroView is designed to be easy to use in interactive environments like Jupyter notebooks, making it a handy tool for astronomers, educators, and hobbyists interested in exploring asteroid orbits.

##Features##
- High-Precision Ephemeris Calculations: Compute an asteroid’s position (RA/Dec or Cartesian coordinates) at any time, using JPL/NASA-grade ephemeris data for accuracy AstroView wraps the Skyfield library, so it handles all the complex astronomy math under the hood.

- Horizontal Coordinates (Alt/Az): Easily convert an asteroid’s position to your local sky coordinates. Given an observing location (latitude, longitude, elevation), AstroView will tell you the object’s altitude and azimuth, i.e. where to look in the sky.

- Orbit Visualization: Plot the orbit of an asteroid in 3D. You can generate a plot of the asteroid’s orbital ellipse around the Sun, and see the relative positions of the asteroid and Earth. This helps in visualizing the object’s path and how close it comes to Earth or other planets.
Observer’s Locations Database Includes a built-in list of famous observatories and observing sites. You can specify your location by name (for example, "Mauna Kea", "Palomar Observatory", "Greenwich", etc.) and AstroView will know the coordinates. No need to look up latitude/longitude for common sites.
- Extensible Design: While the initial focus is on asteroids, the framework is laid out to potentially support other celestial bodies. Future versions may incorporate satellite tracking (using TLE data) or comets, using the same easy interface.

##Installation##
AstroView is a Python package available via pip. To install the latest version, use:
