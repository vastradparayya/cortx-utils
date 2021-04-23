import json
import hashlib
import os
from os import path
from cortx.utils.conf_store import Conf

temp_conf_file = '/etc/cortx/cortx.conf'
temp_track_json_file = "/tmp/in_memory_tracked_files.json"


def load_conf_files():
    try:
        # Load Configuration
        Conf.load('index1', 'json://' + temp_conf_file)

        track_changed_conf_files(temp_conf_file, 'index1')
        Conf.load('index2', 'json://' + temp_conf_file)
        track_changed_conf_files(temp_conf_file, 'index2')
        Conf.load('index3', 'json://' + temp_conf_file)
        track_changed_conf_files(temp_conf_file, 'index3')
        # # Conf.load('index2', 'consul://consul.cortx.colo.com:8500')  # consul.cortx.colo.com is a consul server.

        # Get Config entries
        val1 = Conf.get('index1', 'keygroup3')
        # val2 = Conf.get('index2', 'keygroup3>key>subkey')
        print(val1)
        # print(val2)

        # getting hash of file before modifying file
        before_modify_hash_value = hashlib.md5(open(temp_conf_file, 'rb').read()).hexdigest()
        # Modify Config entries
        Conf.set('index1', 'keygroup3>key>subkey', 'modified value1')
        Conf.save('index1')
        # getting hash of file after modifying file
        after_modify_hash_value = hashlib.md5(open(temp_conf_file, 'rb').read()).hexdigest()

        if before_modify_hash_value == after_modify_hash_value:
            print("Not modified")
        else:
            # Notify all loaded in memory callers
            print("Modified")

            with open(temp_track_json_file) as f:
                data = json.load(f)
                print(data)
    except Exception as err:
        print(err)
    finally:
        # remove loaded files from temp file
        pass


def create_sample_file():
    if not path.exists(temp_track_json_file):
        with open(temp_track_json_file, "w+") as f:
            json.dump({}, f, indent=2)


def track_changed_conf_files(file_type, index):
    # Get the process ID of
    # the current process
    pid = os.getpid()

    with open(temp_track_json_file, "r") as f:
        data = json.load(f)
    try:
        with open(temp_track_json_file, "w") as f:
            if data:
                for x in data[file_type]:
                    if x["PID"] == pid:
                        data[file_type].remove(x)
                        # data[file_type]["PID"] = pid
                        x["indexes"].append(index)
                    else:
                        x = {"PID": pid, "indexes": [index]}
                data[file_type].append(x)
                json.dump(data, f, indent=2)
            else:
                data[file_type] = [{"PID": pid, "indexes": [index]}]
                json.dump(data, f, indent=2)
    except Exception as err:
        with open(temp_track_json_file, "w") as f:
            json.dump(data, f, indent=2)


create_sample_file()
load_conf_files()
