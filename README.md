# PhishNet
## Overview
PhishNet provides a centralized way to find verified contact information for the organizations you interact with every day. PhishNet makes it easy to check whether you’re being contacted through valid channels or whether you’re being targeted by a phishing attack. If you receive an email or text message from an unknown source, you can immediately check its validity using PhishNet’s search feature. Simply copy the sender’s email address or phone number and PhishNet will tell you whether or not you’re interacting with who you think you are.


## Running PhishNet Locally
### Prerequisites
* Have Python installed locally. [See this guide for help](https://realpython.com/installing-python/)
* Install git if you don't have it already. [See this guide for help](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Step 1: Clone the Repository
Start by cloning this repository. You can do this by running the following command in Terminal (MacOS) or Command Prompt (Windows):

```shell
git clone https://github.com/AndersonCodingClub/PhishNet.git
```

Then, move into the newly cloned directory by running this command:

```shell
cd PhishNet
```

### Step 2: Install Flask
We use Flask to host PhishNet's web server locally. To install flask, run this command in Terminal/Command Prompt:

```python
pip install -U Flask
```

### Run the Web Server
There are multiple ways to start running the web server. You can type either of the below commands into Terminal/Command Prompt

Option 1:
```python
python app.py
```

OR

Option 2:
```python
flask run --host=localhost --port=3000
```

### Go to the Website
Finally, once you've run those commands, you should be able to go to [this link](http://localhost:3000/) and find the web page fully working.
Keep in mind this link won't work unless you've done each of the preceeding commands correctly.
