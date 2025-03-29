def scob(string, Len = None, ar = [], Len2 = None, x = None, n = None, z = []):
    if Len != -1 and Len2 == None:
        if Len == None:
            return scob(string, len(string) - 1)
        if (string [Len] == '(' or string [Len] == ')' or string [Len] == '[' or string [Len] == ']' or string [Len] == '{' or string [Len] == '}'):
            ar.append(string[Len])
        return scob(string, Len - 1, ar)
    elif Len == -1:
        if len(ar) % 2 != 0:
            return '''False
#У скобки нет пары.
# Возможно вы пропустили скобку из-за чего она только открывается либо только закрывается'''
        else:
            if '(' in ar or ')'in ar or'['in ar or ']'in ar or '{' in ar:
                Ar_len = len(ar) -1
                return scob(None, None, ar, Ar_len, Ar_len - 1)
            else:
                return 'Скобок нет!!!'
            
    if Len2 != 0: 
        if n == None:
            n = 0
        if str(ar[Len2]) == ')' and not Len2 in z:
            return 'В скобках ошибка с )'
        elif str(ar[Len2]) == ']' and not Len2 in z:
            return 'В скобках ошибка с ]'
        elif str(ar[Len2]) == '}' and not Len2 in z:
            return 'В скобках ошибка с }'
        # для )
        if str(ar[Len2]) == '(':
            if str(ar[Len2]) == str(ar[x]): #Если одинаковы скобки )), ]], }} то n + 1
                return scob(None, None, ar, Len2, x - 1, n + 1, z)
            elif str(ar[Len2-1]) == ']' or str(ar[Len2-1]) == '}':
                return 'Скобка в скобке ( [ ) { ] }'
            elif str(ar[x]) == ')' and n != 0: #Если находит пару и n не равен 0 минусует с n 1
                if x > -1:
                    return scob(None, None, ar, Len2, x - 1, n - 1, z)
                else:
                    return 'FALSE'
            elif int(x) in z:
                return scob(None, None, ar, Len2, x-1, n, z)
            elif str(ar[x]) == ')' and n == 0 and not x in z: #Если находит пару и n равен 0 то добавляет индекс Len2 и x в перременную z
                z.append(Len2)
                z.append(x)
                return scob(None, None, ar, Len2 - 1, Len2 -2, None, z)
                
            else:
                return scob(None, None, ar, Len2, x-1, n, z)
        # для ]
        elif str(ar[Len2]) == '[':
            if str(ar[Len2]) == str(ar[x]): #Если одинаковы скобки )), ]], }} то n + 1
                return scob(None, None, ar, Len2, x - 1, n + 1, z)
            elif str(ar[Len2-1]) == ')' or str(ar[Len2-1]) == '}':
                return 'Скобка в скобке ( [ ) { ] }'
            elif str(ar[x]) == ']' and n != 0: #Если находит пару и n не равен 0 минусует с n 1
                if x > -1:
                    return scob(None, None, ar, Len2, x - 1, n - 1, z)
                else:
                    return 'FALSE'
            elif int(x) in z:
                return scob(None, None, ar, Len2, x-1, n, z)
            elif str(ar[x]) == ']' and n == 0 and not x in z: #Если находит пару и n равен 0 то добавляет индекс Len2 и x в перременную z
                z.append(Len2)
                z.append(x)
                return scob(None, None, ar, Len2 - 1, Len2 -2, None, z)
                
            else:
                return scob(None, None, ar, Len2, x-1, n, z)
            # для }
        elif str(ar[Len2]) == '{':
            if str(ar[Len2]) == str(ar[x]): #Если одинаковы скобки )), ]], }} то n + 1
                return scob(None, None, ar, Len2, x - 1, n + 1, z)
            elif str(ar[Len2-1]) == ')' or str(ar[Len2-1]) == ']':
                return 'Скобка в скобке ( [ ) { ] }'
            elif str(ar[x]) == '}' and n != 0: #Если находит пару и n не равен 0 минусует с n 1
                if x > -1:
                    return scob(None, None, ar, Len2, x - 1, n - 1, z)
                else:
                    return 'FALSE'
            elif int(x) in z:
                return scob(None, None, ar, Len2, x-1, n, z)
            elif str(ar[x]) == '}' and n == 0 and not x in z: #Если находит пару и n равен 0 то добавляет индекс Len2 и x в перременную z
                z.append(Len2)
                z.append(x)
                return scob(None, None, ar, Len2 - 1, Len2 -2, None, z)
                
            else:
                return scob(None, None, ar, Len2, x-1, n, z)
        elif not str(ar[Len2]) == '(': #Если x не  ( то получаем что-то там
            return scob(None, None, ar, Len2 - 1, Len2 - 2, None, z)
        elif not str(ar[Len2]) == '[': #Если x не  ( то получаем что-то там
            return scob(None, None, ar, Len2 - 1, Len2 - 2, None, z)
        elif not str(ar[Len2]) == '{': #Если x не  ( то получаем что-то там
            return scob(None, None, ar, Len2 - 1, Len2 - 2, None, z)
        else:
            return 'False'
    else:
        return 'True'

print(scob(input('Введите данные строки со скобками например: input(\'Введите данные строки со скобками например: input(\'[{True}]\')\')\nВвод: ')))