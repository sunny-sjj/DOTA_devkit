import os
import os.path as osp
from HRSC2DOTA import generate_txt_labels
from DOTA2JSON import generate_json_labels
from DOTA2COCO_poly import DOTA2COCOTrain, DOTA2COCOTest, hrsc_2016, ucas_aod

def preprare_ucas_aod(data_dir):

    train_dir = osp.join(data_dir, 'train')
    test_dir = osp.join(data_dir, 'test')
    # convert hrsc2016 to dota raw format
    # generate_txt_labels(train_dir)
    # generate_txt_labels(test_dir)

    # convert it to json format
    # generate_json_labels(train_dir, osp.join(train_dir,'train.json'))
    # generate_json_labels(test_dir, osp.join(test_dir,'test.json'), trainval=False)

    #convert it to coco format
    DOTA2COCOTrain(train_dir,
                   osp.join(train_dir, 'train.json'),
                   ucas_aod)
    DOTA2COCOTest(test_dir,
                  osp.join(test_dir, 'test.json'),
                  ucas_aod)
if __name__ == '__main__':
    ucas_aod_dir = '/home/sunny/PycharmProjects/PCBproject/OrientedRepPoints-main/data/UCAS_AOD'
    preprare_ucas_aod(ucas_aod_dir )
    print('done')
