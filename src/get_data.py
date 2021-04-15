import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def get_Data(config_path):
    config = read_params(config_path)
    print(config)
    data_path = path + '\\'+ config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    return df

if __name__=="__main__":
    path=r"C:\Users\703202952\PycharmProjects\SIMPLE_APP"
    args=argparse.ArgumentParser()
    default_value=path+"\params.yaml"
    args.add_argument("--config",default=default_value)
    parsed_args=args.parse_args()
    print(get_Data(config_path=parsed_args.config))
    #with open(r"C:\Users\703202952\PycharmProjects\SIMPLE_APP\params.yaml") as yaml_file:
        #config=yaml.safe_load(yaml_file)
    #print(config)