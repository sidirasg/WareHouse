import configparser
import boto3


import configparser
import boto3

config = configparser.ConfigParser()
config.read("dwh.cfg")

config.get("CLUSTER", "HOST.l")


