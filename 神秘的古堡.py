#定义房间信息
rooms = {
    "Foyer":{
        "name":"Foyer",
        "description":"你身处古堡的阴暗门厅。头顶一盏布满蜘蛛网的吊灯微微摇晃，投下忽明忽暗的光芒。空气中弥漫着潮湿的霉味，脚下是冰冷的大理石地面。北面是一扇沉重的橡木门，门上雕刻着狰狞的怪兽头像，东面则是一条通向黑暗深处的走廊。",
        "exits":{"north":"Grand Hall","east":"Hallway"},
        "items":["门厅地毯下的纸条"]
    },
    "Grand Hall":{
        "name":"Grand Hall",
        "description":"你推开橡木门，进入了古堡的宏伟的大厅。尽管岁月流逝，依稀可见昔日的辉煌。一个巨大的水晶吊灯（虽然已经缺了几盏灯泡）仍然悬挂在高耸的天花板上。彩色玻璃窗阻挡了外界的光线，使得大厅内光线昏暗。南面是你进来的门厅，西面是一扇装饰华丽的木门，通往图书馆，东面则是一道拱形石门，通向餐厅。",
        "exits":{"south":"Foyer","west":"Library","east":"Dining Room"},
        "items":["壁炉拔火棍"]
    },
    "Hallway":{
        "name":"Hallway",
        "description":"你沿着昏暗的走廊前行，脚踩在吱吱作响的木地板上。墙壁上挂着褪色的家族画像，画像中的人物表情模糊不清，仿佛在注视着你。走廊尽头似乎传来微弱的滴水声。西面是门厅。",
        "exits":{"west":"Foyer"},
        "items":["生锈的铁钥匙"]
    },
    "Library":{
        "name":"Library",
        "description":"你推开装饰华丽的木门，走进了布满灰尘的图书馆。高耸的书架一直延伸到天花板，上面堆满了布满灰尘的书籍。空气中弥漫着浓重的旧书和皮革的味道，令人昏昏欲睡。阳光透过高窗洒进来，照亮了书架上零星散落的金箔。东面是通往大厅的木门。",
        "exits":{"east":"Grand Hall"},
        "items":["一本厚重的古书"]
    },
    "Dining Room":{
        "name":"Dining Room",
        "description":"你穿过拱形石门，来到了宽敞的餐厅。长长的橡木餐桌上布满了厚厚的灰尘，锈迹斑斑的银质餐具散落在桌面上，仿佛一场盛宴突然中断。墙壁上挂着巨大的狩猎场景油画，画布已经开始剥落。西面是通往大厅的拱形石门，北面是一扇破旧的木门，通向厨房。",
        "exits":{"west":"Grand Hall","north":"Kitchen"},
        "items":["餐桌上的银色烛台"]
    },
    "Kitchen":{
        "name":"Kitchen",
        "description":"你推开破旧的木门，进入了阴冷潮湿的厨房。腐烂的气味扑鼻而来，令人作呕。生锈的厨具散落在各处，巨大的壁炉已经冰冷，炉膛里堆满了黑色的灰烬。南面是餐厅。地板中央，你注意到一块不寻常的木板，似乎可以移动，也许是一个隐蔽的活板门，通往地下。",
        "exits":{"south":"Dining Room","down":"地下通道"},
        "items":["壁炉旁的火柴","水槽边的水桶"]
    },
    "地下通道":{
        "name":"地下通道",
        "description":"你成功逃离了古堡！",
        "exits":{},
        "items":[]
    }
}

#玩家初始位置
current_room = "Foyer"
inventory = []  #创建一个空背包列表

#帮助(help)菜单信息
def help():
    print("help - 显示帮助信息")
    print("look - 查看当前房间信息")
    print("go [方向] - 向指定方向移动(例如：north,south,west,east,down)")
    print("take [物品名称] - 拾取房间内的物品")
    print("inventory - 查看背包")
    print("quit - 退出游戏")

#查看（look）房间信息
def describe_room(room):
    print(f"你身处{room['name']}")
    print(room["description"])
    if room["items"]:
        print("房间里有:")
        for item in room["items"]:
            print(f"- {item}")
    else:
        print("房间里没有明显的物品。")
    if room["exits"]:
        print("你可以向以下方向移动：")
        for direction,target in room["exits"].items():  #items()是用来遍历的方法
            print(f"- {direction} ({target})")
        else:
            print("没有明显的出口")

#移动(go)
def move_player(direction):
    global current_room
    room = rooms[current_room]
    if direction in room["exits"]:
        current_room = room["exits"][direction]
        print(f"向{direction}移动，进入{current_room}")
        describe_room(rooms[current_room])
        if current_room == "地下通道":
            print("你成功逃离了古堡！")
            exit()
        else:
            print("那边没有路")

#捡道具（take）
def take_item(item_name):
    room = rooms[current_room]
    if item_name in room["items"]:
        room["items"].remove(item_name)
        inventory.append(item_name)
        print(f"你拿起了{item_name}")
    else:
        print(f"这里没有{item_name}")

#查看背包（inventory）
def inventory_item():
    if inventory:
        print("你的背包里有：")
        for item in inventory:
            print(f"- {item}")
    else:
        print("你的背包是空的")

#功能模块
def handle_input(command):
    if command == "help":
        help()
    elif command == "look":
        describe_room(rooms[current_room])
    elif command.startswith("go"):
        direction = command.split(" ")[1]  #split(" ")是用来拆分输入单词以识别对应位置属性的
        move_player(direction)
    elif command.startswith("take"):
        item_name = command.split(" ")[1]
        take_item(item_name)
    elif command == "inventory":
        inventory_item()
    elif command in ["quit","exit"]:
        print("")
        exit()
    else:
        print("无效指令，请输入help查看指令")

#主函数
def main():
    print("神秘的古堡")
    describe_room(rooms[current_room])
    while True:
        command = input(">").strip().lower()
        handle_input(command)

#起洞
main()
