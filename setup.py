from distutils.core import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='Cirro',
    version='0.1dev',
    packages=['cirro',],
    license='MIT License',
    long_description=open('README.md').read(),
    install_requires=reqs
)
