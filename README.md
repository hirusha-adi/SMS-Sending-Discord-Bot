# SMS Sending Discord Bot

Send SMS to any supported number using Telnyx easily within discord

# Setup

## 1. Install dependencies

### Windows

```
py -m pip install -r requirements.txt
```

### Other

```
python3 -m pip install -r requirements.txt
```

## 2. Fill Required Information

Fill in the information, save and exit

### Windows

```
notepad .\bot\database\data\main.json
notepad .\bot\database\data\telnyx.json
```

### Other

```
nano ./bot/database/data/main.json
nano ./bot/database/data/telnyx.json
```

## 3. Start Discord Bot

### Windows

```
py main.py
```

### Other

```
python3 main.py
```

# Usage

```
Usage -->
  >sms <to_number> *[text]

Example -->
  >sms +12345678910 any text that comes after the phone number to be sent will be the content of the message
```

- Admin Commands

```
Usage -->
    >change_number <number>

Example -->
    >change_number 1234567890
```

```
Usage -->
    >change_number <api_key>

Example -->
    >change_number VerySecretAPIKeyDoNotShare
```
