from setuptools import setup, find_packages

setup(
    name='ping_script_test_package',  # Name of your package
    version='1.0.0',  # Version of your package
    packages=find_packages(),  # Automatically find the packages
    entry_points={
        'console_scripts': [
            'ping-script=ping_script.ping:main',  # Create a command-line tool called 'ping-script'
        ],
    },
    author='ntt_zz',
    author_email='thanhnguyentrung0910@gmail.com',
    description='A simple ping script utility.',
    long_description=open('README.md').read(),  # Read from README.md for long description (optional)
    long_description_content_type='text/markdown',
    url='https://github.com/nttzz/test_package_ping.git',  # URL to your project's repository
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version requirement
)
