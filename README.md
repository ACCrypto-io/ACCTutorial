# ACC Tutorial

ACC develops data-tools for financial institutions working in Cryptocurrency market investment and risk management.
The ACC Simulator is an ACC tool to choose and asses machine learning models based on probabilities and profit/loss boundaries.

### Installation
This project is using Numpy. Please visit https://www.scipy.org/scipylib/download.html to install Numpy if you do not have it already (Ubuntu users can just follow the following commands).

Install python3.6 and pip if not already installed (Ubuntu commands).

```sh
$ sudo add-apt-repository ppa:deadsnakes/ppa;
$ sudo apt-get update;
$ sudo apt-get install python3.6;
$ curl https://bootstrap.pypa.io/get-pip.py | sudo python3.6;
$ sudo apt-get install build-essential libssl-dev libffi-dev python3.6-dev;
```

Install and create python3.6 virtual environment

```sh
$ sudo apt install python3.6-venv;
$ python3.6 -m venv .env-tutorial;
$ source .env-tutorial/bin/activate;
$ python3.6 -m pip install -r requirements.txt;
```

You can download the features data from https://ACCrypto.io, the btc-price-change-7days.csv.gz file (BTC price change) can be found in https://github.com/ACCrypto-io/AltoProDemo/tree/master/Data. 

### Running the code
```sh 
$ python3.6 tutorial_main.py
```
Please visit our YouTube channel for full tutorial walkthrough https://www.youtube.com/channel/UCkeN-rfUhsbmxwwNZ_pBFPw.

##### For inquiries contact us at inquiries@accrypto.io.

