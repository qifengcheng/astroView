# ⭐️ AstroView

**AstroView** is a Python toolkit for **high-precision asteroid ephemerides** and **orbit visualisation**.  
Powered by the outstanding [**Skyfield**](https://rhodesmill.org/skyfield/) library, AstroView matches official almanac data to within **0.0005 arcsec** accuracy while giving you an intuitive, notebook-friendly API.

## ✨ Features

- **Accurate ephemerides**
  - Asteroid positions (RA/Dec, Cartesian) at any time
  - Distances and 3-D separation vectors (e.g. asteroid ↔ Earth)
- **Horizontal coordinates**
  - Instant conversion to **altitude / azimuth** for any observing site
- **3-D orbit plots**
  - Matplotlib-based orbit viewer with Sun & Earth for context
- **Built-in observatory database**
  - Call sites by name (e.g. **"Mauna Kea"**, **"Paranal"**)
- **Extensible design**
  - Framework ready for satellites, comets, or planets in future versions
 
## Future work

- In future updates, we plan to add **satellite tracking**, so you could get orbits of Earth satellites by providing TLE (two-line element) data.
- We also plan to integrate **comet support** (using similar orbital elements approach as asteroids) and possibly connections to the JPL Horizons API for direct queries of any small-body.
- Additional visualization tools, such as generating sky charts or animations of orbits, are on the roadmap.

## 📦 Installation

```bash
pip install astroview



