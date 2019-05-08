# encoding=utf8
import types
import emoji


def smart_decode(text):
    """智能转码"""
    if text is None:
        return ''
    if isinstance(text, types.UnicodeType):
        return text
    try:
        return text.decode('utf8')
    except UnicodeDecodeError:
        try:
            return text.decode('gb2312')
        except UnicodeDecodeError:
            pass
    return text


def emojize(content):
    """将内容中的输入法表情转移字符串转换为输入法表情"""
    return emoji.emojize(content)


def replace_unvisiable(content):
    '''
    去除一些不可见字符的公共方法
    :param content:
    :return:
    '''
    content = content.strip()
    for one in [u'\u3000', u'\u0020', u'\u0009', u'\u000b', u'\u000c', u'\u00a0', u'\u000a', u'\u000d', u'\u2028',
                u'\u2029', u'\u200f', u'\u200e', u'\u200d', u'\ufeff', u'\u0005', u'\u0001', u'\u0003']:
        content = content.replace(one, '')
    return content


def filter_entity(entitys):
    '''
    功能函数：获取查询结果的所有字段，格式化成 [{}, {}]
    :param all_datas:
    :return:
    '''
    temp_result = []
    if entitys:
        for entity in entitys:
            fields = [one.attname for one in entity._meta._field_name_cache]
            break
    else:
        return temp_result
    # 格式化查询数据
    for one_data in entitys:
        temp_dict = {}
        for field_name in fields:
            if not getattr(one_data, field_name):
                temp_dict[field_name] = None
            elif type(getattr(one_data, field_name)) in [int, long]:
                temp_dict[field_name] = int(getattr(one_data, field_name))
            elif type(getattr(one_data, field_name)) in [str, unicode]:
                temp_dict[field_name] = getattr(one_data, field_name)
            else:
                temp_dict[field_name] = str(getattr(one_data, field_name, ''))
        temp_result.append(temp_dict)
    return temp_result
