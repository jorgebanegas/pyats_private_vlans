# pyats_private_vlans
repo that leverages PYATS package to configure private vlans

1. First step will be to include the information of your device into the config.py file

```python
ip = ""
username = ""
password = ""
hostname = ""
```
2. Create virtual environment and name it env, then activate it

```console
foo@bar:~$ virtualenv env
foo@bar:~$ source env/bin/activate
```

4. Install the dependencies required for the python script
```console
foo@bar(env):~$ pip install -r requirements.txt
```

## Usage

To launch script:


    ```console
    foo@bar(env):~$ python vlan.py
    ```

