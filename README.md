## Install DOTA_devkit

### 1.swing 
    sudo apt-get install swig

### 2.build_file

    cd DOTA_devkit
    swig -c++ -python polyiou.i
    python setup.py build_ext --inplace
 
