import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import pickle
from ransom_c2c_detector import RansomC2CDetector
import sys
import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class URLModel(object):
    """URLModel"""
    def __init__(self):
        """__init__"""
        self.version = '0.1.0'

    def set_data(self):
        self.file_path = os.path.join(os.path.dirname\
                        (os.path.realpath(__file__)),'utils/data.csv')
        self.df = pd.read_csv(self.file_path)
        self.X = self.df.iloc[:,[2,3,4,5,6]].values
        self.y = self.df.iloc[:,7].values

    def split(self,test_size=0.25,random_state=0):
        """split

        :param test_size:
        :param random_state:
        """
        self.test_size = test_size
        self.random_state = random_state
        self.X_train, self.X_test, self.y_train, self.y_test = \
        train_test_split(self.X, self.y, test_size =self.test_size, \
        random_state = self.random_state)

    def featureScaler(self):
        """featureScaler"""
        self.sc = StandardScaler()
        self.X_train = self.sc.fit_transform(self.X_train)
        self.X_test = self.sc.transform(self.X_test)

    def apply_alg(self,n_estimators,criterion,random_state):
        """apply_alg

        :param n_estimators:
        :param criterion:
        :param random_state:
        """
        self.classifier = RandomForestClassifier(n_estimators = 10, \
                criterion = 'entropy', random_state = 0)
        self.classifier.fit(self.X_train, self.y_train)
        return self.classifier

    def get_classifier(self):
        """get_classifier"""
        return self.classifier

    def predict(self):
        """predict"""
        self.y_pred = self.classifier.predict(self.X_test)
        return self.y_pred

    def cf_matrix(self):
        self.cm = confusion_matrix(self.y_test, self.y_pred)
        return self.cm

    def save_model(self,model):
        """save_model

        :param model:
        """
        self.filename = 'model.plk'
        pickle.dump(model,open(self.filename , 'wb'))
        return

    def get_model(self,filename):
        """get_model

        :param filename: Model filename to get model.
        """
        self.filename = filename
        self.classifier = pickle.load(open(self.filename,'rb'))
        return self.classifier

    def pred(self,features):
        """pred

        :param features:
        """
        self.features = np.asarray(features).reshape(1,5)
        self.res = self.classifier.predict(self.features)
        return self.res


def make_model():
    m = URLModel()
    m.set_data()
    m.split()
    #m.featureScaler()
    m.apply_alg(10,'entropy',0)
    m.predict()
    print m.cf_matrix()
    m.save_model(m.get_classifier())


def test_model_with_new_record():
    domain_list = ['gwbgmsmhgsp.com','facebook.com','fklafkaaaassf.com',\
                   'puciftnfkplcbhp.net','bowjjxxnhkyvygk.biz',\
                   'osvwkptpwqyiqen.ru','cpmjpnwdgbxyyql.org',\
                   'ptlwqfsfvhxlaxw.co.uk','wwcdhdhijsfsuyr.info',\
                   'kbbqiudkyyffmeq.com','xxrdnsgxijevnij.net',\
                   'lcqqokcaxpeiowq.biz','fhhvhiqlrtwpnik.ru',\
                   'gwgweakshkaxnqv.org','giwvnxpbqkvsnet.co.uk',\
                   'hxvwkpjigbybwyw.info','bpmpfnagtcdmuuk.com',\
                   'cflqcftnjsguukr.net','cqcpldyvsscpnpk.biz',\
                   'dgbqiusdijfxwrj.ru','xjneysaum.us','hhbrghm.eu','jijps.in',\
                   'ernthxdqkbuoi.tf','npixhjhhmpm.uk','burfvaac.pm',\
                   'ksmbxx.in','mtuamviphwoapcq.uk','jjrlgvdlqurpa.pm',\
                   'shmcsgbpypg.fr','uivmeislw.eu','prsobv.pm',\
                   'ypnlcncyegxteub.in','bqvjrrodkfhjg.it','vaaytyxqyl.eu',\
                   'fxnitwaq.fr','pvmyilqakqqkl.in','kfqoruddyo.nl',\
                   'myxmilto.it','hicqd.us','qnqlfdthdyidbw.be',\
                   'shxppmfnhjao.pm','nqcxfhycl.in','wowkllj.it']

    m = URLModel()
    logger.info('URLModel:get_model()')
    m.get_model('model.plk')
    c2 = RansomC2CDetector()
    logger.info('RansomC2CDetector:create_corpus()')
    c2.create_corpus()
    for i in range(len(domain_list)):
        domain_name = domain_list[i]
        full_domain = domain_name.lower()
        domain_name = c2.clean_url(full_domain).replace('$','')
        ent = c2.entropy(domain_name)
        c2.calculate_bigrams(domain_name)
        c2.calculate_trigrams(domain_name)
        bi_score = c2.bigram_score(domain_name)
        tri_score= c2.trigram_score(domain_name)
        c2.trigram_score_old(domain_name)
        trigram_benign = c2.trigram_benign
        trigram_malicious = c2.trigram_malicious
        data = [ent,bi_score,tri_score,trigram_benign,trigram_malicious]
        print data
        res = m.pred(data)
        print '[*]Prediction for url {} --> {}'.format(domain_list[i],res)


if __name__ == '__main__':
    #make_model()
    test_model_with_new_record()
