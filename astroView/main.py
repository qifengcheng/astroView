from skyfield.api import load, Loader
from astroquery.jplhorizons import Horizons
from astropy.time import Time
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt

class AsteroidVisualizer:
    def __init__(self):
        self.loader = Loader('./skyfield_data')
        self.eph = self.loader('de421.bsp')
        self.sun = self.eph['sun']
        self.earth = self.eph['earth']
        self.ts = self.loader.timescale()

    def get_heliocentric_position(self, target_name, dates_utc, id_type='smallbody'):
        jd_times = [self.ts.utc(*t).jd for t in dates_utc]
        obj = Horizons(id=target_name, location='500', epochs=jd_times, id_type=id_type)
        eph = obj.vectors()
        return eph['x'], eph['y'], eph['z']

    def visualize_orbit_3d(self, asteroid_name, start_year=2025):
        # Time range for 1 year
        days = self.ts.utc(start_year, 1, range(1, 366))

        # Earth's heliocentric orbit
        earth_pos = self.earth.at(days).observe(self.sun).apparent().position.au
        earth_x, earth_y, earth_z = -earth_pos[0], -earth_pos[1], -earth_pos[2]

        # Asteroid's heliocentric orbit
        jd_list = [t.utc_jpl() for t in days]
        x_ast, y_ast, z_ast = self.get_heliocentric_position(asteroid_name, [(t.utc.year, t.utc.month, t.utc.day) for t in days])

        fig = go.Figure()

        fig.add_trace(go.Scatter3d(x=earth_x, y=earth_y, z=earth_z, mode='lines', name='Earth Orbit'))
        fig.add_trace(go.Scatter3d(x=x_ast, y=y_ast, z=z_ast, mode='lines', name=f'{asteroid_name} Orbit'))
        fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0],
                                   mode='markers',
                                   marker=dict(size=6, color='yellow'),
                                   name='Sun'))

        fig.update_layout(
            scene=dict(
                xaxis_title='X (AU)',
                yaxis_title='Y (AU)',
                zaxis_title='Z (AU)',
                aspectmode='data'
            ),
            title=f'Orbit Around the Sun: Earth and {asteroid_name}',
            margin=dict(l=0, r=0, b=0, t=30)
        )

        fig.show()

    def visualize_skyview(self, objects, obs_code='500', obs_time_utc='2025-08-05 10:00'):
        t_astropy = Time(obs_time_utc)
        epoch_jd = t_astropy.jd

        positions = {}
        for obj in objects:
            horizons_obj = Horizons(id=obj, location=obs_code, epochs=epoch_jd)
            eph = horizons_obj.ephemerides()
            positions[obj] = (eph['EL'][0], eph['AZ'][0])  # Altitude, Azimuth

        fig, (ax_sky, ax_ground) = plt.subplots(1, 2, figsize=(12, 6), subplot_kw=dict(polar=True))
        fig.suptitle(f"Sky View from Observatory {obs_code} – {t_astropy.iso}", fontsize=14)

        for ax, title, bgcolor in zip([ax_sky, ax_ground], ["Above Horizon", "Below Horizon"], ['#f5faff', '#eaeaea']):
            ax.set_theta_zero_location('N')
            ax.set_theta_direction(-1)
            ax.set_rlim(0, 90)
            ax.set_title(title)
            ax.set_facecolor(bgcolor)
            ax.plot(np.linspace(0, 2 * np.pi, 500), [90]*500, color='gray', linestyle='--', linewidth=0.5)
            ax.set_rlabel_position(135)

        colors = {'Sun': 'orange', '301': 'gray'}
        for obj, (alt, az) in positions.items():
            az_rad = np.deg2rad(az)
            radius = 90 - abs(alt)
            color = colors.get(obj, 'red')  # Default: red
            if alt >= 0:
                ax_sky.plot(az_rad, radius, 'o', color=color, label=obj)
            else:
                ax_ground.plot(az_rad, radius, 'o', color=color, label=obj)

        ax_sky.legend(loc='lower left')
        ax_ground.legend(loc='lower left')
        plt.tight_layout()
        plt.show()
