Ransom C2C Detector
===================

Machine Learning Based Ransom C2C Detector.


* Free software: MIT license

<img src="https://travis-ci.org/uppusaikiran/ransom_c2c_detector.svg?branch=master">



## Usage:

1. Clone the Repo
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
2. Create a virutalenv
```
/tmp/dummy/ransom_c2c_detector
 % virtualenv venv
New python executable in /tmp/dummy/ransom_c2c_detector/venv/bin/python
Installing setuptools, pip, wheel...done.

```
3. Install the Required Packages.
```
 % pip install -r requirements_dev.txt
Requirement already satisfied: alabaster==0.7.10 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 1)) (0.7.10)
Requirement already satisfied: argh==0.26.2 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 2)) (0.26.2)
Requirement already satisfied: attrs==17.4.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 3)) (17.4.0)
Requirement already satisfied: Babel==2.5.3 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 4)) (2.5.3)
Requirement already satisfied: backports.functools-lru-cache==1.5 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 5)) (1.5)
Requirement already satisfied: bumpversion==0.5.3 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 6)) (0.5.3)
Requirement already satisfied: certifi==2018.4.16 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 7)) (2018.4.16)
Requirement already satisfied: chardet==3.0.4 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 8)) (3.0.4)
Requirement already satisfied: configparser==3.5.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 9)) (3.5.0)
Requirement already satisfied: coverage==4.5.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 10)) (4.5.1)
Requirement already satisfied: cycler==0.10.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 11)) (0.10.0)
Requirement already satisfied: docutils==0.14 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 12)) (0.14)
Requirement already satisfied: enum34==1.1.6 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 13)) (1.1.6)
Requirement already satisfied: flake8==3.5.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 14)) (3.5.0)
Requirement already satisfied: funcsigs==1.0.2 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 15)) (1.0.2)
Requirement already satisfied: idna==2.6 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 16)) (2.6)
Requirement already satisfied: imagesize==1.0.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 17)) (1.0.0)
Requirement already satisfied: Jinja2==2.10 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 18)) (2.10)
Requirement already satisfied: kiwisolver==1.0.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 19)) (1.0.1)
Requirement already satisfied: MarkupSafe==1.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 20)) (1.0)
Requirement already satisfied: matplotlib==2.2.2 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 21)) (2.2.2)
Requirement already satisfied: mccabe==0.6.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 22)) (0.6.1)
Requirement already satisfied: more-itertools==4.1.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 23)) (4.1.0)
Requirement already satisfied: nltk==3.2.5 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 24)) (3.2.5)
Requirement already satisfied: numpy==1.14.3 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 25)) (1.14.3)
Requirement already satisfied: packaging==17.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 26)) (17.1)
Requirement already satisfied: pandas==0.22.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 27)) (0.22.0)
Requirement already satisfied: pathtools==0.1.2 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 28)) (0.1.2)
Requirement already satisfied: pkginfo==1.4.2 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 29)) (1.4.2)
Requirement already satisfied: pluggy==0.6.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 30)) (0.6.0)
Requirement already satisfied: py==1.5.3 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 31)) (1.5.3)
Requirement already satisfied: pycodestyle==2.3.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 32)) (2.3.1)
Requirement already satisfied: pyflakes==1.6.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 33)) (1.6.0)
Requirement already satisfied: Pygments==2.2.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 34)) (2.2.0)
Requirement already satisfied: pyparsing==2.2.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 35)) (2.2.0)
Requirement already satisfied: pytest==3.5.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 36)) (3.5.0)
Requirement already satisfied: pytest-cov==2.5.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 37)) (2.5.1)
Requirement already satisfied: python-dateutil==2.7.2 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 38)) (2.7.2)
Requirement already satisfied: pytz==2018.4 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 39)) (2018.4)
Requirement already satisfied: PyYAML==3.12 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 40)) (3.12)
Requirement already satisfied: requests==2.18.4 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 41)) (2.18.4)
Requirement already satisfied: requests-file==1.4.3 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 42)) (1.4.3)
Requirement already satisfied: requests-toolbelt==0.8.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 43)) (0.8.0)
Requirement already satisfied: scikit-learn==0.19.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 44)) (0.19.1)
Requirement already satisfied: scipy==1.0.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 45)) (1.0.1)
Requirement already satisfied: six==1.11.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 46)) (1.11.0)
Requirement already satisfied: sklearn==0.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 47)) (0.0)
Requirement already satisfied: snowballstemmer==1.2.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 48)) (1.2.1)
Requirement already satisfied: Sphinx==1.7.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 49)) (1.7.1)
Requirement already satisfied: sphinxcontrib-websupport==1.0.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 50)) (1.0.1)
Requirement already satisfied: subprocess32==3.2.7 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 51)) (3.2.7)
Requirement already satisfied: tldextract==2.2.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 52)) (2.2.0)
Requirement already satisfied: tox==2.9.1 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 53)) (2.9.1)
Requirement already satisfied: tqdm==4.23.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 54)) (4.23.0)
Requirement already satisfied: twine==1.10.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 55)) (1.10.0)
Requirement already satisfied: typing==3.6.4 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 56)) (3.6.4)
Requirement already satisfied: urllib3==1.22 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 57)) (1.22)
Requirement already satisfied: virtualenv==15.2.0 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 58)) (15.2.0)
Requirement already satisfied: watchdog==0.8.3 in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from -r requirements_dev.txt (line 59)) (0.8.3)
Requirement already satisfied: setuptools in /home/admin/ransom_c2c_detector/venv/lib/python2.7/site-packages (from kiwisolver==1.0.1->-r requirements_dev.txt (line 19)) (40.0.0)
```
4. Make the Model
```
/tmp/dummy/ransom_c2c_detector
 % cd ransom_c2c_detector
admin@root /tmp/dummy/ransom_c2c_detector/ransom_c2c_detector
 % ls
data.csv  __init__.py  model.plk  model.py  ransom_c2c_detector.py  utils
admin@root /tmp/dummy/ransom_c2c_detector/ransom_c2c_detector
 % python ransom_c2c_detector.py
 ```
5. Run the Predictor Script which helps in predicting unknown urls.
```
 python model.py
INFO:__main__:URLModel:get_model()
Something wrong File not open for reading
INFO:__main__:RansomC2CDetector:create_corpus()
[2.663532754804255, 0.09151861261246144, 0.004186571949577747, 0.0002567613830879836, 0.0003830928361639637]
[*]Prediction for url gwbgmsmhgsp.com --> [1]
[2.75, 0.10122248604065265, 0.006589616361559483, 0.00019257103731598767, 0.0002873196271229728]
[*]Prediction for url facebook.com --> [0]
[2.1339375660949167, 0.10058688355294867, 0.004507770077122136, 0.0002781581650119822, 0.00041501723917762736]
[*]Prediction for url fklafkaaaassf.com --> [1]
[3.3232314287976203, 0.09591292856839724, 0.005411682974433002, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url puciftnfkplcbhp.net --> [1]
[3.3735572622751855, 0.09266339761338309, 0.005271302898258853, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url bowjjxxnhkyvygk.biz --> [1]
[3.5068905956085183, 0.09888045826589101, 0.0030378142068361643, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url osvwkptpwqyiqen.ru --> [1]
[3.640223928941852, 0.09015006751494577, 0.005937731371062851, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url cpmjpnwdgbxyyql.org --> [1]
[3.3735572622751855, 0.09234710330865999, 0.004987793673035381, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url ptlwqfsfvhxlaxw.co.uk --> [1]
[3.3735572622751855, 0.09396832544281, 0.002608515439458365, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url wwcdhdhijsfsuyr.info --> [1]
[3.240223928941852, 0.09064149258329363, 0.0024859599970877564, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url kbbqiudkyyffmeq.com --> [1]
[3.189898095464287, 0.09183726914608926, 0.0010277985362339775, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url xxrdnsgxijevnij.net --> [1]
[3.323231428797621, 0.09842381498176074, 0.003258183435700826, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url lcqqokcaxpeiowq.biz --> [1]
[3.4565647621309536, 0.09752592362946534, 0.004035195581902906, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url fhhvhiqlrtwpnik.ru --> [1]
[3.373557262275185, 0.09827483164842604, 0.003803209303146385, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url gwgweakshkaxnqv.org --> [1]
[3.6402239289418516, 0.10354928151178744, 0.005891174491725246, 0.00029955494693598085, 0.0005107904482186183]
[*]Prediction for url giwvnxpbqkvsnet.co.uk --> [1]
[3.3232314287976212, 0.08699136018850911, 0.00312622793769253, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url hxvwkpjigbybwyw.info --> [1]
[3.5068905956085192, 0.09834284754964771, 0.0049787483364783615, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url bpmpfnagtcdmuuk.com --> [1]
[3.5068905956085183, 0.09447294641055652, 0.005988544879368465, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url cflqcftnjsguukr.net --> [1]
[3.1395722619867232, 0.09655016017948378, 0.006025346983987714, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url cqcpldyvsscpnpk.biz --> [1]
[3.506890595608518, 0.09234832515119694, 0.0039192024425246455, 0.00034234851078397807, 0.0005107904482186183]
[*]Prediction for url dgbqiusdijfxwrj.ru --> [1]
[3.169925001442312, 0.09745807064058191, 0.001698306278465652, 0.0002139678192399863, 0.00031924403013663645]
[*]Prediction for url xjneysaum.us --> [0]
[2.1280852788913944, 0.08759649806895933, 0.0031128372923973327, 0.00017117425539198904, 0.00025539522410930913]
[*]Prediction for url hhbrghm.eu --> [0]

```
Here 1 indicates the model predicted as C2C Generated By Ransomware and 0 indicates the model predicted as non-genereated by Ransomware.


Features
--------

* TODO

