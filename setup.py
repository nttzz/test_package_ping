from setuptools import setup, find_packages
import os

this_directory = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = 'A simple ping script utility.'

def main():
    setup(
        name='ping_script_test_package',
        version='1.0.0',
        packages=find_packages(),  # Tự động tìm và bao gồm tất cả các package con
        entry_points={
            'console_scripts': [
                'ping-script=app_test.ping:main',  # Tạo công cụ dòng lệnh từ hàm main() trong ping.py
            ],
        },
        author='ntt_zz',
        author_email='thanhnguyentrung0910@gmail.com',
        description='A simple ping script utility.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/nttzz/test_package_ping.git',
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.6',
    )


