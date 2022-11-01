import ast

import asn1tools


class ASN1(object):
    def __init__(self):
        self.foo = None
        self.main_key = ""

    def compile(self, file_name, code_X):
        self.foo = asn1tools.compile_files(file_name, code_X.lower())

    def get_mainName(self):
        foo_values = list(self.foo.modules.values())
        key_dict = foo_values[0]
        key_list = list(key_dict.keys())
        self.main_key = key_list[0]

        print(self.main_key)
        return self.main_key

    # str = "3054d69203130d151cc206e6d816f0"
    # "{'avaliableNetwork': {'available-AP-SSID': 'Mi 10', 'ap-Macadr': b'\x8a\x8ea\x03sl', 'frequencyBand': 1, 'rssi': 45, 'networkavailable': True, 'conn-Status': True, 'sec-Type': 'wpa-PSK'}}"
    def decode(self, str_s):
        bt = bytearray.fromhex(str_s)
        print(bt)
        re = self.foo.decode(self.get_mainName(), bt)
        re = self.get_dict_value(re)
        print(re)
        return re

    def encode(self, name, str_s):
        dic_data = ast.literal_eval(str_s)

        dic_data = self.set_dict_value(dic_data, "Hex-")

        re = self.foo.encode(name, dic_data)

        re = re.hex().upper()
        return re

    def get_dict_value(self, now_dict):
        for key in now_dict.keys():  # 当前迭代的字典
            data = now_dict[key]  # 当前key所对应的value赋给data

            if isinstance(data, dict):  # 如果data是一个字典，就递归遍历
                self.get_dict_value(data)

            if not isinstance(data, dict):  # 找到了目标key，并且它的value不是一个字典
                if isinstance(data, bytes):
                    now_dict[key] = "Hex-" + data.hex().upper()
                # results.append(now_dict[key])
        return now_dict

    def set_dict_value(self, now_dict, Str):
        for key in now_dict.keys():  # 当前迭代的字典
            data = now_dict[key]  # 当前key所对应的value赋给data

            if isinstance(data, dict):  # 如果data是一个字典，就递归遍历
                self.set_dict_value(data, Str)

            if isinstance(data, str):  # 找到了目标key，并且它的value不是一个字典
                if data.find(Str) != -1:
                    data = data.replace(Str, "")
                    now_dict[key] = bytes.fromhex(data)

                # results.append(now_dict[key])
        return now_dict
