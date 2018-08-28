# Ransom C2C Detector

Machine Learning Based Ransom C2C URL/Domain Detector.

[![Language](https://img.shields.io/badge/Python-2.7-blue.svg?style=plastic&colorB=68B7EB)]()
[![License](https://img.shields.io/github/license/vhesener/Closures.svg?style=plastic&colorB=68B7EB)]()
[![Release](https://img.shields.io/github/release/vhesener/Closures.svg?style=plastic&colorB=68B7EB)]()

**Ransom C2C Detector!** helps in finding the on-fly generated domains while ransomware infections:

* Easy to Generate New Model apt to requirements.
* Pluggable model to adapt to new variants of ransomwares.
* Uses n-gram technique to detect domains generated by ransomware.
* Support Algorthim Selector to choose algorthim to use based on the Efficasy.

## ▶️ Installation

### ▶️ Clone the Repo

```
% git clone git@github.com:uppusaikiran/ransom_c2c_detector.git
Cloning into 'ransom_c2c_detector'...
remote: Counting objects: 63, done.
remote: Compressing objects: 100% (52/52), done.
remote: Total 63 (delta 12), reused 51 (delta 6), pack-reused 0
Receiving objects: 100% (63/63), 23.16 MiB | 696.00 KiB/s, done.
Resolving deltas: 100% (12/12), done.
Checking connectivity... done.

```

### ▶️ Create a virutalenv

```
/tmp/dummy/ransom_c2c_detector
 % virtualenv venv
New python executable in /tmp/dummy/ransom_c2c_detector/venv/bin/python
Installing setuptools, pip, wheel...done.

```

### ▶️ Install the Required Packages

```
 % pip install -r requirements_dev.txt

```
### ▶️ Make the Model

* To make the model,navigate to the project root and run the script.As this creation of model takes long time,a generated model is already included.

```
 % cd ransom_c2c_detector
admin@root /tmp/dummy/ransom_c2c_detector/ransom_c2c_detector
admin@root /tmp/dummy/ransom_c2c_detector/ransom_c2c_detector
 % python ransom_c2c_detector.py
 ```
### ▶️ Run the Predictor Script which helps in predicting unknown urls

```
 python predictor.py 
[*]Prediction for url gwbgmsmhgsp.com --> [1]
[*]Prediction for url facebook.com --> [0]
[*]Prediction for url fklafkaaaassf.com --> [1]
[*]Prediction for url puciftnfkplcbhp.net --> [1]
[*]Prediction for url bowjjxxnhkyvygk.biz --> [1]
[*]Prediction for url osvwkptpwqyiqen.ru --> [1]
[*]Prediction for url cpmjpnwdgbxyyql.org --> [1]
[*]Prediction for url ptlwqfsfvhxlaxw.co.uk --> [1]
[*]Prediction for url wwcdhdhijsfsuyr.info --> [1]
[*]Prediction for url kbbqiudkyyffmeq.com --> [1]
[*]Prediction for url xxrdnsgxijevnij.net --> [1]
[*]Prediction for url lcqqokcaxpeiowq.biz --> [1]
[*]Prediction for url fhhvhiqlrtwpnik.ru --> [1]
[*]Prediction for url gwgweakshkaxnqv.org --> [1]
[*]Prediction for url giwvnxpbqkvsnet.co.uk --> [1]
[*]Prediction for url hxvwkpjigbybwyw.info --> [1]
[*]Prediction for url bpmpfnagtcdmuuk.com --> [1]
[*]Prediction for url cflqcftnjsguukr.net --> [1]
[*]Prediction for url cqcpldyvsscpnpk.biz --> [1]
[*]Prediction for url dgbqiusdijfxwrj.ru --> [1]
[*]Prediction for url xjneysaum.us --> [0]
[*]Prediction for url hhbrghm.eu --> [0]

```
* Here 1 indicates the model predicted as C2C Generated By Ransomware and 0 indicates the model predicted as non-genereated by Ransomware.


Features
--------

* TODO

TODO
--------

* Write a brief in Readme explaining how model works.
* Show the detection Accuracy. 
* Decrease the time for model-building and prediction.(Top Priority)
