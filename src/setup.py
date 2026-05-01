from setuptools import setup
import setup_translate

pkg = 'Extensions.Moviearchiver'
setup(name='enigma2-plugin-extensions-moviearchiver',
       version='0.2',
       description='Archive or Backup your Movielist automatically. MovieArchiver by svox',
       package_dir={pkg: 'Moviearchiver'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
