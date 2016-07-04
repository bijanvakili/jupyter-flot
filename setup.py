from setuptools import setup

# TODO avoid hardcoding version
PACKAGE_VERSION='0.0.1'

def main():
    setup(
        name='jupyter-flot',
        version=PACKAGE_VERSION,
        description='FlotCharts extensions for Jupyter Notebook',
        author='Bijan Vakili',
        author_email='bijvak2@gmail.com',
        license='MIT',
        packages=['flotcharts'],
        package_dir = {'': 'src'},
    )

if __name__ == "__main__":
    main()
