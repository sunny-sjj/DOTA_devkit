import os
import os.path as osp
from HRSC2DOTA import generate_txt_labels
from DOTA2JSON import generate_json_labels
from DOTA2COCO_poly import DOTA2COCOTrain, DOTA2COCOTest, hrsc_2016

def preprare_hrsc2016(data_dir):
    train_dir = osp.join(data_dir, 'train')
    test_dir = osp.join(data_dir, 'test')
    # convert hrsc2016 to dota raw format
    # generate_txt_labels(train_dir)
    # generate_txt_labels(test_dir)

    # convert it to json format
    # generate_json_labels(train_dir, osp.join(train_dir,'train.json'))
    # generate_json_labels(test_dir, osp.join(test_dir,'test.json'), trainval=False)
    # DOTA2COCOTrain(train_dir,
    #                osp.join(train_dir,'train.json'),
    #                hrsc_2016)
    DOTA2COCOTest(test_dir,
                  osp.join(test_dir,'test.json'),
                  hrsc_2016)
if __name__ == '__main__':
    hrsc2016_dir = '/home/sunny/PycharmProjects/PCBproject/OrientedRepPoints-main/data/HRSC2016'
    preprare_hrsc2016(hrsc2016_dir)
    print('done')
