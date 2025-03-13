from setuptools import find_packages, setup

package_name = 'my_example_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nuke-wsl',
    maintainer_email='nuke-wsl@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'example_publisher = my_example_package.example_publisher:main',
            'example_subscriber = my_example_package.example_subscriber:main'
        ],
    },
)
