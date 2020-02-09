from enum import Enum
import datetime
import decimal


class Jsonable(object):
    def __iter__(self):
        for attr, value in self.__dict__.items():
#            print("attr: " + attr  + "- type:" + str(type(value)))
            if isinstance(value, datetime.datetime):
                iso = value.isoformat()
                yield attr, iso
            elif isinstance(value, decimal.Decimal):
                yield attr, str(value)
            elif isinstance(value, tuple):
                a = []
                a.append(value[0])
                a.append(value[1])
                yield attr, a
#            elif isinstance(value, Enum):
#                yield str(value)
            elif isinstance(value, str):
                yield attr, value
            elif isinstance(value, dict):
                yield attr, value
            elif(hasattr(value, '__iter__')):
                if(hasattr(value, 'pop')):
                    a = []
                    for subval in value:
                        if(hasattr(subval, '__iter__')):
                            a.append(dict(subval))
                        else:
                            a.append(subval)
                    yield attr, a
                else:
                    yield attr, dict(value)
            else:
                yield attr, value
