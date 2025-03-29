import vk_api
import re
VK_API_KEY = "Тут Api VK"
GROUP_ID = "lololoshkashop24"


def get_last_post(group_id, token):
    """Получение последнего поста из группы ВКонтакте."""
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    try:
        response = vk.wall.get(domain=group_id, count=1)
        if response['items']:
            last_post = response['items'][0]
            post_text = last_post.get('text', 'Нет текста')
            return {
                "Текст поста": post_text,
            }
        else:
            return "В группе пока нет постов."
    except vk_api.exceptions.ApiError as e:
        return f"Ошибка API: {e}"


def extract_keys(post_text):
    """Извлечение ключей из текста поста."""
    key_pattern = r'[A-Z0-9\*]{4,}-[A-Z0-9\*]{4,}-[A-Z0-9\*]{4,}'
    keys = re.findall(key_pattern, post_text)
    return keys


def resolve_asterisks(keys):
    """Замена символа * в ключах на числа от 0 до 9."""
    resolved_keys = []
    for key in keys:
        if '*' in key:  # Если есть символ *, заменяем его
            queue = [key]
            while '*' in queue[0]:  # Пока есть *, заменяем по очереди
                current_key = queue.pop(0)
                for digit in range(10):  # Числа от 0 до 9
                    queue.append(current_key.replace('*', str(digit), 1))  # Заменяем только первую *
            resolved_keys.extend(queue)  # Добавляем все варианты
        else:
            resolved_keys.append(key)  # Если нет *, оставляем как есть
    return resolved_keys

def key_string():
    # Получаем последний пост
    post_data = get_last_post(GROUP_ID,VK_API_KEY)
    if isinstance(post_data, dict):  # Если пост успешно получен
        print("Последний пост из группы:")
        print(f"Текст: {post_data['Текст поста']}")
    # Извлекаем ключи
    keys = extract_keys(post_data['Текст поста'])
    print("\nИзвлеченные ключи:")
    if keys:
        for key in keys:
            print(key)
        # Решаем ключи с * (заменяем звезды на цифры)
        resolved_keys = resolve_asterisks(keys)
        return resolved_keys
    else:
        print("Ключи не найдены.")
