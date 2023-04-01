# APItest.py

import requests
#note that you might need to install the requests module with pip or pip3


def main():

    url = "http://time.jsontest.com"
    results = requests.get(url)

    #print(results)
    #<Response [200]> is a good result

    json = results.json()

    # print the raw JSON data to see the shape of the data
    print(json)
    print()

    # The json can now be read as a Python dictionary.

    print("Date:  {}".format(json["date"]))
    print("Time:  {}".format(json["time"]))
    print("Epoch: {}".format(json["milliseconds_since_epoch"]))


if __name__ == "__main__":
    main()
