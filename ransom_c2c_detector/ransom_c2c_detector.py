from __future__ import division
#-*- coding: utf-8 -*-

"""Main module."""
import math
import sys
import nltk
from nltk import word_tokenize,ngrams
#nltk.download('punkt')
import os
import tldextract
import csv
import pickle

class RansomC2CDetector(object):
    """RansomC2CDetector"""
    def __init__(self):
        """__init__"""
        self.score = 0
        self.corpus = []
        self.clean_domains = []
        self.clean_bigrams = []
        self.clean_trigrams = []
        self.mal_bigrams = []
        self.mal_trigrams = []
        self.malicious_domains = []
        try:
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                                 'utils/clean_bigrams.pkl'),'wb') as f:
                self.clean_bigrams = pickle.load(f)
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                                 'utils/clean_trigrams.pkl'),'wb') as f:
                self.clean_trigrams = pickle.load(f)
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                                 'utils/mal_bigrams.pkl'),'wb') as f:
                self.mal_bigrams = pickle.load(f)
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                                 'utils/mal_trigrams.pkl'),'wb') as f:
                self.mal_trigrams = pickle.load(f)

        except Exception as e:
            print 'Something wrong {}'.format(e)
    def entropy(self,domain):
        """entropy

        :param domain: Domain passed
        """
        self.domain = domain
        self.ent = 0.0
        self.prob = [ float(self.domain.count(c)) / len(self.domain) for c in\
                     dict.fromkeys(list(self.domain))]
        self.ent =  - sum([p * math.log(p) /math.log(2.0) for p in self.prob])
        return self.ent

    def create_corpus(self):
        """corpus

        :param domain: Doamin passed will be split and words are stored in
        corpus.
        """
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'utils/alexa1million.txt'),'r') as f:
            for line in f:
                line = line.rstrip()
                #print self.clean_url(line)
                #self.clean_domains.append(line)
                self.line_bigram = self.calculate_bigrams(line)
                for i in self.line_bigram:
                    self.clean_bigrams.append(i)
                self.line_trigram = self.calculate_trigrams(line)
                for i in self.line_trigram:
                    self.clean_trigrams.append(i)
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'utils/dga.txt'),'r') as f:
            for line in f:
                line = line.rstrip()
                #self.malicious_domains.append(line)
                self.line_bigram = self.calculate_bigrams(line)
                for i in self.line_bigram:
                    self.mal_bigrams.append(i)
                self.line_trigram = self.calculate_trigrams(line)
                for i in self.line_trigram:
                    self.mal_trigrams.append(i)

        # Store the Datasets in pickle Formats
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                               'utils/clean_bigrams.pkl'),'wb') as f:
            pickle.dump(self.clean_bigrams , f)

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                               'utils/clean_trigrams.pkl'),'wb') as f:
            pickle.dump(self.clean_trigrams , f)
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                               'utils/mal_bigrams.pkl'),'wb') as f:
            pickle.dump(self.mal_bigrams , f)
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                               'utils/mal_trigrams.pkl'),'wb') as f:
            pickle.dump(self.mal_trigrams, f)
        return 1

    def calculate_bigrams(self,domain):
        """calculate_bigrams

        :param domain: Domain to calculate calculate_bigrams
        """
        self.domain = self.clean_url(domain)
        self.bgrm = list(ngrams(self.domain,2))
        self.bgrm = [''.join(a) for a in self.bgrm ]
        return self.bgrm

    def calculate_trigrams(self,domain):
        """calculate_trigrams

        :param domain: Domain to get list of calculate_bigrams
        """
        self.domain = self.clean_url(domain)
        self.tgrm = list(ngrams(self.domain,3))
        self.tgrm = [''.join(a) for a in self.tgrm]
        return self.tgrm

    def clean_url(self,domain):
       """clean_url

       :param domain: Domain name
       """
       self.ext = tldextract.extract(domain.lower())
       self.domain = '.'.join(self.ext[:2])
       self.domain = self.domain.replace('.','$')
       self.domain = '$' + self.domain + '$'
       return self.domain

    def bigram_score_old(self,domain):
        """bigram_score

        :param domain:
        """
        self.bigram_score_clean = 0.0
        self.bigram_score_mal   = 0.0
        for i in set(self.calculate_bigrams(domain)):
            if i in set(self.clean_bigrams):
                self.bigram_score_clean +=1
            if i in set(self.mal_bigrams):
                self.bigram_score_mal += 1
        self.bigram_benign = self.bigram_score_clean / len(set(self.calculate_bigrams(domain)))
        self.bigram_malicious = self.bigram_score_mal / len(set(self.calculate_bigrams(domain)))
        return self.bigram_score_clean
        #return (self.bigram_score/len(self.clean_bigrams)) *100

    def bigram_score(self,domain):
        """bigram_score

        :param domain:
        """
        self.domain = domain
        self.gram_freq = {}
        self.bi_score = 0.0
        from collections import Counter
        #self.bgrm = self.calculate_bigrams(self.domain)
        #print Counter([self.clean_bigrams.count(x) for x in self.bgrm])
        for x in self.bgrm:
            self.gram_freq[x] = {}
            self.gram_freq[x]['occur'] = self.clean_bigrams.count(x)
            self.gram_freq[x]['freq']  = self.clean_bigrams.count(x)/len(self.clean_bigrams)
        #print self.gram_freq
        for key,value in self.gram_freq.iteritems():
            self.bi_score += value['freq']
        return self.bi_score


    def trigram_score_old(self,domain):
        """trigram_score

        :param domain:
        """
        self.trigram_score_clean = 0.0
        self.trigram_score_mal   = 0.0
        for i in set(self.calculate_trigrams(domain)):
            if i in set(self.clean_trigrams):
                self.trigram_score_clean +=1
            if i in set(self.mal_trigrams):
                self.trigram_score_mal += 1
        self.trigram_benign = self.trigram_score_clean / len(set(self.clean_trigrams))
        self.trigram_malicious = self.trigram_score_mal / len(set(self.mal_trigrams))
        return self.trigram_score_clean , self.trigram_score_mal

    def trigram_score(self,domain):
        """trigram_score

        :param domain:
        """
        self.domain = domain
        self.gram_freq = {}
        self.tri_score = 0.0
        #self.tgrm = self.calculate_trigrams(self.domain)
        for x in self.tgrm:
            self.gram_freq[x] = {}
            self.gram_freq[x]['occur'] = self.clean_trigrams.count(x)
            self.gram_freq[x]['freq']   = self.clean_trigrams.count(x) / len(self.clean_trigrams)
        #print self.gram_freq
        for key,value in self.gram_freq.iteritems():
            self.tri_score += value['freq']
        return self.tri_score

    def write_to_file(self):
        """write_to_file"""
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'utils/data.csv'),'wb') as f:
            writer = csv.writer(f)
            writer.writerow(["Full_Domain","Domain","Entropy","Bigram_score","Trigram_score","Trigram_benign_score","Trigram_malicious_score","label"])
            return 'success',200

    def generate_data(self):
        """generate_data"""
        self.file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        #Clean Domains
        data_list = ['utils/alexa1million.txt','utils/dga.txt']
        with open(os.path.join(self.file_path,'utils/alexa1million.txt'),'r') as f:
            #Traverse each line and add it to training set.
            for domain_name in f:
                full_domain = domain_name.rstrip().lower()
                #print 'Processing clean url {}'.format(full_domain)
                domain_name = self.clean_url(full_domain).replace('$','')
                ent = self.entropy(full_domain)
                self.calculate_bigrams(full_domain)
                self.calculate_trigrams(full_domain)
                bi_score = self.bigram_score(full_domain)
                tri_score= self.trigram_score(full_domain)
                self.trigram_score_old(full_domain)
                trigram_benign = self.trigram_benign
                trigram_malicious = self.trigram_malicious
                label = 0
                data = '{},{},{},{},{},{},{},{}'.format(full_domain,domain_name,ent,bi_score,tri_score,trigram_benign,trigram_malicious,label)
                self.save_data(data)
        #Malicious Domains
        return
    def save_data(self,data):
        with open(os.path.join(self.file_path , 'utils/data.csv'),'a') as f:
            f.write(data)
            f.write('\n')

if __name__ == '__test__':
    c2 = RansomC2CDetector()
    c2.create_corpus()
    print c2.entropy(sys.argv[1])
    print c2.calculate_bigrams(sys.argv[1])
    print c2.calculate_trigrams(sys.argv[1])
    print 'Bigram Score {}'.format(c2.bigram_score(sys.argv[1]))
    print 'Trigram score {}'.format(c2.trigram_score(sys.argv[1]))
    c2.trigram_score_old(sys.argv[1])
    print 'Trigram benign score {}'.format(c2.trigram_benign)
    print 'Trigram malicious score {}'.format(c2.trigram_malicious)
    c2.write_to_file()


if __name__ == '__main__':
    c2 = RansomC2CDetector()
    c2.create_corpus()
    c2.generate_data()
