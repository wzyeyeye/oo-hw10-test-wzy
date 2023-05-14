import cmp
import random
import networkx as nx

instr_list = ['ap', 'ar', 'qv', 'qci', 'qbs', 'qts', 'mr', 'qcs', 'qba', 'ag', 'atg', 'dfg',
              'qgvs', 'qgav', 'am', 'sm', 'qsv', 'qrm']
group_list = set()
group_id_list = set()
message_id_list = set()
emoji_id_list = set()
G = nx.Graph()
min_id = 0
max_id = 10000
test_num = 100
instr_num = 10000


class Group:
    def __init__(self, group_id):
        self.id = group_id
        self.people = set()

    def add(self, person_id):
        self.people.add(person_id)

    def remove(self, person_id):
        self.remove(person_id)


def get_exist_id():
    return random.choice(list(G.nodes))


def get_unExist_id():
    un_exist_id = random.randint(min_id, max_id)
    while G.has_node(un_exist_id):
        un_exist_id = random.randint(min_id, max_id)
    return un_exist_id


def get_related_person_id():
    edge = random.choice(list(G.edges))
    related_id1 = edge[0]
    related_id2 = edge[1]
    return related_id1, related_id2


def get_unRelated_person_id():
    unrelated_id1 = get_exist_id()
    unrelated_id2 = get_exist_id()
    while G.has_edge(unrelated_id1, unrelated_id2) or unrelated_id1 == unrelated_id2:
        unrelated_id1 = get_exist_id()
        unrelated_id2 = get_exist_id()
    return unrelated_id1, unrelated_id2


def get_age():
    return random.randint(0, 200)


def get_value():
    return random.randint(1, 100)


def get_name():
    random_str = ""
    base_str = "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789"
    length = random.randint(1, 10)
    for j in range(length):
        random_str += base_str[random.randint(0, len(base_str) - 1)]
    return random_str


def add_person():
    prob = random.uniform(0, 1)
    add_person_age = get_age()
    add_person_name = get_name()
    if prob < 0.01 and G.number_of_nodes() > 0:
        add_person_id = get_exist_id()
    else:
        add_person_id = get_unExist_id()
        G.add_node(add_person_id, age=add_person_age, name=add_person_name)
    return "ap " + str(add_person_id) + " " + add_person_name + " " + str(add_person_age)


def add_relation():
    prob = random.uniform(0, 1)
    value = get_value()
    if prob < 0.95 and G.number_of_nodes() >= 2 and G.number_of_edges() < \
            G.number_of_nodes() * (G.number_of_nodes() - 1) / 2:
        add_relation_id1, add_relation_id2 = get_unRelated_person_id()
        G.add_edge(add_relation_id1, add_relation_id2, value=value)
    elif 0.95 <= prob < 0.96 and G.number_of_nodes() >= 2 and G.number_of_edges() >= 1:
        add_relation_id1, add_relation_id2 = get_related_person_id()
    elif 0.96 <= prob < 0.97 and G.number_of_nodes() >= 1:
        add_relation_id1 = get_exist_id()
        add_relation_id2 = get_unExist_id()
    else:
        add_relation_id1 = get_unExist_id()
        sub = random.uniform(0, 1)
        if sub < 0.5 and G.number_of_nodes() >= 1:
            add_relation_id2 = get_exist_id()
        else:
            add_relation_id2 = get_unExist_id()
    return "ar " + str(add_relation_id1) + " " + str(add_relation_id2) + " " + str(value)


def query_value():
    prob = random.uniform(0, 1)
    if prob < 0.95 and G.number_of_nodes() >= 2 and G.number_of_edges() >= 1:
        query_value_id1, query_value_id2 = get_related_person_id()
    elif 0.95 <= prob < 0.97 and G.number_of_nodes() >= 2 and G.number_of_edges() < G.number_of_nodes() * (
            G.number_of_nodes() - 1) / 2:
        query_value_id1, query_value_id2 = get_unRelated_person_id()
    elif 0.97 <= prob < 0.98 and G.number_of_nodes() >= 1:
        query_value_id1 = get_exist_id()
        query_value_id2 = get_unExist_id()
    else:
        query_value_id1 = get_unExist_id()
        sub = random.uniform(0, 1)
        if sub < 0.5 and G.number_of_nodes() >= 1:
            query_value_id2 = get_exist_id()
        else:
            query_value_id2 = get_unExist_id()
    return "qv " + str(query_value_id1) + " " + str(query_value_id2)


def query_circle():
    prob = random.uniform(0, 1)
    if prob < 0.97 and G.number_of_nodes() >= 2 and G.number_of_edges() >= 1:
        # sub = random.uniform(0, 1)
        query_circle_id1 = get_exist_id()
        query_circle_id2 = get_exist_id()
        # need to improve
        # divided into 2 kinds, the result is true or false
    elif 0.97 <= prob < 0.98 and G.number_of_nodes() >= 1:
        query_circle_id1 = get_exist_id()
        query_circle_id2 = get_unExist_id()
    else:
        query_circle_id1 = get_unExist_id()
        sub = random.uniform(0, 1)
        if sub < 0.5 and G.number_of_nodes() >= 1:
            query_circle_id2 = get_exist_id()
        else:
            query_circle_id2 = get_unExist_id()
    return "qci " + str(query_circle_id1) + " " + str(query_circle_id2)


def query_block_sum():
    return "qbs"


def query_triple_sum():
    return "qts"


def query_best_acquaintance():
    prob = random.uniform(0, 1)
    if prob < 0.99 and G.number_of_nodes() >= 2 and G.number_of_edges() >= 1:
        query_best_acquaintance_id = get_exist_id()
    else:
        query_best_acquaintance_id = get_unExist_id()
    return "qba " + str(query_best_acquaintance_id)


def modify_relation():
    prob = random.uniform(0, 1)
    modify_relation_value = get_value()
    if prob < 0.95 and G.number_of_nodes() >= 2 and G.number_of_edges() >= 1:
        modify_relation_id1, modify_relation_id2 = get_related_person_id()
        old_value = G[modify_relation_id1][modify_relation_id2]['value']
        sub = random.uniform(0, 1)
        if sub < 0.5:
            modify_relation_value = random.randint(-100, -old_value)
            G.remove_edge(modify_relation_id1, modify_relation_id2)
        else:
            modify_relation_value = random.randint(-old_value + 1, 100)
    elif 0.95 <= prob < 0.97 and G.number_of_nodes() >= 2 and G.number_of_edges() <= G.number_of_nodes() * (
            G.number_of_nodes() - 1) / 2:
        modify_relation_id1, modify_relation_id2 = get_unRelated_person_id()
    elif 0.97 <= prob < 0.98 and G.number_of_nodes() >= 1:
        modify_relation_id1 = get_exist_id()
        modify_relation_id2 = get_unExist_id()
    else:
        modify_relation_id1 = get_unExist_id()
        sub = random.uniform(0, 1)
        if sub < 0.5 and G.number_of_nodes() >= 1:
            modify_relation_id2 = get_exist_id()
        else:
            modify_relation_id2 = get_unExist_id()
    return "mr " + str(modify_relation_id1) + " " + str(modify_relation_id2) + " " + str(modify_relation_value)


def query_couple_sum():
    return "qcs"


def add_group():
    prob = random.uniform(0, 1)
    if prob < 0.01 and len(group_id_list) > 0:
        add_group_id = random.choice(list(group_id_list))
    else:
        add_group_id = random.randint(min_id, max_id)
        while add_group_id in group_id_list:
            add_group_id = random.randint(min_id, max_id)
        group_id_list.add(add_group_id)
        group_list.add(Group(add_group_id))
    return "ag " + str(add_group_id)


def add_to_group():
    prob = random.uniform(0, 1)
    if prob < 0.95 and len(group_id_list) > 0:
        add_to_group_id2 = random.choice(list(group_id_list))
        add_to_group_id1 = get_exist_id()
    elif 0.95 <= prob < 0.96 and len(group_id_list) > 0:
        add_to_group_id2 = random.choice(list(group_id_list))
        add_to_group_id1 = get_unExist_id()
    else:
        add_to_group_id2 = random.randint(min_id, max_id)
        while add_to_group_id2 in group_id_list:
            add_to_group_id2 = random.randint(min_id, max_id)
        add_to_group_id1 = get_exist_id()
    return "atg " + str(add_to_group_id1) + " " + str(add_to_group_id2)


def del_from_group():
    prob = random.uniform(0, 1)
    if prob < 0.98 and len(group_id_list) > 0:
        del_from_group_id2 = random.choice(list(group_id_list))
        del_from_group_id1 = get_exist_id()
    elif 0.98 <= prob < 0.99 and len(group_id_list) > 0:
        del_from_group_id2 = random.choice(list(group_id_list))
        del_from_group_id1 = get_unExist_id()
    else:
        del_from_group_id2 = random.randint(min_id, max_id)
        while del_from_group_id2 in group_id_list:
            del_from_group_id2 = random.randint(min_id, max_id)
        del_from_group_id1 = get_exist_id()
    return "dfg " + str(del_from_group_id1) + " " + str(del_from_group_id2)


def query_group_value_sum():
    prob = random.uniform(0, 1)
    if prob < 0.99 and len(group_id_list) > 0:
        query_group_value_sum_id = random.choice(list(group_id_list))
    else:
        query_group_value_sum_id = random.randint(min_id, max_id)
        while query_group_value_sum_id in group_id_list:
            query_group_value_sum_id = random.randint(min_id, max_id)
    return "qgvs " + str(query_group_value_sum_id)


def query_group_age_var():
    prob = random.uniform(0, 1)
    if prob < 0.99 and len(group_id_list) > 0:
        query_group_age_var_id = random.choice(list(group_id_list))
    else:
        query_group_age_var_id = random.randint(min_id, max_id)
        while query_group_age_var_id in group_id_list:
            query_group_age_var_id = random.randint(min_id, max_id)
    return "qgav " + str(query_group_age_var_id)


def add_message():
    prob = random.uniform(0, 1)
    add_message_social_value = random.randint(-1000, 1000)
    if prob < 0.01 and len(message_id_list) > 0:
        add_message_id = random.choice(list(message_id_list))
        add_message_type = random.randint(0, 1)
        add_message_person_id1 = random.randint(min_id, max_id)
        add_message_person_id2 = random.randint(min_id, max_id)
        add_message_group_id = random.randint(min_id, max_id)
    elif 0.01 <= prob < 0.02 and G.number_of_nodes() >= 1:
        add_message_id = random.randint(min_id, max_id)
        while add_message_id in message_id_list:
            add_message_id = random.randint(min_id, max_id)
        add_message_type = 0
        add_message_person_id1 = get_exist_id()
        add_message_person_id2 = add_message_person_id1
        add_message_group_id = random.randint(min_id, max_id)
    elif G.number_of_nodes() >= 2 and len(group_id_list) >= 1:
        add_message_id = random.randint(min_id, max_id)
        while add_message_id in message_id_list:
            add_message_id = random.randint(min_id, max_id)
        add_message_type = random.randint(0, 1)
        add_message_person_id1 = get_exist_id()
        add_message_person_id2 = get_exist_id()
        while add_message_person_id2 == add_message_person_id1:
            add_message_person_id2 = get_exist_id()
        add_message_group_id = random.choice(list(group_id_list))
        message_id_list.add(add_message_id)
    else:
        return ""
    if add_message_type == 0:
        return "am " + str(add_message_id) + " " + str(add_message_social_value) + " 0 " + str(
            add_message_person_id1) + " " + str(add_message_person_id2)
    elif add_message_type == 1:
        return "am " + str(add_message_id) + " " + str(add_message_social_value) + " 1 " + str(
            add_message_person_id1) + " " + str(add_message_group_id)
    else:
        return ""


def send_message():
    prob = random.uniform(0, 1)
    if prob < 0.99 and len(message_id_list) > 0:
        send_message_id = random.choice(list(message_id_list))
        # need to improve and add remove message action
    else:
        send_message_id = random.randint(min_id, max_id)
        while send_message_id in message_id_list:
            send_message_id = random.randint(min_id, max_id)
    return "sm " + str(send_message_id)


def query_social_value():
    prob = random.uniform(0, 1)
    if prob < 0.99 and G.number_of_nodes() >= 1:
        query_social_value_id = get_exist_id()
    else:
        query_social_value_id = get_unExist_id()
    return "qsv " + str(query_social_value_id)


def query_received_messages():
    prob = random.uniform(0, 1)
    if prob < 0.99 and G.number_of_nodes() >= 1:
        query_received_messages_id = get_exist_id()
    else:
        query_received_messages_id = get_unExist_id()
    return "qrm " + str(query_received_messages_id)


def add_red_envelope_message():
    prob = random.uniform(0, 1)
    money = random.randint(0, 200)
    if prob < 0.01 and len(message_id_list) > 0:
        add_message_id = random.choice(list(message_id_list))
        add_message_type = random.randint(0, 1)
        add_message_person_id1 = random.randint(min_id, max_id)
        add_message_person_id2 = random.randint(min_id, max_id)
        add_message_group_id = random.randint(min_id, max_id)
    elif 0.01 <= prob < 0.02 and G.number_of_nodes() >= 1:
        add_message_id = random.randint(min_id, max_id)
        while add_message_id in message_id_list:
            add_message_id = random.randint(min_id, max_id)
        add_message_type = 0
        add_message_person_id1 = get_exist_id()
        add_message_person_id2 = add_message_person_id1
        add_message_group_id = random.randint(min_id, max_id)
    elif G.number_of_nodes() >= 2 and len(group_id_list) >= 1:
        add_message_id = random.randint(min_id, max_id)
        while add_message_id in message_id_list:
            add_message_id = random.randint(min_id, max_id)
        add_message_type = random.randint(0, 1)
        add_message_person_id1 = get_exist_id()
        add_message_person_id2 = get_exist_id()
        while add_message_person_id2 == add_message_person_id1:
            add_message_person_id2 = get_exist_id()
        add_message_group_id = random.choice(list(group_id_list))
        message_id_list.add(add_message_id)
    else:
        return ""
    if add_message_type == 0:
        return "arem " + str(add_message_id) + " " + str(money) + " 0 " + str(
            add_message_person_id1) + " " + str(add_message_person_id2)
    elif add_message_type == 1:
        return "arem " + str(add_message_id) + " " + str(money) + " 1 " + str(
            add_message_person_id1) + " " + str(add_message_group_id)
    else:
        return ""


def add_notice_message():
    prob = random.uniform(0, 1)
    string = ""
    base_str = "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789"
    length = random.randint(1, 10)
    for j in range(length):
        string += base_str[random.randint(0, len(base_str) - 1)]
    if prob < 0.01 and len(message_id_list) > 0:
        add_message_id = random.choice(list(message_id_list))
        add_message_type = random.randint(0, 1)
        add_message_person_id1 = random.randint(min_id, max_id)
        add_message_person_id2 = random.randint(min_id, max_id)
        add_message_group_id = random.randint(min_id, max_id)
    elif 0.01 <= prob < 0.02 and G.number_of_nodes() >= 1:
        add_message_id = random.randint(min_id, max_id)
        while add_message_id in message_id_list:
            add_message_id = random.randint(min_id, max_id)
        add_message_type = 0
        add_message_person_id1 = get_exist_id()
        add_message_person_id2 = add_message_person_id1
        add_message_group_id = random.randint(min_id, max_id)
    elif G.number_of_nodes() >= 2 and len(group_id_list) >= 1:
        add_message_id = random.randint(min_id, max_id)
        while add_message_id in message_id_list:
            add_message_id = random.randint(min_id, max_id)
        add_message_type = random.randint(0, 1)
        add_message_person_id1 = get_exist_id()
        add_message_person_id2 = get_exist_id()
        while add_message_person_id2 == add_message_person_id1:
            add_message_person_id2 = get_exist_id()
        add_message_group_id = random.choice(list(group_id_list))
        message_id_list.add(add_message_id)
    else:
        return ""
    if add_message_type == 0:
        return "anm " + str(add_message_id) + " " + string + " 0 " + str(
            add_message_person_id1) + " " + str(add_message_person_id2)
    elif add_message_type == 1:
        return "anm " + str(add_message_id) + " " + string + " 1 " + str(
            add_message_person_id1) + " " + str(add_message_group_id)
    else:
        return ""


def clear_notices():
    prob = random.uniform(0, 1)
    if prob < 0.99 and G.number_of_nodes() > 0:
        person_id = get_exist_id()
    else:
        person_id = get_unExist_id()
    return "cn " + str(person_id)


def add_emoji_message():
    prob = random.uniform(0, 1)
    sub_prob = random.uniform(0, 1)
    if sub_prob < 0.99 and len(emoji_id_list) > 0:
        emoji_id = random.choice(list(emoji_id_list))
    else:
        emoji_id = random.randint(0, 10000)
        while emoji_id in emoji_id_list:
            emoji_id = random.randint(0, 10000)

    if prob < 0.01 and len(message_id_list) > 0:
        add_message_id = random.choice(list(message_id_list))
        add_message_type = random.randint(0, 1)
        add_message_person_id1 = random.randint(min_id, max_id)
        add_message_person_id2 = random.randint(min_id, max_id)
        add_message_group_id = random.randint(min_id, max_id)
    elif 0.01 <= prob < 0.02 and G.number_of_nodes() >= 1:
        add_message_id = random.randint(min_id, max_id)
        while add_message_id in message_id_list:
            add_message_id = random.randint(min_id, max_id)
        add_message_type = 0
        add_message_person_id1 = get_exist_id()
        add_message_person_id2 = add_message_person_id1
        add_message_group_id = random.randint(min_id, max_id)
    elif G.number_of_nodes() >= 2 and len(group_id_list) >= 1:
        add_message_id = random.randint(min_id, max_id)
        while add_message_id in message_id_list:
            add_message_id = random.randint(min_id, max_id)
        add_message_type = random.randint(0, 1)
        add_message_person_id1 = get_exist_id()
        add_message_person_id2 = get_exist_id()
        while add_message_person_id2 == add_message_person_id1:
            add_message_person_id2 = get_exist_id()
        add_message_group_id = random.choice(list(group_id_list))
        message_id_list.add(add_message_id)
    else:
        return ""
    if add_message_type == 0:
        return "aem " + str(add_message_id) + " " + str(emoji_id) + " 0 " + str(
            add_message_person_id1) + " " + str(add_message_person_id2)
    elif add_message_type == 1:
        return "aem " + str(add_message_id) + " " + str(emoji_id) + " 1 " + str(
            add_message_person_id1) + " " + str(add_message_group_id)
    else:
        return ""


def store_emoji_id():
    prob = random.uniform(0, 1)

    if prob < 0.01 and len(emoji_id_list) > 0:
        emoji_id = random.choice(list(emoji_id_list))
    else:
        emoji_id = random.randint(0, 10000)
        while emoji_id in emoji_id_list:
            emoji_id = random.randint(0, 10000)
        emoji_id_list.add(emoji_id)
    return "sei " + str(emoji_id)


def query_popularity():
    prob = random.uniform(0, 1)

    if prob < 0.99 and len(emoji_id_list) > 0:
        emoji_id = random.choice(list(emoji_id_list))
    else:
        emoji_id = random.randint(0, 10000)
        while emoji_id in emoji_id_list:
            emoji_id = random.randint(0, 10000)
    return "qp " + str(emoji_id)


def delete_cold_emoji():
    limit = random.randint(1, 1)
    return "dce " + str(limit)


def query_money():
    prob = random.uniform(0, 1)
    if prob < 0.99 and G.number_of_nodes() > 0:
        person_id = get_exist_id()
    else:
        person_id = get_unExist_id()
    return "qm " + str(person_id)


def query_least_moment():
    prob = random.uniform(0, 1)
    if prob < 0.99 and G.number_of_nodes() > 0:
        person_id = get_exist_id()
    else:
        person_id = get_unExist_id()
    return "qlm " + str(person_id)


def get_instr(instr_variety):
    if instr_variety == 'ap':
        return add_person()
    elif instr_variety == 'ar':
        return add_relation()
    elif instr_variety == 'qv':
        return query_value()
    elif instr_variety == 'qci':
        return query_circle()
    elif instr_variety == 'qbs':
        return query_block_sum()
    elif instr_variety == 'qts':
        return query_triple_sum()
    elif instr_variety == 'mr':
        return modify_relation()
    elif instr_variety == 'qcs':
        return query_couple_sum()
    elif instr_variety == 'qba':
        return query_best_acquaintance()
    elif instr_variety == 'ag':
        return add_group()
    elif instr_variety == 'atg':
        return add_to_group()
    elif instr_variety == 'dfg':
        return del_from_group()
    elif instr_variety == 'qgvs':
        return query_group_value_sum()
    elif instr_variety == 'qgav':
        return query_group_age_var()
    elif instr_variety == 'am':
        return add_message()
    elif instr_variety == 'sm':
        return send_message()
    elif instr_variety == 'qsv':
        return query_social_value()
    elif instr_variety == 'qrm':
        return query_received_messages()


def test(num):
    # init
    G.clear()
    group_id_list.clear()
    group_list.clear()
    message_id_list.clear()
    emoji_id_list.clear()
    f = open("in.txt", "w")
    # message test
    '''
    for k in range(200):
        f.write(add_person() + '\n')
    for k in range(200):
        f.write(add_relation() + '\n')
    for k in range(10):
        f.write(add_group() + '\n')
    for k in range(100):
        f.write(add_to_group() + '\n')
    for k in range(1000):
        f.write(add_message() + '\n')
        f.write(send_message() + '\n')
        f.write(query_social_value() + '\n')
        f.write(query_received_messages() + '\n')'''
    # group test
    '''
    group_test_instr = ['ap', 'ar', 'mr', 'atg', 'dfg']
    for k in range(200):
        f.write(add_person() + '\n')
    for k in range(20):
        f.write(add_group() + '\n')
    for k in range(1000):
        group_test_instr_type = random.choice(list(group_test_instr))
        if group_test_instr_type == 'ap':
            f.write(add_person() + '\n')
        elif group_test_instr_type == 'ar':
            f.write(add_relation() + '\n')
        elif group_test_instr_type == 'mr':
            f.write(modify_relation() + '\n')
        elif group_test_instr_type == 'atg':
            f.write(add_to_group() + '\n')
        elif group_test_instr_type == 'dfg':
            f.write(del_from_group() + '\n')
    '''
    # modify relation test
    # need to revise return of modify_relation
    '''
    for k in range(50):
        instr = add_person()
        f.write(instr + '\n')
    for k in range(1000):
        instr = add_relation()
        f.write(instr + '\n')
    for k in range(10000):
        instr, modify_relation_id1, modify_relation_id2 = modify_relation()
        f.write(instr + '\n')
        f.write("qba " + str(modify_relation_id1) + '\n')
        f.write("qba " + str(modify_relation_id2) + '\n')
        f.write("qv " + str(modify_relation_id1) + " " + str(modify_relation_id2) + '\n')
        f.write("qcs\n")
        f.write("qts\n")
        f.write("qbs\n")'''
    '''
    # comprehensive test
    for k in range(200):
        f.write(add_person() + '\n')
    for k in range(1000):
        f.write(add_relation() + '\n')
    for k in range(num):
        instr_type = random.choice(instr_list)
        instr = get_instr(instr_type)
        f.write(instr + '\n')
    '''
    # red_envelope_message test
    '''
    for k in range(100):
        f.write(add_person() + '\n')
    for k in range(5000):
        f.write(add_relation() + '\n')
    for k in range(10):
        f.write(add_group() + '\n')
    for k in range(90):
        f.write(add_to_group() + '\n')
    for k in range(100):
        f.write(add_red_envelope_message() + '\n')
    for k in range(100):
        f.write(send_message() + '\n')
        for m in range(100):
            f.write(query_social_value() + '\n')
            f.write(query_money() + '\n')
    '''
    # notice_message test
    '''
    for k in range(100):
        f.write(add_person() + '\n')
    for k in range(5000):
        f.write(add_relation() + '\n')
    for k in range(10):
        f.write(add_group() + '\n')
    for k in range(90):
        f.write(add_to_group() + '\n')
    for k in range(100):
        f.write(add_notice_message() + '\n')
    for k in range(100):
        f.write(send_message() + '\n')
        for m in range(100):
            f.write(query_social_value() + '\n')
    '''
    # emoji_message test
    '''
    for k in range(100):
        f.write(add_person() + '\n')
    for k in range(5000):
        f.write(add_relation() + '\n')
    for k in range(10):
        f.write(add_group() + '\n')
    for k in range(100):
        f.write(add_to_group() + '\n')
    for k in range(10):
        f.write(store_emoji_id() + '\n')
    for k in range(100):
        f.write(add_emoji_message() + '\n')
    for k in range(100):
        f.write(send_message() + '\n')
        for m in range(100):
            f.write(query_social_value() + '\n')
            f.write(query_popularity() + '\n')
    '''
    # delete_cold_emoji test
    '''
    for k in range(100):
        f.write(add_person() + '\n')
    for k in range(2000):
        f.write(add_relation() + '\n')
    for k in range(10):
        f.write(add_group() + '\n')
    for k in range(100):
        f.write(add_to_group() + '\n')
    for k in range(10):
        f.write(store_emoji_id() + '\n')
    for k in range(100):
        f.write(add_emoji_message() + '\n')
    for k in range(100):
        f.write(add_notice_message() + '\n')
    for k in range(100):
        f.write(add_red_envelope_message() + '\n')
    for k in range(100):
        f.write(send_message() + '\n')
    f.write(delete_cold_emoji() + '\n')
    for k in range(100):
        f.write(send_message() + '\n')
        for m in range(100):
            f.write(query_social_value() + '\n')
            f.write(query_popularity() + '\n')
    '''
    # query_least_moment test
    for k in range(100):
        f.write(add_person() + '\n')
    for k in range(200):
        f.write(add_relation() + '\n')
    for k in list(G.nodes):
        f.write('qlm ' + str(k) + ' \n')
    f.close()
    return cmp.cmp()


def test_known_data():
    if cmp.cmp():
        print("AC")
    else:
        print("WA")


def test_generate_data():
    for i in range(test_num):
        if test(instr_num) is False:
            print(str(i + 1) + ': WA')
            break
        else:
            print(str(i + 1) + ': AC')


if __name__ == '__main__':
    # test_known_data()
    test_generate_data()
