from setuptools import setup, find_packages

setup(
    name='server_ping',
    packages=find_packages(),
    author='dsociative',
    entry_points={
        'console_scripts': [
            'server_ping = server_ping.ping:main',
        ]
    },
    dependency_links=[
      "https://github.com/dsociative/socket_server2/archive/client_fix.zip#egg=socket_server2-0.0.0",
    ],
    install_requires=[
        'socket_server2'
    ]
)
