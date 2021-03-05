from setuptools import setup
setup(
    name='pyXIOP-lechnerml',
    packages=['pyxiop'],
    package_dir={   'pyXIOP': 'pyXIOP',
                    'pyXIOP.lib':'pyXIOP/lib'
                },
    package_data={'pyXIOP.lib':[
        'darwin/*.dylib',
        'linux/*.so'
    ]}
)