res_path, z = [], ""


def biggestPath(X: dict) -> str:
    global res_path
    global z
    result = {}
    parameter_for_len = 0
    """Ищем поддиректории, т.е. вложенные файлы"""
    if type(X) == dict:
        for key, value in X.items():
            """Ищем максимальную вложенность"""
            if len(value) > parameter_for_len and type(value) == dict:
                result = {key: value}
                parameter_for_len = len(value)
                res_path.append(key)
            last_element = key
        try:
            """Рекурсией проходимся по вложенным словарям"""
            biggestPath(result[last_element])
        except KeyError:
            """Найдя последний вложенный словарь, добавляем его в результат"""
            res_path.append(last_element)
    """Случай, когда в исходном словаре не оказалось вложенных словарей. Исследуем вложенный список"""
    if len(res_path) == 1:
        """Если все файлы имеют одинаковое имя"""
        if len(set(X[res_path[0]])) == 1:
            res_path = ""
        elif len(set(X[res_path[0]])) == len(X[res_path[0]]):
            """Если все имена файлов разные"""
            res_path.append(X[res_path[0]][0])
        else:
            """Случай, когда есть одинаковые имена файлов"""
            for element in X[res_path[0]]:
                if X[res_path[0]].count(element) == 1:
                    res_path.append(element)
                    break
    return f"/{'/'.join(res_path)}"


def test():
    assert biggestPath({'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}) == "/dir3/dir5/dir6/dir7"
    #assert biggestPath({'dir1': ['file1', 'file1']}) == '/'
    #assert biggestPath({'dir1': ['file1', 'file2', 'file2']}) == "/dir1/file1"
    #assert biggestPath({"dir1": {}, "dir2": ["file1", "file2", "file3"]}) == "/dir2/file1"
    #assert biggestPath({"dir1": ['file1', 'file1'], "dir2": ["file1", "file2", "file3"]}) == "/dir2/file1"


if __name__ == "__main__":
    test()
