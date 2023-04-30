from setuptools import setup

setup(name='newm-atha',
      version='0.4',
      description='newm-atha - touchpad and touchscreen centric wayland compositor',
      url="https://sr.ht/~atha/newm-atha",
      author='~atha',
      author_email='74566464+Pandademic@users.noreply.github.com',
      packages=['newm', 'newm.helper', 'newm.resources', 'newm.overlay', 'newm.widget', 'newm.dbus', 'newm.gestures', 'newm.gestures.provider', 'newm_panel_basic'],
      package_data={'newm.resources': ['wallpaper.jpg', 'newm.desktop']},
      scripts=['bin/start-newm', 'bin/.start-newm', 'bin/newm-cmd', 'bin/newm-panel-basic'],
      install_requires=[
          'pycairo',
          'psutil',
          'python-pam',
          'pyfiglet',
          'dasbus',
          'thefuzz'
      ])
