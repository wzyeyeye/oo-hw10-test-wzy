# OO第三单元测试
## 使用方法
在文件夹下设置两个jar包，分别命名为code1.jar和code2.jar
测试模式有两种，随机测试和测试已知数据，在随机测试中有指令的专门测试
可设置指令条数和测试样例数
点击运行后，对拍相同显示AC，不同的话则停止测试并显示不同的输出和改行对应的输入
## 框架
* 数据生成器：
    * 根据规格，每种类型的指令可能有多个分支，需要保证每个分支都有可能出现，并控制好每个分支出现的可能性，比如出现异常的分支可能性应设置小一点。同时每种分支有前置条件，比如person在people里的前置条件是people至少有一个人。并且每个分支出现后具有影响，即规格中的assignable，需要保证实现相应影响，比如add person后必要将这个人加入到people里
* 对拍器：将input.txt输入给两个jar包，对比输出，完全相同则AC，否则输出出现差异的行数，对应输入，差异的输出
## 具体指令实现
### add person
1. Person以前不在people里
`!(\exists int i; 0 <= i && i < people.length; people[i].equals(person));`
2. Person本来就在people里(保证people不为空)
`(\exists int i; 0 <= i && i < people.length; people[i].equals(person));`

### add relation
1. id1的Person不在people里
`!contains(id1);`
2. id1的Person在people里，id2的Person不在people里(保证people至少有1个人)
`contains(id1) && !contains(id2);`
3. id1的Person在people里，id2的Person在people里，两个Person有关系(保证people至少有两个人，且至少有两个人有关系)
`contains(id1) && contains(id2) && getPerson(id1).isLinked(getPerson(id2));`
4. id1的Person在people里，id2的Person在people里，两个Person没有关系(保证people至少有两个人，且至少有两个人没有关系)
`contains(id1) && contains(id2) && !getPerson(id1).isLinked(getPerson(id2));`

### query value
1. id1的Person不在people里
`!contains(id1);`
2. id1的Person在people里，id2的Person不在people里(保证people至少有1个人)
`contains(id1) && !contains(id2);`
3. id1的Person在people里，id2的Person在people里，两个Person有关系(保证people至少有两个人，且至少有两个人有关系)
`contains(id1) && contains(id2) && getPerson(id1).isLinked(getPerson(id2));`
4. id1的Person在people里，id2的Person在people里，两个Person没有关系(保证people至少有两个人，且至少有两个人没有关系)
`contains(id1) && contains(id2) && !getPerson(id1).isLinked(getPerson(id2));


### query circle
1. id1的Person不在people里
`!contains(id1);`
2. id1的Person在people里，id2的Person不在people里(保证people至少有1个人)
`contains(id1) && !contains(id2);`
3. id1的Person在people里，id2的Person在people里(保证people至少有2个人)
`contains(id1) && contains(id2);`
    * ture (至少有一条边)
    * false (联通块数不为1)
### modify relation
1. id1的Person不在people里
`!contains(id1);`
2. id1的Person在people里，id2的Person不在people里(保证people至少有1个人)
`contains(id1) && !contains(id2);`
3. id1的Person在people里，id2的Person在people里,id1等于id2(保证people至少有1个人)
`contains(id1) && contains(id2) && id1 == id2;`
4. id1的Person在people里，id2的Person在people里,id1不等于id2,两个人没关系(保证people至少有2个人)
`contains(id1) && contains(id2) && id1 != id2 && !getPerson(id1).isLinked(getPerson(id2));`
5. id1的Person在people里，id2的Person在people里,id1不等于id2,两个人有关系(保证people至少有两个人，且至少有两个人有关系)
    * 不删边
`contains(id1) && contains(id2) && id1 != id2 && getPerson(id1).isLinked(getPerson(id2)) && getPerson(id1).queryValue(getPerson(id2)) + value > 0;`
    * 删边
`contains(id1) && contains(id2) && id1 != id2 && getPerson(id1).isLinked(getPerson(id2)) && getPerson(id1).queryValue(getPerson(id2)) + value <= 0;`

### query best acquaintance
1. id1的Person不在people里
`!contains(id);`
2. id1的Person在people里，但没有熟人
`contains(id) && getPerson(id).acquaintance.length == 0;`
3. id1的Person在people里，且有熟人
`contains(id) && getPerson(id).acquaintance.length != 0;`

### add_group
1. group在groups里(groups至少有一个group)
`(\exists int i; 0 <= i && i < groups.length;groups[i].equals(group));`
2. group不在groups里
`!(\exists int i; 0 <= i && i < groups.length;groups[i].equals(group));`


### add_to_group 
1. 没有id1的group
`!(\exists int i; 0 <= i && i < groups.length;groups[i].getId() == id2);`
2. 有id1的group，但people没有id2的人(groups至少有一个group)
`(\exists int i; 0 <= i && i < groups.length;groups[i].getId() == id2) && !(\exists int i; 0 <= i && i < people.length;people[i].getId() == id1);`
3. 有id1的group，people有id2的人，但group有id2的人(groups至少有一个group有人)
`(\exists int i; 0 <= i && i < groups.length;groups[i].getId() == id2) && (\exists int i; 0 <= i && i < people.length;people[i].getId() == id1) && getGroup(id2).hasPerson(getPerson(id1));`
4. 有id1的group，people有id2的人，group没有id2的人，group的人少于1111(groups至少有一个group，该group的人少于people的人)
`(\exists int i; 0 <= i && i < groups.length; groups[i].getId() == id2) &&(\exists int i; 0 <= i && i < people.length; people[i].getId() == id1) &&getGroup(id2).hasPerson(getPerson(id1)) == false &&getGroup(id2).people.length <= 1111;`
5. 有id1的group，people有id2的人，group没有id2的人，group的人多于1111(暂时不管)
`(\exists int i; 0 <= i && i < groups.length; groups[i].getId() == id2) &&(\exists int i; 0 <= i && i < people.length; people[i].getId() == id1) &&getGroup(id2).hasPerson(getPerson(id1)) == false && getGroup(id2).people.length > 1111;`

### del_from_group
1. 没有id1的group
`!(\exists int i; 0 <= i && i < groups.length;groups[i].getId() == id2);`
2. 有id1的group，但people没有id2的人(groups至少有一个group)
`(\exists int i; 0 <= i && i < groups.length;groups[i].getId() == id2) && !(\exists int i; 0 <= i && i < people.length;people[i].getId() == id1);`
3. 有id1的group，people有id2的人，但group没有id2的人(groups至少有一个group)
`(\exists int i; 0 <= i && i < groups.length;groups[i].getId() == id2) && (\exists int i; 0 <= i && i < people.length;people[i].getId() == id1) && !getGroup(id2).hasPerson(getPerson(id1));`
4. 有id1的group，people有id2的人，group有id2的人(groups至少有一个group有人)
`\exists int i; 0 <= i && i < groups.length; groups[i].getId() == id2) &&(\exists int i; 0 <= i && i < people.length; people[i].getId() == id1) &&getGroup(id2).hasPerson(getPerson(id1)) == true;`



### query_group_value_sum 
1. 没有id1的group
`!(\exists int i; 0 <= i && i < groups.length;groups[i].getId() == id);`
2. 有id1的group
`(\exists int i; 0 <= i && i < groups.length; groups[i].getId() == id);`

### query_group_age_var
1. 没有id1的group
`!(\exists int i; 0 <= i && i < groups.length;groups[i].getId() == id);`
2. 有id1的group
`(\exists int i; 0 <= i && i < groups.length; groups[i].getId() == id);`

### add_message
1. 有id的message
`(\exists int i; 0 <= i && i < messages.length;messages[i].equals(message));`
2. 没有id的message，且如果是单发则发给自己
`!(\exists int i; 0 <= i && i < messages.length;messages[i].equals(message)) && message.getType() == 0 && message.getPerson1() == message.getPerson2();`
3. 没有id的message，且如果是单发则不能发给自己
`!(\exists int i; 0 <= i && i < messages.length; messages[i].equals(message)) &&((message.getType() == 0) ==> (message.getPerson1() != message.getPerson2()));`
### send_message
1. 没有id的message
`!containsMessage(id);`
2. 有id的message，且为单发，但两人没关系
`containsMessage(id) && getMessage(id).getType() == 0 &&!(getMessage(id).getPerson1().isLinked(getMessage(id).getPerson2()));`
3. 有id的message，且为群发，但group里没有person
`containsMessage(id) && getMessage(id).getType() == 1 &&!(getMessage(id).getGroup().hasPerson(getMessage(id).getPerson1()));`
4. 有id的message，且为单发，两人有关系
`containsMessage(id) && getMessage(id).getType() == 0 &&getMessage(id).getPerson1().isLinked(getMessage(id).getPerson2()) &&getMessage(id).getPerson1() != getMessage(id).getPerson2();`
5. 有id的message，且为群发，group里没有person
`containsMessage(id) && getMessage(id).getType() == 1 &&getMessage(id).getGroup().hasPerson(getMessage(id).getPerson1());`

### query_social_value
1. 没有id的person
`!contains(id);`
2. 有id的person
`contains(id);`
### query_received_messages
1. 没有id的person
`!contains(id);`
2. 有id的person
`contains(id);`
  
### modifyRelationOKTest
**数据满足条件**
* beforeData满足
    * 人数在[0,10]中
    * 若id为id1的人有id为id2的acquaintance，且对应的value为v1；则id为id2的人有id为id1的acquaintance，且对应的value为v1
    * 给出的acquaintance的id一定存在，且不会同自身id相同。即不会出现id为id1的人有id为id2的acquaintance，但id为id2的人不存在或id2等于id1的情况
* afterData满足
    * 人数在[0,10]中
    * 给出的acquaintance的id一定存在，且不会同自身id相同。即不会出现id为id1的人有id为id2的acquaintance，但id为id2的人不存在或id2等于id1的情况

**异常**
>对于异常部分检测，我们进一步给出提示：如果检测出在当前状态下调用该方法会抛出异常，需要判断异常方法是否对于前后状态产生“副作用”，若无副作用，则认为符合规格，返回 0；否则认为不符合规格，返回 -1。此处，我们可以将“副作用”简单理解为，调用方法后的状态相较调用前的状态发生了改变。

没有id1的人，没有id2的人，id1等于id2，id1和id2没有关系

**ensures**
1. 前后人数相同
2. 之前的人在之后一定存在
3. 除id1和id2其他人不能改变
4. id1和id2有关系
5. id1和id2的value变为原来的value加改变的value
6. id2和id1的value变为原来的value加改变的value
7. id1熟人人数不变
8. id2熟人人数不变
9. id1熟人id不变
10. id2熟人id不变
11. id1除id2的熟人value不变
12. id2除id1的熟人value不变
13. id1的value的长度等于熟人的长度
14. id2的value的长度等于熟人的长度
15. id1和id2没有关系
16. id1熟人人数少1
17. id2熟人人数少1
18. id1的value的长度等于熟人的长度
19. id2的value的长度等于熟人的长度
20. 之后id1的熟人和value与之前一样
21. 之后id2的熟人和value与之前一样


### add_red_envelope_message
与add message类似

### add_notice_message
与add message类似

### clear_notices
1. contains(personId)
2. !contains(personId)

### add_emoji_message
与add message类似
emojiId有两种可能，一种是在emojiIdList中，一种不在

### store_emoji_id
1. (\exists int i; 0 <= i && i < emojiIdList.length; emojiIdList[i] == id)
2. !(\exists int i; 0 <= i && i < emojiIdList.length; emojiIdList[i] == id)

### query_popularity id(int)
1. contains(personId)
2. !contains(personId)

### delete_cold_emoji
limit范围

### query_money id(int)
1. contains(personId)
2. !contains(personId)

### query_least_moment
1. contains(personId)
2. !contains(personId)

### delete_cold_emoji_ok_test
1. 旧的emojiIdList中heat大于limit的在新的emojiIdList中存在
2. 新的emojiIdList中的所有emoji，在旧的emojiIdList中存在emoji与其id和heat相等
3. 新的emojiIdList的长度等于旧的emojiIdList中heat大于limit的emoji的个数
4. 新的emojiIdList的长度等于新的emojiHeatList的长度（不用判断）
5. 旧的messages中是emoji的并且在新的emojiMessages中存在的message，不能改变（即对应的emojiId仍然等于messageId）且在新的messages中存在
6. 旧的messages中不是emoji的message，不能改变（即对应的emojiId仍为null）且在新的messages中存在
7. 新的messages的长度等于旧的messages中不是emoji的message的个数加旧的messages中且在新的emojiIdList中存在的个数
8. 结果等于新的emojiIdList的长度

## 测试
可以专门测试某一种指令
### modify relation
该指令改变了两个人的价值以及可能改变两个人的关系，blockSum，tripleSum，coupleSum，这两个人的bestAcquaintance
因此在modify relation这条指令后分别测试改变的值
### group计算测试
add_group、add_to_group、del_from_group后测试query_group_value_sum、query_group_age_var
### message测试
add_message和send_message后测试query_social_valuequery_received_messages
### query_least_moment测试
加人加关系后测对所有人测试query_least_moment
