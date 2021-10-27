#Install DOTA_devkit

## 1.swing 
    sudo apt-get install swig

## 2.build_file
    swig -c++ -python polyiou.i
    python setup.py build_ext --inplace
 
