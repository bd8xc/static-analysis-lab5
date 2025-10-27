import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='inventory.log', level=logging.INFO)

stock_data = {}

def addItem(item="default", qty=0, logs=None):
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.error("Invalid item or quantity types.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return logs

def removeItem(item, qty):
    try:
        if item not in stock_data:
            raise KeyError(f"Item '{item}' not found in stock.")
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        logging.warning(e)

def getQty(item):
    return stock_data.get(item, 0)

def loadData(file="inventory.json"):
    global stock_data
    try:
        with open(file, "r") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        logging.warning(f"{file} not found. Starting with empty inventory.")
        stock_data = {}

def saveData(file="inventory.json"):
    with open(file, "w") as f:
        json.dump(stock_data, f)

def printData():
    print("Items Report:")
    for i, qty in stock_data.items():
        print(f"{i} -> {qty}")

def checkLowItems(threshold=5):
    return [i for i, qty in stock_data.items() if qty < threshold]

def main():
    addItem("apple", 10)
    addItem("banana", -2)
    addItem("orange", 5)
    removeItem("apple", 3)
    removeItem("orange", 1)
    print(f"Apple stock: {getQty('apple')}")
    print(f"Low items: {checkLowItems()}")
    saveData()
    loadData()
    printData()

if __name__ == "__main__":
    main()
